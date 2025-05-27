import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.cloud import secretmanager
import pandas as pd
import dash
from dash import dcc, html, Input, Output, State, callback
import plotly.graph_objs as go
import numpy as np
import dash_bootstrap_components as dbc

# Initialize the Dash app
dash.register_page(__name__, path='/correlation', name="Correlation")

# Function to access credentials from Secret Manager
def get_gspread_client_from_secret(secret_id, project_id, scopes):
    
    # Create the Secret Manager client
    client = secretmanager.SecretManagerServiceClient()

    name = f"projects/{project_id}/secrets/{secret_id}/versions/latest"
    
    # Access the secret version
    response = client.access_secret_version(name=name)
    secret_payload = response.payload.data.decode("UTF-8")
    
    # Load JSON credentials from secret and authorize
    creds_dict = json.loads(secret_payload)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scopes)
    return gspread.authorize(creds)

# Set up the Google Sheets API client
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
project_id = "prague-devils-412311"
secret_id = "GOOGLE_SHEETS_CREDS"

# Now use this client:
gspread_client = get_gspread_client_from_secret(secret_id, project_id, scope)

# Open the Google Sheet by name or URL
sheet = gspread_client.open('Prague Devils 2018-2024')  

# Select the worksheet by name
worksheet = sheet.worksheet("Chart Preparation 2023-2024")

# Fetch the data and convert it to DataFrame
data = worksheet.get_all_records()

# Convert data to pandas DataFrame
df = pd.DataFrame(data)

# Convert values with comma as decimal separator to floats
for column in ["X: Weighted Average per Match", "Y: Average Age", "Y: Percentage of Italians in the Team"]:
    df[column] = df[column].astype(str).str.replace(',', '.').astype(float)/100

layout = dbc.Container([
    dbc.Row([
            dbc.Col([
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
                                "width": "100%",
                            },
                )
            ], xs=10, sm=8, md=3, lg=3, xl=3)
        ], className="mb-3"),

        dbc.Row([
            dbc.Col([
                dcc.Graph(id="line-chart", config={"responsive": True}, style={"height": "100%", "width": "100%"})
            ], xs=12, sm=12, md=6, lg=6, xl=6, style={'marginBottom': '60px'})
        ]),

        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Correlation Coefficient", style={"fontSize": "30px", "fontWeight": "bold", "margin-right": "10px"}, className="card-title"),
                        html.P(id="correlation-coefficient", className="card-text"),
                    ]),                    
                ], 
                className="mb-4",
                style={
                    "backgroundColor": "transparent",
                    "border": "1px solid white",
                    "borderRadius": "10px",
                    "padding": "20px",
                    "textAlign": "center",
                    "margin-top": "10px",
                    "color": "white",
                    "fontWeight": "bold",
                    "fontSize": "30px",
                    "position": "relative",
                    "height": "240px",
                    "width": "240px"},                
                ),
                dbc.Tooltip(
                            id="correlation-tooltip",
                            target="correlation-coefficient",
                            className="custom-tooltip",
                        ),
            ], 
            xs=12, sm=12, md=3, lg=3, xl=3,
            style={"display": "flex", "alignItems": "center", "justifyContent": "center"},
            ),
        ]),

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
        autosize=True,
        height=None,  # Let container decide
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
            orientation="h",       # Horizontal layout
            yanchor="bottom",
            y=1.1,                 # Position above the chart (higher = further up)
            xanchor="center",
            x=0.5,                 # Centered horizontally
            font=dict(size=14, color="white", family="Arial"),
            bgcolor="rgba(0,0,0,0)"
        )
    )

    return f"{correlation:.2f}", tooltip_text, fig
