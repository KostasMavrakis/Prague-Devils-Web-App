import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px

# Initialize the Dash app
dash.register_page(__name__, path='/map', name="Map")

# Set up the Google Sheets API client
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Add the path to your 'credentials.json' file
creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\Kostas Mavrakis\\Downloads\\Prague Devils\\prague-devils-412311-a8a26089aa1a.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet by name or URL
sheet = client.open('Prague Devils 2018-2024')  

# Select the worksheet by name
worksheet = sheet.worksheet("All Players")

# Fetch the data and convert it to DataFrame
data = worksheet.get_all_records()
df = pd.DataFrame(data)

# Convert Latitude and Longitude values to float with correct decimal format
df['Latitude'] = df['Latitude'].astype(str).str.replace(",", ".").astype(float)/100
df['Longitude'] = df['Longitude'].astype(str).str.replace(",", ".").astype(float)/100

# Add a new column with HTML to display images in the DataTable
df["Flag"] = df["Flag"].apply(
    lambda url: f'<img src="{url}" style="width: 40px; height: 30px;">'
)

# Layout of the Dash app
layout = html.Div([    
    # Dropdown filters
    html.Div([
        dcc.Dropdown(
            id='season-filter',
            options=[{'label': season, 'value': season} for season in sorted(df['Season'].unique())],
            value="2024 - 2025",
            multi=False,
            placeholder="Season",
            style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "50%",
                    },
        ),
        dcc.Dropdown(
            id='position-filter',
            options=['Goalkeepers','Defenders','Midfielders','Forwards', 'Coaches'],
            multi=True,
            placeholder="Position",
            style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "50%",
                    },
        ),
        dcc.Dropdown(
            id='country-filter',
            options=[{'label': country, 'value': country} for country in sorted(df['Country of Origin'].unique())],
            multi=True,
            placeholder="Country",
            style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "50%",
                    },
        ),
    ], style={'display': 'flex', 'flex-direction': 'column', 'gap': '8px', 'margin-bottom': '20px'}),

    # Map display
    dcc.Graph(id='player-map',
              config={"scrollZoom": True},  # Enable mouse scroll zoom
              )
])

# Callback to update the map
@callback(
    Output('player-map', 'figure'),
    [Input('season-filter', 'value'),
     Input('position-filter', 'value'),
     Input('country-filter', 'value')]
)
def update_map(selected_season, selected_positions, selected_countries):
    # Filter the data based on the inputs
    filtered_df = df.copy()
    if selected_season:
        filtered_df = filtered_df[filtered_df['Season'] == selected_season]
    if selected_positions:
        filtered_df = filtered_df[filtered_df['Field Position'].isin(selected_positions)]
    if selected_countries:
        filtered_df = filtered_df[filtered_df['Country of Origin'].isin(selected_countries)]

    # Create the scatter map
    fig = px.scatter_mapbox(
        filtered_df,
        lat='Latitude',
        lon='Longitude',
        color='Field Position',
        hover_name=None,
        hover_data={
            'Field Position': False,
            'Player Name': False,
            'Country of Origin': True,
            'Main Position': True
            },
        custom_data=["Player Name", "Country of Origin", "Main Position"],
        size_max=30,
        zoom=15,
        template='plotly_dark'
    )

    # Map styling and customization
    fig.update_layout(
        mapbox_style="open-street-map",
        mapbox=dict(center=dict(lat=20, lon=0), zoom=1.5),
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        showlegend=True,
        legend=dict(font=dict(color="white", size=16)),  # White text for the legend
        plot_bgcolor="rgba(0,0,0,0)",  # Transparent background
        paper_bgcolor="rgba(0,0,0,0)"
    )
    
    fig.update_traces(
        marker=dict(
            size=14,
            opacity = 0.7
        )
    )
    
     # Customize tooltips to display flag images
    fig.update_traces(
        hovertemplate=(
            '<span style="color: black; font-size: 16px; fontWeight: bold; ">%{customdata[0]}</span><br>'
            '<span style="color: black; font-size: 14px;">Country: %{customdata[1]}</span><br>'
            '<span style="color: black; font-size: 14px;">Primary Position: %{customdata[2]}</span><extra></extra>'
        )
    )

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
    
    return fig