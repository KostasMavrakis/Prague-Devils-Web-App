import gspread
from oauth2client.service_account import ServiceAccountCredentials
import dash
from dash import html, dcc, page_registry, page_container
import dash_bootstrap_components as dbc

LOGO = "https://pibfal.com/wp-content/uploads/2018/08/Prague-Devils-126x128.png"

# Create the dash app
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SOLAR, '/assets/custom.css'])

# Define the navigation bar
navbar = dbc.NavbarSimple(
    children=[
        dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO, height="55px")),
                        dbc.Col(dbc.NavbarBrand("Prague Devils", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="/",
                style={"textDecoration": "none"},
                ),
        ]
                ),
                dbc.NavItem(dbc.NavLink("Gallery", href="/")),
                dbc.NavItem(dbc.NavLink("Roster", href="/roster")),
                dbc.NavItem(dbc.NavLink("Overview", href="/overview")),
                dbc.NavItem(dbc.NavLink("Map", href="/map")),
                dbc.NavItem(dbc.NavLink("Results", href="/results")),
                dbc.NavItem(dbc.NavLink("The_Top", href="/top")),
                dbc.NavItem(dbc.NavLink("Correlation", href="/correlation")),
    ],
        color="dark",
        dark=True,
)

footer = dbc.Container(
    dbc.Row(
        [
            dbc.Col(
                children=[
                # Spacer above the footer
            html.Div(style={"height": "50px"}),  # Adjust the height as needed
            # Logo and Text
            html.Div(
                children=[
                    # Web Image (via URL)
                    html.Img(
                        src=LOGO,  # Replace with your web image URL
                        alt="Club Logo",
                        style={
                            "height": "50px",  # Adjust the size of the image
                            "marginRight": "10px"  # Space between image and text
                        }
                    ),
                    # Text Field
                    html.Span(
                        "Prague Devils FC",
                        style={
                            "fontSize": "28px",  # Adjust the font size
                            "fontWeight": "bold",  # Makes the text bold
                            "verticalAlign": "middle"  # Aligns text with the image
                        }
                    )
                ],
                style={
                    "display": "flex",  # Aligns items horizontally
                    "alignItems": "left",  # Centers items vertically
                    "justifyContent": "left",  # Centers content horizontally
                }
            ),
            # Icons
            html.Div(
                children=[
                    # Facebook Icon
                    html.A(
                        href="https://www.facebook.com/PragueDevilsFC",  # Replace with your Facebook page URL
                        target="_blank",
                        children=[
                            html.Img(
                                src="/assets/facebook.png",  # Path to Facebook logo in the assets folder
                                alt="Facebook Logo",
                                style={
                                    "height": "30px",
                                    "width": "30px",
                                    "marginRight": "15px",  # Space between Facebook and Instagram icons
                                    "marginLeft": "60px",  # Add space before the Facebook icon
                                }
                            )
                        ],
                        style={"textDecoration": "none"}  # Removes underline from the link
                    ),
                    # Instagram Icon
                    html.A(
                        href="https://www.instagram.com/praguedevilsfc/",  # Replace with your Instagram page URL
                        target="_blank",
                        children=[
                            html.Img(
                                src="/assets/instagram.png",  # Path to Instagram logo in the assets folder
                                alt="Instagram Logo",
                                style={
                                    "height": "30px",
                                    "width": "30px",
                                }
                            )
                        ],
                        style={"textDecoration": "none"}  # Removes underline from the link
                    ),
                ]
            ),
        ],
                align="left"),
        ],
        style={
            "marginTop": "50px",  # Additional space between the footer and core components
        }
    ),
    className="footer",
    fluid=True,
)

# Overall layout
app.layout = html.Div([
    navbar,  # Include the navigation bar
    dash.page_container,
    footer,  # Include the footer
])

# Run the dash app
if __name__ == '__main__':
    app.run_server(debug=True)