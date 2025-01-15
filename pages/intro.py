import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

# Initialize the Dash app
dash.register_page(__name__, path='/')
                
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Carousel(
                                items=[
                    {"key": "1", "src": "/assets/2024-2025.jpg", "header": "Prague Devils", "caption": "2024 - 2025"},
                    {"key": "2", "src": "/assets/2023-2024.jpg", "header": "Prague Devils", "caption": "2023 - 2024"},
                    {"key": "3", "src": "/assets/2022-2023.jpg", "header": "Prague Devils", "caption": "2022 - 2023"},
                    {"key": "4", "src": "/assets/2021-2022.jpg", "header": "Prague Devils", "caption": "2021 - 2022"},
                    {"key": "5", "src": "/assets/2019-2020.jpg", "header": "Prague Devils", "caption": "2019 - 2020"},
                    {"key": "6", "src": "/assets/2018-2019.jpg", "header": "Prague Devils", "caption": "2018 - 2019"},
                    ],
                    controls=True,
                    indicators=True,
                    interval=2500,
                    ride="carousel",
                    className="carousel-fade",
                    style={"width": "60%", "margin": "0 auto", "padding": "20px"},
            )
        ])
    ])
])
  