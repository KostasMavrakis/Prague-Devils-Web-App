import dash
from dash import dcc, html, Input, Output, dash_table, callback
import pandas as pd
import dash_bootstrap_components as dbc
from data_loader import load_performance_stats

# Initialize the Dash app
dash.register_page(__name__, path='/performance', name="Trackers")

df = load_performance_stats()

# Extract header tooltips from first 4 rows
# Generate header tooltips based on first 4 rows
header_tooltips = {}
cols_to_exclude = ["Tracker", "Category", "Description", "Metric", "Data Type", "Team's Average", "Delta"]
for col in df.columns:
   if col == "Average Pro Player":
       # Special tooltip with line breaks
       header_tooltips[col] = {
           "value": "Sources:  \nFootball Observatory  \nFIFA Training Centre  \nPubMed Central  \nResearchGate",
           "type": "markdown"   # allow markdown/HTML rendering
       }
   elif col in cols_to_exclude:
       header_tooltips[col] = ''
   else:
       tooltip_lines = []
       for i in range(4):  # Use first 4 rows
           metric = df.at[i, 'Metric']
           value = df.at[i, col]
           tooltip_lines.append(f"{metric}: {value}")
           header_tooltips[col] = {
                               'value':"  \n".join(tooltip_lines),
                               'type': 'markdown'                                
                               }
# Display sample header tooltips dictionary
header_tooltips

# Convert comma-separated floats to dot-separated floats for rows with "Data Type" == "Float"
float_rows = df['Data Type'] == 'Float'
df.loc[float_rows, df.columns[5:]] = df.loc[float_rows, df.columns[5:]].applymap(
   lambda x: float(str(x).replace(',', '.')) if isinstance(x, str) and ',' in x else x
)/100

# Convert the Image URLs to markdown
# Define the columns that should NOT contain images
non_image_cols = ["Tracker", "Category", "Description", "Metric", "Data Type", "Team's Average", "Average Pro Player", "Delta"]

# Dynamically select image columns by excluding the non-image ones
image_cols = [col for col in df.columns if col not in non_image_cols]

# Convert image URLs to markdown for rows where Data Type == "Image"
for col in image_cols:
   df.loc[df["Data Type"] == "Image", col] = df.loc[df["Data Type"] == "Image", col].apply(
       lambda x: f'<div style="text-align:center;"><img src="{x}" style="height:150px; width:auto;"></div>' if isinstance(x, str) and x.startswith("http") else ""
   )
# List of markdown columns: Metric + image columns
markdown_cols = ["Metric"] + list(image_cols)
data_filtered = df[df["Tracker"] != "N/A"]
# Remove "Description" and "Data Type" from display
data_display = data_filtered.drop(columns=["Tracker", "Category", "Description", "Data Type"])

# Preparing the table data (excluding 'Description' and 'Data Type' columns)
columns_to_display = data_display.columns

# Layout of the Dash app
layout = html.Div([
   html.Div([
       html.A([
               html.Img(src="/assets/statsports.png", style={'width': '100%', 'maxWidth': '100px', 'height': 'auto'})
           ], href='https://www.soccerscene.com.au/statsports-apex-athlete-track-like-a-pro/', target="_blank"),
       html.A([
               html.Img(src="/assets/footbar.png", style={'width': '100%', 'maxWidth': '100px', 'height': 'auto', 'marginLeft': '5px'})
           ], href='https://www.soccerscene.com.au/footbar-meteor-tracker-a-data-tracker-for-everyone/', target="_blank"),
   html.Div(
       dcc.Dropdown(
               id='category-filter',
               options=[{'label': category, 'value': category} for category in sorted(df['Category'].dropna().unique()) if category!= "N/A"],
               placeholder='Category',
               multi=True,
               style={
                       "background-color": "transparent",
                       "color": "black",
                       "font-weight": "bold",
                       "width": '200px',
                   },
               className="mb-3"
           ),
           style={'marginLeft': '20px'},
   ),
   html.Div(
       dcc.Dropdown(
               id='tracker-filter',
               options=[{'label': tracker, 'value': tracker} for tracker in sorted(df['Tracker'].dropna().unique()) if tracker!= "N/A"],
               placeholder='Tracker',
               #value=["STATSports APEX", "Footbar Meteor"],
               multi=True,
               style={
                       "background-color": "transparent",
                       "color": "black",
                       "font-weight": "bold",
                       "width": '200px',
                   },
               className="mb-3"
           ),
           style={'marginLeft': '10px'},
   ),
   ], style={
       'display': 'flex',
       'alignItems': 'center',
       'justifyContent': 'center',
       'flexWrap': 'wrap',  # Makes the layout responsive
       'gap': '20px',
       'marginTop': '20px'
   }),
   html.Div([
       dash_table.DataTable(
               id='performance-table',
               columns=[
                   {
                       "name": col,
                       "id": col,
                       "presentation": "markdown" if col == "Metric" else "input",
                       "presentation": "markdown" if col in image_cols else "input",
                       "selectable": True,
                       "hideable": True
                   } for col in data_display.columns if col in columns_to_display
               ],
               tooltip_data=[],
               tooltip_header=header_tooltips,
               column_selectable="multi",  # allows users to select 'multi' or 'single' columns
               style_cell={"textAlign": "center", "whiteSpace": "normal"},
               style_header_conditional=[
                   {
                       'if': {'column_id': col},
                       'whiteSpace': 'pre-line'   # allows line feeds in tooltips
                       } for col in columns_to_display
                       ],
               style_table={
                   'overflowX': 'auto',
                   'grid-template-columns': '1fr 0.2fr'  # Adjusts the width ratio of the columns
                   },
               style_data={
                   "minWidth": "145px",
                   "width": "auto",
                   "maxWidth": "350px",
                   'backgroundColor': 'rgb(0, 43, 54)',
                   'color': 'white',
                   #"whiteSpace": "normal",
                   'border': '1px solid white',
                   'textAlign': 'center',
                   "height": "auto"
                   },
               fill_width=True,
               page_size=100,
               fixed_rows={"headers": True},
               style_header={
                   'backgroundColor': 'rgb(0, 43, 54)',
                   'color': 'white',
                   'fontWeight': 'bold',
                   'textAlign': 'center',
                   "whiteSpace": "normal",
                   },
               markdown_options={"html": True, "link_target": "_blank"},
               #dangerously_allow_html=True  # This enables HTML in cells (for images)
           )
   ], style={'padding': '0 20px'})
])

# Callback to update the table based on the filters
@callback(
   Output('performance-table', 'data'),
   Output('performance-table', 'tooltip_data'),
   Input('category-filter', 'value'),
   Input('tracker-filter', 'value')
)
def update_table(selected_category, selected_tracker):
   filtered_df = data_filtered.copy()
   # Apply filters for Category and Tracker
   # Apply Tracker filter only if something is selected
   if selected_tracker:
       if isinstance(selected_tracker, str):  # Ensure selected_tracker is treated as a list for filtering
           selected_tracker = [selected_tracker]
       filtered_df = filtered_df[filtered_df["Tracker"].isin(selected_tracker)]
   # Apply Category filter only if something is selected
   if selected_category:
       if isinstance(selected_category, str):  # Ensure selected_category is treated as a list for filtering
           selected_category = [selected_category]
       filtered_df = filtered_df[filtered_df["Category"].isin(selected_category)]
   # Prepare display table
   df_display = filtered_df.drop(columns=["Tracker", "Category", "Description", "Data Type"])
   table_data = df_display.to_dict('records')
   # Create metric to description mapping for the filtered data
   metric_to_description = {
       row['Metric']: row['Description']
       for _, row in filtered_df.iterrows()
       if pd.notna(row.get('Metric')) and pd.notna(row.get('Description'))
   }
   # Build row-level tooltips
   tooltip_data = []
   for _, row in df_display.iterrows():
       tooltip_row = {}
       for col in df_display.columns:
           if col == "Metric":
               tooltip_row[col] = {
                   'value': metric_to_description.get(row["Metric"], ""),
                   'type': 'markdown'
               }
           else:
               tooltip_row[col] = None
       tooltip_data.append(tooltip_row)

   return table_data, tooltip_data
