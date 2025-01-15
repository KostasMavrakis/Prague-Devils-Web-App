import gspread
from oauth2client.service_account import ServiceAccountCredentials
import dash
from dash import dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Initialize the Dash app
dash.register_page(__name__, path='/overview', name="Overview")

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

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Convert "Age" from comma-separated to dot-separated floats
df['Age'] = df['Age'].astype(str).str.replace(",", ".").astype(float)/100

# App layout
layout = dbc.Container(
    fluid=True,
    children=[
        # Header Drop-down filter
        dbc.Row(
            dbc.Col(
                dcc.Dropdown(
                    id="season-filter",
                    options=[{"label": season, "value": season} for season in sorted(df["Season"].unique())],
                    placeholder="Season",
                    value="2024 - 2025",
                    style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "50%",
                        },
                ),
                width=12,
            ),
            className="mb-4",
        ),
        # Main Content: Pie chart and cards
        dbc.Row(
            [
                # Pie Chart Column
                dbc.Col(
                    dcc.Graph(
                        id="pie-chart",
                        style={"width": "65%", "display": "inline-block"},
                    ),
                    xs=10, sm=8, md=8, lg=6, xl=5,  # 85% of the page
                ),
                # Cards Column
                dbc.Col(
                    html.Div(
                        [
                            # First row of cards (2 cards side by side)
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.Card(
                                            dbc.CardBody(
                                                id="total-players-card",
                                                style={
                                                    "background-color": "transparent",
                                                    "border": "1px solid white",
                                                    "padding": "20px",
                                                    "border-radius": "5px",
                                                    "text-align": "center",
                                                    "color": "white",
                                                    "font-size": "30px",
                                                    "font-weight": "bold",
                                                    "height": "240px",  
                                                    "width": "260px",
                                                    "margin": "auto",
                                                    "display": "flex",  # Added for vertical alignment
                                                    "align-items": "center",  # Center vertically
                                                    "justify-content": "center",  # Center horizontally
                                                    },
                                            ),
                                            className="h-100",
                                        ),
                                        xs=10, sm=8, md=8, lg=6, xl=5,  # 50% of the card column
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                            dbc.CardBody(
                                                id="distinct-countries-card",
                                                style={
                                                    "background-color": "transparent",
                                                    "border": "1px solid white",
                                                    "padding": "20px",
                                                    "border-radius": "5px",
                                                    "text-align": "center",
                                                    "color": "white",
                                                    "font-size": "30px",
                                                    "font-weight": "bold",
                                                    "height": "240px",  
                                                    "width": "260px",
                                                    "margin": "auto",
                                                    "display": "flex",  # Added for vertical alignment
                                                    "align-items": "center",  # Center vertically
                                                    "justify-content": "center",  # Center horizontally
                                                },
                                            ),
                                            className="h-100",
                                        ),
                                        xs=10, sm=8, md=8, lg=5, xl=5,  # 50% of the card column
                                    ),
                                ],
                                className="mb-2",
                                justify="center",  # Align cards in the row
                            ),
                            # Second row of cards (third card below)
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.Card(
                                            dbc.CardBody(
                                                id="average-age-card",
                                                style={
                                                    "background-color": "transparent",
                                                    "border": "1px solid white",
                                                    "padding": "20px",
                                                    "border-radius": "5px",
                                                    "text-align": "center",
                                                    "color": "white",
                                                    "font-size": "30px",
                                                    "font-weight": "bold",
                                                    "height": "240px",  
                                                    "width": "260px",
                                                    "margin": "auto",
                                                    "display": "flex",  # Added for vertical alignment
                                                    "align-items": "center",  # Center vertically
                                                    "justify-content": "center",  # Center horizontally
                                                    },
                                            ),
                                            className="h-100",
                                        ),
                                        xs=10, sm=5, md=5, lg=5, xl=5,  # 50% of the card column
                                        style={"padding-left": "5px", "padding-right": "5px"},  # Reduced horizontal gap
                                        className="card-column",  # Add this class
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                            dbc.CardBody(
                                                id="field-position-card",
                                                style={
                                                    "background-color": "transparent",
                                                    "border": "1px solid white",
                                                    "padding": "20px",
                                                    "border-radius": "5px",
                                                    "text-align": "center",
                                                    "color": "white",
                                                    "font-size": "30px",
                                                    "font-weight": "bold",
                                                    "height": "240px",  
                                                    "width": "260px",
                                                    "margin": "auto",
                                                    "display": "flex",  # Added for vertical alignment
                                                    "align-items": "center",  # Center vertically
                                                    "justify-content": "center",  # Center horizontally
                                                },
                                            ),
                                            className="h-100",
                                        ),
                                        xs=10, sm=5, md=5, lg=5, xl=5,  # 50% of the card column
                                        style={"padding-left": "5px", "padding-right": "5px"},  # Reduced horizontal gap
                                        className="card-column",  # Add this class
                                    ),
                                ],
                                className="mb-2",
                                justify="center",  # Align cards in the row
                            ),
                        ]
                    ),
                    xs=10, sm=5, md=5, lg=5, xl=5,  # 15% of the page
                ),
            ],
            className="align-items-center",  # Vertical alignment
        ),
    ],
    style={"backgroundColor": "transparent", "color": "white", "padding": "20px"},
)

# Callback to update the pie chart and cards
@callback(
    [
        Output("pie-chart", "figure"),
        Output("total-players-card", "children"),
        Output("distinct-countries-card", "children"),
        Output("average-age-card", "children"),
        Output("field-position-card", "children"),
    ],
    [Input("season-filter", "value")],
)
def update_dashboard(selected_season):
    # Filter data based on selected season
    if selected_season:
        filtered_df = df[df["Season"] == selected_season]
    else:
        filtered_df = df

    # Pie chart data
    pie_data = filtered_df["Country of Origin"].value_counts().reset_index()
    pie_data.columns = ["Country of Origin", "Count"]

    # Pie chart
    fig = px.pie(
        pie_data,
        names="Country of Origin",
        values="Count",
        color_discrete_sequence=px.colors.sequential.RdBu,
    )
    fig.update_traces(
        textinfo="percent+label",  # Show percentages inside, labels outside
        textposition="inside",
        hoverinfo="label+percent",
        hovertemplate=(
            '<span style="color: black; font-size: 14px; fontWeight: bold; ">%{label}</span><br>'
            "<b>Number of Players: </b> %{value}<extra></extra>"
        ),
    )
    fig.update_layout(
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        title=dict(font=dict(size=18), x=0.5),
        hoverlabel=dict(
            bgcolor="white",
            font=dict(color="black", family="Arial"),
            bordercolor="lightgray"
        ),
        height=700,  # Increase height for larger pie chart
        width=700,   # Increase width for larger pie chart
    )
    fig.update_traces(
        textfont=dict(
            size=18,  # Increased font size for labels
            family="Arial",
            color="#4c4b4b",
            weight="bold"  # Make labels bold
        )
    )

    # Cards
    total_players = filtered_df["Player Name"].count()
    distinct_countries = filtered_df["Country of Origin"].nunique()
    avg_age = filtered_df.loc[filtered_df["Appearences"] > 0, "Age"].mean()
    field_positions = ["Goalkeepers", "Defenders", "Midfielders", "Forwards"]
    field_position_counts = {
        position: filtered_df["Field Position"].value_counts().get(position, 0) for position in field_positions
    }
    field_position_card_content = "\n".join([f"{pos} {count}" for pos, count in field_position_counts.items()])

    total_players_card = f"Number of Players:\n{total_players}"
    distinct_countries_card = f"Nationalities:\n{distinct_countries}"
    avg_age_card = f"Average Age\n{avg_age:.1f} years"
    field_position_card = field_position_card_content

    return fig, total_players_card, distinct_countries_card, avg_age_card, field_position_card
