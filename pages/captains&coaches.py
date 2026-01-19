import dash
from dash import dcc, dash_table, Input, Output, callback
import dash_bootstrap_components as dbc
from data_loader import load_all_time_results

# Initialize the Dash app
dash.register_page(__name__, path='/c&c', name="Coaches & Captains")

df = load_all_time_results()

# Exclude rows where Outcome is blank (NaN or empty string)
df = df[df["Outcome"].notna() & (df["Outcome"].astype(str).str.strip() != "")]

# Preprocessing function
def prepare_summary(df, group_col):

    df_grouped = df.groupby(group_col).agg({
        'Season': lambda x: ', '.join(sorted(set(x))),
        'Competition': 'count',
        'Wins': 'sum',
        'Draws': 'sum',
        'Losses': 'sum'
    }).reset_index()

    df_grouped.rename(columns={
        group_col: 'Name',
        'Competition': 'Matches',
        'Season': 'Seasons'
    }, inplace=True)

    df_grouped['Wins'] = df_grouped.apply(lambda x: f"{x['Wins']} ({x['Wins']/x['Matches']:.0%})", axis=1)
    df_grouped['Draws'] = df_grouped.apply(lambda x: f"{x['Draws']} ({x['Draws']/x['Matches']:.0%})", axis=1)
    df_grouped['Losses'] = df_grouped.apply(lambda x: f"{x['Losses']} ({x['Losses']/x['Matches']:.0%})", axis=1)

    # Sort by Seasons alphabetically
    df_grouped = df_grouped.sort_values(by='Seasons')

    return df_grouped[['Name', 'Seasons', 'Matches', 'Wins', 'Draws', 'Losses']]

# Layout of the Dash app
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='role-selector',
                options=[
                    {'label': 'Coaches', 'value': 'Coach'},
                    {'label': 'Captains', 'value': 'Captain'}
                ],
                value='Coach',
                clearable=False,
                multi=False,
                style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "50%",
                    },
            ),
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
            dash_table.DataTable(
                id='summary-table',
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
                page_size=15,
            )
        ], width=12),
    ])
], fluid=True)

# Callback to update the table based on the filters
@callback(    
    Output('summary-table', 'data'),
    Output('summary-table', 'columns'),
    Input('role-selector', 'value'),
    Input('competition-filter', 'value')
)

def update_tables(role, selected_competition):
    filtered_df = df.copy()

    # Apply filters for Competition
    if selected_competition:
        if isinstance(selected_competition, str): # Ensure selected_competition is treated as a list for filtering
            selected_competition = [selected_competition]
        filtered_df = filtered_df[filtered_df["Competition"].isin(selected_competition)] # Filter dataframe based on selected competition

    summary_df = prepare_summary(filtered_df, role)

    # Rename column label dynamically
    summary_df.rename(columns={'Name': role}, inplace=True)
    columns = [{'name': col, 'id': col} for col in summary_df.columns]

    return summary_df.to_dict('records'), columns
