import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import dash
from dash import html, dcc, dash_table, Input, Output, callback
import requests

# Initialize the Dash app
dash.register_page(__name__, path='/results', name="Results")

# Set up the Google Sheets API client
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Add the path to your 'credentials.json' file
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet by name or URL
sheet = client.open('Prague Devils 2018-2024')  

# Select the worksheet by name
worksheet = sheet.worksheet("All Time Results")

# Fetch the data from the worksheet
data = worksheet.get_all_records()

df = pd.DataFrame(data)

# Add a new column with HTML to display images in the DataTable
df["Logo"] = df["Logo"].apply(
    lambda url: f'<img src="{url}" style="width: 32px; height: 32px;">'
)

# App layout
layout = html.Div([
    
    # Filters for Season, Competition, Opponent, Outcome, Coach and Pitch
    html.Div([
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
        dcc.Dropdown(
            id="competition-filter",
            options=['League','Cup','Friendly', 'Post-Corona Tournament 2020'],
            placeholder="Competition",
            multi=True,
            style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "50%",
                    },
        ),
        dcc.Dropdown(
            id="opponent-filter",
            options=[{'label': opponent, 'value': opponent} for opponent in sorted(df['Opponent'].dropna().unique()) if opponent!= ""],
            placeholder="Opponent",
            multi=True,
            style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "50%",
                    },
        ),
        dcc.Dropdown(
            id="outcome-filter",
            options=['Win','Draw','Loss'],
            placeholder="Outcome",
            multi=True,
            style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "50%",
                    },
        ),
        dcc.Dropdown(
            id="coach-filter",
            options=[{'label': coach, 'value': coach} for coach in sorted(df['Coach'].dropna().unique()) if coach != ""],
            placeholder="Coach",
            multi=True,
            style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "50%",
                    },
        ),
        dcc.Dropdown(
            id="pitch-filter",
            options=[{'label': pitch, 'value': pitch} for pitch in sorted(df['Pitch'].dropna().unique()) if pitch != ""],
            placeholder="Pitch",
            multi=True,
            style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "50%",
                    },
        )
    ], style={'display': 'flex', 'flex-direction': 'column', 'gap': '8px', 'margin-bottom': '20px'}),
    
    # Data table
    dash_table.DataTable(
        id='results',
        columns=[
            {'name': '#', 'id': 'Index', 'type': 'numeric', "selectable": True, "hideable": True},
            {'name': 'Season', 'id': 'Season', 'type': 'text', "selectable": True, "hideable": True},
            {'name': 'Competition', 'id': 'Competition', 'type': 'text', "selectable": True, "hideable": True},
            {'name': 'Date', 'id': 'Date', 'type': 'datetime', "selectable": True, "hideable": True},
            {'name': 'Opponent', 'id': 'Opponent', 'type': 'text', "selectable": True, "hideable": True},
            {'name': '', 'id': 'Logo', 'presentation': 'markdown'},
            {'name': 'Score', 'id': 'Score', 'type': 'text', "selectable": True, "hideable": True},
            {'name': 'Goals Scored', 'id': 'Goals Scored', 'type': 'numeric', "selectable": True, "hideable": True},
            {'name': 'Goals Conceded', 'id': 'Goals Conceded', 'type': 'numeric', "selectable": True, "hideable": True},
            {'name': 'Outcome', 'id': 'Outcome', 'type': 'text', "selectable": True, "hideable": True},
            {'name': 'Coach', 'id': 'Coach', 'type': 'text', "selectable": True, "hideable": True},
            {'name': 'Pitch', 'id': 'Pitch', 'type': 'text', "selectable": True, "hideable": True},
            {'name': 'Squad', 'id': 'Squad', 'type': 'text', "selectable": True, "hideable": True}
        ],
        data=[],
        sort_action="native",       # enables data to be sorted per-column by user or not ('none')
        sort_mode="single",         # sort across 'multi' or 'single' columns
        column_selectable="multi",  # allow users to select 'multi' or 'single' columns
        style_data={
            'backgroundColor': 'transparent',
            'color': 'white',
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
    )
    
])

# Callback to update the table based on the filters
@callback(
    Output('results', 'data'),
    [Input('season-filter', 'value'),
    Input('competition-filter', 'value'),
    Input('opponent-filter', 'value'), 
    Input('outcome-filter', 'value'),
    Input('coach-filter', 'value'),
    Input('pitch-filter', 'value')]
)
def update_results(season_filter, competition_filter, opponent_filter, outcome_filter, coach_filter, pitch_filter):
    filtered_df = df.copy()

    # Apply filters for Season, Competition, Opponent, Outcome, Coach and Pitch
    if season_filter:
        if isinstance(season_filter, str): # Ensure selected_seasons is treated as a list for filtering
            season_filter = [season_filter]
        filtered_df = filtered_df[filtered_df["Season"].isin(season_filter)] # Filter dataframe based on selected seasons

    if competition_filter:
        if isinstance(competition_filter, str):
            competition_filter = [competition_filter]
        filtered_df = filtered_df[filtered_df["Competition"].isin(competition_filter)]

    if opponent_filter:
        if isinstance(opponent_filter, str):
            opponent_filter = [opponent_filter]
        filtered_df = filtered_df[filtered_df["Opponent"].isin(opponent_filter)]
    
    if outcome_filter:
        if isinstance(outcome_filter, str):
            outcome_filter = [outcome_filter]
        filtered_df = filtered_df[filtered_df["Outcome"].isin(outcome_filter)]

    if coach_filter:
        if isinstance(coach_filter, str):
            coach_filter = [coach_filter]
        filtered_df = filtered_df[filtered_df["Coach"].isin(coach_filter)]

    if pitch_filter:
        if isinstance(pitch_filter, str):
            pitch_filter = [pitch_filter]
        filtered_df = filtered_df[filtered_df["Pitch"].isin(pitch_filter)]

     # Add an Index column starting from 1
    filtered_df = filtered_df.reset_index(drop=True)
    filtered_df["Index"] = range(1, len(filtered_df) + 1)
    
    # Define visible columns and return data
    columns = ['Index', 'Season', 'Competition', 'Date', 'Opponent', 'Logo', 'Score', 'Goals Scored', 'Goals Conceded', 'Outcome', 'Coach', 'Pitch', 'Squad']

    return filtered_df[columns].to_dict('records')
