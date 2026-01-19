import dash
from dash import dcc, Input, Output, dash_table, callback
import plotly.express as px
import dash_bootstrap_components as dbc
from data_loader import load_all_time_results

# Initialize the Dash app
dash.register_page(__name__, path='/fields', name="Fields")

df = load_all_time_results()

# Exclude rows where Outcome is blank (NaN or empty string)
df = df[df["Outcome"].notna() & (df["Outcome"].astype(str).str.strip() != "")]

# Convert Latitude and Longitude values to float with correct decimal format
df['Latitude'] = df['Latitude'].astype(str).str.replace(",", ".").astype(float)/1000
df['Longitude'] = df['Longitude'].astype(str).str.replace(",", ".").astype(float)/1000

# Preprocessing function
def prepare_summary(df):
   df_grouped = df.groupby('Pitch').agg({
       'Competition': 'count',
       'Wins': 'sum',
       'Draws': 'sum',
       'Losses': 'sum',
       'Latitude': 'first',
       'Longitude': 'first',
   }).reset_index()
   df_grouped.rename(columns={
       'Competition': 'Matches',
   }, inplace=True)
   df_grouped['Wins'] = df_grouped.apply(lambda x: f"{x['Wins']} ({x['Wins']/x['Matches']:.0%})", axis=1)
   df_grouped['Draws'] = df_grouped.apply(lambda x: f"{x['Draws']} ({x['Draws']/x['Matches']:.0%})", axis=1)
   df_grouped['Losses'] = df_grouped.apply(lambda x: f"{x['Losses']} ({x['Losses']/x['Matches']:.0%})", axis=1)
   
   # Sort by Pitch alphabetically
   df_grouped = df_grouped.sort_values(by='Pitch')
   return df_grouped

# Layout of the Dash app
layout = dbc.Container([
   dbc.Row([
       dbc.Col([
           dcc.Dropdown(
               id='competition-filter',
               options=['League','Cup','Friendly','Post-Corona Tournament 2020'],
               placeholder="Competition",
               value="League",
               clearable=False,
               multi=True,
               style={
                       "background-color": "transparent",
                       "color": "black",
                       "font-weight": "bold",
                       "width": "50%",
                   },
           )
       ], style={'display': 'flex', 'flex-direction': 'column', 'gap': '8px', 'margin-bottom': '20px'},
       width=12)
   ]),
   dbc.Row([
       dbc.Col([
           dcc.Graph(id='pitch-map',
                     config={"scrollZoom": True},  # Enable mouse scroll zoom
                     )
       ], xs=12, sm=12, md=12, lg=6),
       dbc.Col([
           dash_table.DataTable(
               id='pitch-table',
               sort_action="native",       # enables data to be sorted per-column by user or not ('none')
               sort_mode="single",         # sort across 'multi' or 'single' columns
               style_table={'overflowX': 'auto'},
               style_cell={'textAlign': 'center', 'minWidth': '70px'},
               style_data={
                   "minWidth": "70px",
                   "width": "auto",
                   "maxWidth": "180px",
                   'backgroundColor': 'rgb(0, 43, 54)',
                   'color': 'white',            
                   'border': '1px solid white',
                   'textAlign': 'center',
                   "height": "auto"
                   },
               style_header={
                   'backgroundColor': 'rgb(0, 43, 54)',
                   'color': 'white',
                   'fontWeight': 'bold',
                   'textAlign': 'center',
                   "whiteSpace": "normal",
                   },
           )
       ], xs=12, sm=12, md=12, lg=6),
   ])
], fluid=True)

# Callback to update the table based on the filters
@callback(    
   Output('pitch-map', 'figure'),
   Output('pitch-table', 'data'),
   Output('pitch-table', 'columns'),
   Input('competition-filter', 'value')
)

def update_tables(selected_competition):
   filtered_df = df.copy()
        # Apply filters for Competition
   if selected_competition:
       if isinstance(selected_competition, str): # Ensure selected_competition is treated as a list for filtering
           selected_competition = [selected_competition]
       filtered_df = filtered_df[filtered_df["Competition"].isin(selected_competition)] # Filter dataframe based on selected competition
   summary_df = prepare_summary(filtered_df)

   # Custom tooltip text
   summary_df['tooltip'] = (
       summary_df['Pitch'] +
       "<br>Matches: " + summary_df['Matches'].astype(str) +
       "<br>Wins: " + summary_df['Wins'].astype(str) +
       "<br>Draws: " + summary_df['Draws'].astype(str) +
       "<br>Losses: " + summary_df['Losses'].astype(str)
   )

   # Create map
   fig = px.scatter_mapbox(
       summary_df,
       lat="Latitude",
       lon="Longitude",
       size="Matches",
       size_max=40,
       zoom=11,
       center={"lat": 50.0755, "lon": 14.4378},  # Prague
       height=500,
       hover_name=None,
       hover_data={"Matches": False, "Wins": False, "Draws": False, "Losses": False, "Latitude": False, "Longitude": False, 'tooltip': True},
       text=None,
       template='plotly_dark'
       )
   
   fig.update_traces(
       marker=dict(
           size=14,
           color="rgb(228, 155, 88)",
           opacity = 0.7,
       ),
       hovertemplate=(
       "<b><span style='font-size:16px'>%{customdata[0]}</span></b><br>" +  # Pitch
       "Matches: %{customdata[1]}<br>" +
       "Wins: %{customdata[2]}<br>" +
       "Draws: %{customdata[3]}<br>" +
       "Losses: %{customdata[4]}<br><extra></extra>"
   ),
   customdata=summary_df[['Pitch', 'Matches', 'Wins', 'Draws', 'Losses']].values
   )

   fig.update_layout(mapbox_style="carto-positron")

   # Update layout for clarity
   fig.update_layout(
       margin={"r": 0, "t": 0, "l": 0, "b": 0},
       hoverlabel=dict(
           bgcolor="white",
           font_size=12,
           font_color="black",
           bordercolor="lightgray",
       ),
       dragmode="zoom",  # Enable zooming with mouse
       uirevision="constant",  # Enables zoom retention and user interactions
   )
   # Table setup
   table_data = summary_df[['Pitch', 'Matches', 'Wins', 'Draws', 'Losses']].to_dict('records')
   table_columns = [{'name': col, 'id': col} for col in ['Pitch', 'Matches', 'Wins', 'Draws', 'Losses']]

   return fig, table_data, table_columns
