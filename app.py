import dash
from dash import html, page_registry, page_container
import dash_bootstrap_components as dbc
LOGO = "https://pibfal.com/wp-content/uploads/2018/08/Prague-Devils-126x128.png"

# Create the dash app
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SOLAR, '/assets/custom.css'], meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
server = app.server

# Defining the groups
page_groups = {
   "Squad": [
       {"name": "Overview", "path": "/overview"},
       {"name": "Roster", "path": "/roster"},
       {"name": "Map", "path": "/map"},
       {"name": "Coaches & Captains", "path": "/c&c"},
   ],
   "Results": [
       {"name": "All-time Results", "path": "/results"},
       {"name": "Goals", "path": "/goals"},
       {"name": "Fields", "path": "/fields"},
   ],
   "Performance Stats": [
       {"name": "The Top", "path": "/top"},
       {"name": "Trackers", "path": "/performance"},
       {"name": "Ratings", "path": "/ratings"},
   ],
   "Statistical Analysis": [
       {"name": "Correlation", "path": "/correlation"},
   ]
}

# Building dropdown menus for Navbar
dropdowns = []
for group, pages in page_groups.items():
   dropdowns.append(
       dbc.DropdownMenu(
           label=group,
           nav=True,
           in_navbar=True,
           children=[
               dbc.DropdownMenuItem(page["name"], href=page["path"])
               for page in pages
           ],
       )
   )

# Defining the navigation bar
navbar = dbc.Navbar(
   dbc.Container(
       [
           # Left side: logo + brand
           html.A(
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
           # Right side: navigation items
           dbc.Nav(
               [dbc.NavItem(dbc.NavLink("Gallery", href="/", active="exact"))] + dropdowns,
               className="ms-auto",  # pushes to the right
               navbar=True,
           ),
       ]
   ),
   color="dark",
   dark=True,
   sticky="top",
)
footer = dbc.Container(
   dbc.Row(
       [
           dbc.Col(
               children=[
               # Spacer above the footer
           html.Div(style={"height": "50px"}),  # Adjusts the height as needed
           # Logo and Text
           html.Div(
               children=[
                   # Web Image (via URL)
                   html.Img(
                       src=LOGO,  
                       alt="Club Logo",
                       style={
                           "height": "50px",  # Adjusts the size of the image
                           "marginRight": "10px"  # Space between image and text
                       }
                   ),
                   # Text Field
                   html.Span(
                       "Prague Devils FC",
                       style={
                           "fontSize": "28px",  # Adjusts the font size
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
                       href="https://www.facebook.com/PragueDevilsFC", 
                       target="_blank",
                       children=[
                           html.Img(
                               src="/assets/facebook.png",  # Path to Facebook logo in the assets folder
                               alt="Facebook Logo",
                               style={
                                   "height": "30px",
                                   "width": "30px",
                                   "marginRight": "15px",  # Space between Facebook and Instagram icons
                                   "marginLeft": "60px",  # Adds space before the Facebook icon
                               }
                           )
                       ],
                       style={"textDecoration": "none"}  # Removes underline from the link
                   ),
                   # Instagram Icon
                   html.A(
                       href="https://www.instagram.com/praguedevilsfc/",
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
   navbar,  # Includes the navigation bar
   dash.page_container,
   footer,  # Includes the footer
])

# Run the dash app
if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=8080)
    
