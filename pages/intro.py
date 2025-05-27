import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

# Initialize the Dash app
dash.register_page(__name__, path='/')
                
carousel = dbc.Carousel(
    items=[
                    {"key": "1", "src": "/assets/photo_1.jpg", "header": "Prague Devils", "caption": "2024 - 2025"},
                    {"key": "2", "src": "/assets/photo_2.jpg", "header": "Prague Devils", "caption": "2023 - 2024"},
                    {"key": "3", "src": "/assets/photo_3.jpg", "header": "Prague Devils", "caption": "2022 - 2023"},
                    {"key": "4", "src": "/assets/photo_4.jpg", "header": "Prague Devils", "caption": "2021 - 2022"},
                    {"key": "5", "src": "/assets/photo_5.jpg", "header": "Prague Devils", "caption": "2019 - 2020"},
                    {"key": "6", "src": "/assets/photo_6.jpg", "header": "Prague Devils", "caption": "2018 - 2019"},
    ],
    controls=True,
    indicators=True,
    interval=2500,
    className="carousel-fade",
    style={"width": "60%", "margin": "0 auto", "padding": "20px"},
)

layout = dbc.Container([
    html.Div(
        carousel,
        style={
            "--bs-carousel-caption-color": "white",
            "--bs-carousel-caption-bg": "rgba(0,0,0,0.5)",
        },
        className="carousel-container"
    )
], fluid=True)
