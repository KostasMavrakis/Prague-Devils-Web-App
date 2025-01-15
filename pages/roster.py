import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import dash
from dash import html, dcc, dash_table, Input, Output, callback
import requests
import dash_bootstrap_components as dbc

# Initialize the Dash app
dash.register_page(__name__, path='/roster', name="Roster")

# Set up the Google Sheets API client
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Add the path to your 'credentials.json' file
creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\Kostas Mavrakis\\Downloads\\Prague Devils Web App\\assets\\credentials.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet by name or URL
sheet = client.open('Prague Devils 2018-2024')  

# Select the worksheet by name
worksheet = sheet.worksheet("All Players")

# Fetch the data from the worksheet
data = worksheet.get_all_records()

df = pd.DataFrame(data)

# Handle decimal separator conversion
df['Goals Scored per Match'] = df['Goals Scored per Match'].astype(str).str.replace(",", ".").astype(float)/100
df['Goals Conceded per Match'] = df['Goals Conceded per Match'].astype(str).str.replace(",", ".").astype(float)/100
df['Assists per Match'] = df['Assists per Match'].astype(str).str.replace(",", ".").astype(float)/100
df['Weighted Score per Match'] = df['Weighted Score per Match'].astype(str).str.replace(",", ".").astype(float)/100

# Add a new column with HTML to display images in the DataTable
df["Flag"] = df["Flag"].apply(
    lambda url: f'<img src="{url}" style="width: 40px; height: 30px;">'
)

# App layout
layout = dbc.Container([
    
    # Filters for Season and Field Position
    dbc.Row([
        dbc.Col(
            dcc.Dropdown(
            id="season-filter",
            options=[{'label': season, 'value': season} for season in sorted(df['Season'].unique())],
            placeholder="Season",
            value="2024 - 2025",
            multi=True,
            style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "50%",
                    },
            ),
            ),
        dbc.Col(
            dcc.Dropdown(
            id="position-filter",
            options=['Goalkeepers','Defenders','Midfielders','Forwards','Coaches'],
            placeholder="Position",
            multi=True,
            style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "50%",
                    },
            ),
            ),
        dbc.Col(
            dcc.Dropdown(
            id="name-filter",
            options=[{'label': name, 'value': name} for name in sorted(df['Player Name'].unique())],
            placeholder="Player",
            multi=True,
            style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "50%",
                    },
            ),
            ),
        dbc.Col(
            dcc.Dropdown(
            id="flag-filter",
            options=[{'label': country, 'value': country} for country in sorted(df['Country of Origin'].unique())],
            multi=True,
            placeholder="Country",
            style={"margin-bottom": "20px", 
                    "background-color": "transparent",
                    "color": "black",
                    "font-weight": "bold",
                    "width": "50%",
                    },
            ),
            ),
        ], style={'display': 'flex', 'flex-direction': 'column', 'gap': '8px', 'margin-bottom': '20px'}),

    # Toggle between different metrics for Goals, Assists, and Goals Conceded
    dbc.Row([
        # Metric toggles
        dbc.Col(
            dcc.RadioItems(
            id='metric-toggle',
            options=[
                {'label': 'Total Goals Scored', 'value': 'Goals Scored'},
                {'label': 'Goals Scored per Match', 'value': 'Goals Scored per Match'}
            ],
            value='Goals Scored',
            labelStyle={'display': 'inline-block', 'margin-right': '15px'}
            ),
            ),
        dbc.Col(
            dcc.RadioItems(
            id='assists-toggle',
            options=[
                {'label': 'Total Assists', 'value': 'Assists'},
                {'label': 'Assists per Match', 'value': 'Assists per Match'}
            ],
            value='Assists',
            labelStyle={'display': 'inline-block', 'margin-right': '15px'}
        ),
        ),
        dbc.Col(
            dcc.RadioItems(
            id='conceded-toggle',
            options=[
                {'label': 'Total Goals Conceded', 'value': 'Goals Conceded'},
                {'label': 'Goals Conceded per Match', 'value': 'Goals Conceded per Match'}
            ],
            value='Goals Conceded',
            labelStyle={'display': 'inline-block', 'margin-right': '15px'}
        ),
        )
    ], style={'textAlign': 'center', 'margin': '20px'}),
    
    # Data table
    dbc.Row([
        dbc.Col(
            dash_table.DataTable(
        id='table',
        columns=[
            {'name': '#', 'id': 'Index', 'type': 'numeric', "selectable": True, "hideable": True},
            {'name': 'Player Name', 'id': 'Player Name', 'type': 'text', "selectable": True, "hideable": True},
            {'name': 'Season', 'id': 'Season', 'type': 'text', "selectable": True, "hideable": True},
            {'name': 'Main Position', 'id': 'Main Position', 'type': 'text', "selectable": True, "hideable": True},
            {'name': 'Country of Origin', 'id': 'Country of Origin', 'type': 'text', "selectable": True, "hideable": True},
            {'name': '', 'id': 'Flag', 'presentation': 'markdown'},
            {'name': 'Appearences', 'id': 'Appearences', 'type': 'numeric', "selectable": True, "hideable": True},
            {'name': 'Scored Goals', 'id': 'Scored Goals', 'type': 'numeric', "selectable": True, "hideable": True},
            {'name': 'Conceded Goals', 'id': 'Conceded Goals', 'type': 'numeric', "selectable": True, "hideable": True},
            {'name': 'Assists', 'id': 'Assists', 'type': 'numeric', "selectable": True, "hideable": True},
            {'name': 'Weighted Score per Match', 'id': 'Weighted Score per Match', 'type': 'numeric', "selectable": True, "hideable": True}
        ],
        data=[],
        sort_action="native",       # enables data to be sorted per-column by user or not ('none')
        sort_mode="single",         # sort across 'multi' or 'single' columns
        column_selectable="multi",  # allow users to select 'multi' or 'single' columns
        style_data={
            'backgroundColor': 'transparent',
            'color': 'white',
            'color:hover': 'transparent',
            'border': '1px solid white',
            'textAlign': 'center'
        },
        style_header={
            'backgroundColor': 'transparent',
            'color': 'white',
            'fontWeight': 'bold',
            'border': '1.5px solid white',
            'textAlign': 'center',
            'grid-column': '1 / span 2'  # Spans both columns
        },     
        style_table={
            'overflowX': 'auto',
             'grid-template-columns': '1fr 0.2fr'  # Adjusts the width ratio of the columns
        },
        markdown_options={"html": True},  # Enable HTML for rendering images
        

        tooltip_delay=0, # 1000
        tooltip_duration=4000, # 2000
        
        tooltip={
        'Country of Origin': 'Catalonia and the Basque Country are considered as separate nations, as we respect our Teammates who come from there.',
        'Weighted Score per Match': 'Average points collected per match played. Victories are weighted with 3, draws with 1 and defeats with 0.',
        'type': 'markdown',
        'use_with': 'both',  # both refers to header & data cell
                 },

    )
        )
    ])     
],
fluid=True,
)

# Callback to update the table based on the filters
@callback(
    Output('table', 'data'),
    [Input('season-filter', 'value'),
    Input('position-filter', 'value'),
    Input('name-filter', 'value'), 
    Input('flag-filter', 'value'),
    Input('metric-toggle', 'value'),
    Input('assists-toggle', 'value'),
    Input('conceded-toggle', 'value')]
)
def update_table(season_filter, position_filter, name_filter, selected_flags, goals_filter, assists_filter, conceded_filter):
    filtered_df = df.copy()

    # Apply filters for Season, Field Position, Player Name and Country
    if season_filter:
        if isinstance(season_filter, str): # Ensure selected_seasons is treated as a list for filtering
            season_filter = [season_filter]
        filtered_df = filtered_df[filtered_df["Season"].isin(season_filter)] # Filter dataframe based on selected seasons

    if position_filter:
        if isinstance(position_filter, str):
            position_filter = [position_filter]
        filtered_df = filtered_df[filtered_df["Field Position"].isin(position_filter)]

    if name_filter:
        if isinstance(name_filter, str):
            name_filter = [name_filter]
        filtered_df = filtered_df[filtered_df["Player Name"].isin(name_filter)]

    if selected_flags:
        if isinstance(selected_flags, str):
            selected_flags = [selected_flags]
        filtered_df = filtered_df[filtered_df["Country of Origin"].isin(selected_flags)]

    # Select columns based on toggles
    filtered_df = filtered_df.rename(columns={
        goals_filter: 'Scored Goals',
        assists_filter: 'Assists',
        conceded_filter: 'Conceded Goals'
    })
    
     # Add an Index column starting from 1
    filtered_df = filtered_df.reset_index(drop=True)
    filtered_df["Index"] = range(1, len(filtered_df) + 1)

    # Define visible columns and return data
    columns = ['Index', 'Player Name', 'Season', 'Country of Origin', 'Flag', 'Main Position', 'Appearences', 'Scored Goals', 'Conceded Goals', 'Assists', 'Weighted Score per Match']

    return filtered_df[columns].to_dict('records')
