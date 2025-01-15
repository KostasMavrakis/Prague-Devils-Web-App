import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import dash
from dash import dcc, html, Input, Output, State, callback
import plotly.graph_objs as go
import numpy as np
import dash_bootstrap_components as dbc

# Initialize the Dash app
dash.register_page(__name__, path='/correlation', name="Correlation")

# Set up the Google Sheets API client
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Add the path to your 'credentials.json' file
creds = ServiceAccountCredentials.from_json_keyfile_name("C:\\Users\\Kostas Mavrakis\\Downloads\\Prague Devils\\prague-devils-412311-a8a26089aa1a.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet by name or URL
sheet = client.open('Prague Devils 2018-2024')  

# Select the worksheet by name
worksheet = sheet.worksheet("Chart Preparation 2023-2024")

# Fetch the data from the worksheet
data = worksheet.get_all_records()

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Convert values with comma as decimal separator to floats
for column in ["X: Weighted Average per Match", "Y: Average Age", "Y: Percentage of Italians in the Team"]:
    df[column] = df[column].astype(str).str.replace(',', '.').astype(float)/100

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Dropdown(
                            id="y-axis-dropdown",
                            options=[
                                {"label": "Average Age", "value": "Y: Average Age"},
                                {"label": "Percentage of Italians", "value": "Y: Percentage of Italians in the Team"},
                            ],
                            value="Y: Average Age",
                            clearable=False,
                            style={
                                "background-color": "transparent",
                                "color": "black",
                                "font-weight": "bold",
                                "width": "50%",
                            },
                        ),
                        dcc.Graph(id="line-chart", style={"height": "450px"}),
                        # style={"display": "inline-block", "verticalAlign": "top"},
                    ],
                    xs=10, sm=8, md=8, lg=6, xl=5,  # 85% of the page
                ),
                dbc.Col(
                    [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4("Correlation Coefficient", className="card-title"),
                                    html.P(id="correlation-coefficient", className="card-text"),
                                ]
                            ),
                            className="mb-3",
                            style={
                                "backgroundColor": "transparent",
                                "border": "1px solid white",
                                "borderRadius": "10px",
                                "padding": "20px",
                                "margin": "0 10px",
                                "textAlign": "center",
                                "color": "white",
                                "fontSize": "30px",
                                "fontWeight": "bold",
                                "position": "relative",
                                "height": "240px",
                                "width": "260px",
                            },
                        ),
                        dbc.Tooltip(
                            id="correlation-tooltip",
                            target="correlation-coefficient",
                            className="custom-tooltip",
                        ),
                    ],
                    xs=10, sm=5, md=2, lg=6, xl=5,  # 15% of the page
                    style={"display": "flex", "alignItems": "center", "justifyContent": "center"},
                ),
            ]
        )
    ],
    fluid=True,
    className="mt-5",
)

# Callbacks
@callback(
    [Output("correlation-coefficient", "children"),
     Output("correlation-tooltip", "children"),
     Output("line-chart", "figure")],
    [Input("y-axis-dropdown", "value")],
)
def update_components(y_column):
    # Correlation calculation
    x_values = df["X: Weighted Average per Match"]
    y_values = df[y_column]
    correlation = np.corrcoef(x_values, y_values)[0, 1]

    # Tooltip text
    if y_column == "Y: Average Age":
        tooltip_text = (
            "The age and the performance of the Team have a negative correlation. "
            "As the Team is getting older, we notice that our results are getting worse."
        )
    elif y_column == "Y: Percentage of Italians in the Team":
        tooltip_text = (
            "The percentage of Italians in the Team and the weighted score per match "
            "have a positive correlation. In other words, a larger number of Italians in the Team "
            "means better results."
        )
    else:
        tooltip_text = ""

    # Create line chart
    fig = go.Figure()

    # Line for "X: Weighted Average per Match"
    fig.add_trace(
        go.Scatter(
            x=df["Season"],
            y=df["X: Weighted Average per Match"],
            mode="lines+markers+text",
            name="X: Weighted Average per Match",
            line=dict(color="rgb(0, 123, 164)", width=2),
            text=df["X: Weighted Average per Match"],
            textposition="top center",
            textfont=dict(color="white", size=14, family="Arial")
        )
    )

    # Line for selected Y-axis variable
    fig.add_trace(
        go.Scatter(
            x=df["Season"],
            y=df[y_column],
            mode="lines+markers+text",
            name=y_column,
            line=dict(color="rgb(228, 155, 88)", width=2),
            text=df[y_column],
            textposition="top center",
            textfont=dict(color="white", size=14, family="Arial")
        )
    )

    # Update layout to remove outer border lines and y-axis
    fig.update_layout(
        hovermode=False,  # Disable hover tooltip
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(
            showline=False,
            showgrid=False,
            tickmode="array",
            tickvals=df["Season"],
            ticktext=df["Season"],  # Display season labels
            tickfont=dict(color="white", size=14, family="Arial")
        ),
        yaxis=dict(
            showline=False,
            showgrid=False,
            visible=False  # Hides y-axis
        ),
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=True,
        legend=dict(
            font=dict(size=14, color="white", family="Arial"),
            bgcolor="rgba(0,0,0,0)"
        )
    )

    return f"{correlation:.2f}", tooltip_text, fig
