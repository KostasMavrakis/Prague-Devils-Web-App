import dash
from dash import html
import dash_bootstrap_components as dbc

# Initialize the Dash app
dash.register_page(__name__, path='/')

carousel = dbc.Carousel(
   items=[
                   {"key": "1", "src": "/assets/image1.webp", "header": "Prague Devils", "caption": "2025 - 2026"},
                   {"key": "2", "src": "/assets/image2.webp", "header": "Prague Devils", "caption": "2024 - 2025"},
                   {"key": "3", "src": "/assets/image3.webp", "header": "Prague Devils", "caption": "2023 - 2024"},
                   {"key": "4", "src": "/assets/image4.webp", "header": "Prague Devils", "caption": "2022 - 2023"},
                   {"key": "5", "src": "/assets/image5.webp", "header": "Prague Devils", "caption": "2021 - 2022"},
                   {"key": "6", "src": "/assets/image6.webp", "header": "Prague Devils", "caption": "2019 - 2020"},
                   {"key": "7", "src": "/assets/image7.webp", "header": "Prague Devils", "caption": "2018 - 2019"},
   ],
   controls=True,
   indicators=True,
   interval=2500,
   className="carousel-fade",
   style={"width": "60%", "margin": "0 auto", "padding": "20px"},
)

# Layout of the Dash app
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
