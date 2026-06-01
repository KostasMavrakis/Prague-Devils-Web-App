import dash
from dash import html, dcc, ALL, ctx, Input, Output, State
import dash_bootstrap_components as dbc
import dash_svg as svg
import flask
from data_loader import load_all_players

# Initialize the Dash app
app = dash.Dash(__name__, external_scripts=["https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"], external_stylesheets=[dbc.themes.SOLAR, '/assets/lineup.css'], suppress_callback_exceptions=True, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])

df = load_all_players()
# --------------------------------------------------
# FORMATIONS
# --------------------------------------------------
FORMATIONS = {
   "4-3-3 (Single Pivot)": [
       ("GK", 5, 50),
       ("LB", 20, 10), ("CB", 14, 35),
       ("CB", 14, 65), ("RB", 20, 90),
       ("CM", 55, 30), ("CDM", 39.5, 50), ("CM", 55, 70),
       ("LW", 68, 10), ("CF", 77, 50), ("RW", 68, 90),
   ],
   "4-3-3 (Double Pivot)": [
       ("GK", 5, 50),
       ("LB", 20, 10), ("CB", 14, 35),
       ("CB", 14, 65), ("RB", 20, 90),
       ("CDM", 39.5, 65), ("CDM", 39.5, 35), ("CAM", 62, 50),
       ("LW", 68, 10), ("CF", 77, 50), ("RW", 68, 90),
   ],
   "4-4-2": [
       ("GK", 5, 50),
       ("LB", 20, 10), ("CB", 14, 35),
       ("CB", 14, 65), ("RB", 20, 90),
       ("LM", 62, 10), ("CM", 39.5, 35),
       ("CM", 39.5, 65), ("RM", 62, 90),
       ("ST", 77, 65), ("ST", 77, 35),
   ],
   "4-4-2 (Diamond)": [
       ("GK", 5, 50),
       ("LB", 20, 10), ("CB", 14, 35),
       ("CB", 14, 65), ("RB", 20, 90),
       ("CDM", 39.5, 50),
       ("LCM", 53, 30), ("RCM", 53, 70),
       ("CAM", 62, 50),
       ("ST", 77, 35), ("ST", 77, 65),
   ],
   "4-4-1-1": [
       ("GK", 5, 50),
       ("LB", 20, 10), ("CB", 14, 35),
       ("CB", 14, 65), ("RB", 20, 90),
       ("LM", 58, 15), ("LCM", 39.5, 35),
       ("RCM", 39.5, 65), ("RM", 58, 85),
       ("CAM", 62, 50),
       ("CF", 77, 50),
   ],
   "4-3-2-1": [
       ("GK", 5, 50),
       ("LB", 20, 10), ("CB", 14, 35),
       ("CB", 14, 65), ("RB", 20, 90),
       ("LCM", 53, 30), ("CDM", 39.5, 50),
       ("RCM", 53, 70),
       ("LAM", 68, 35), ("RAM", 68, 65),
       ("CF", 77, 50),
   ],
   "4-2-3-1": [
       ("GK", 5, 50),
       ("LB", 20, 10), ("CB", 14, 35),
       ("CB", 14, 65), ("RB", 20, 90),
       ("CDM", 39.5, 35), ("CDM", 39.5, 65),
       ("LW", 58, 10), ("CAM", 62, 50), ("RW", 58, 90),
       ("CF", 77, 50),
   ],
   "4-5-1": [
       ("GK", 5, 50),
       ("LB", 20, 10), ("CB", 14, 35),
       ("CB", 14, 65), ("RB", 20, 90),
       ("LM", 62, 10),
       ("LCM", 53, 35), ("CDM", 39.5, 50), ("RCM", 53, 65),
       ("RM", 62, 90),
       ("CF", 77, 50),
   ],
   "3-4-3": [
       ("GK", 5, 50),
       ("LCB", 14, 25), ("CB", 14, 50), ("RCB", 14, 75),
       ("LM", 53, 20), ("LCM", 39.5, 35),
       ("RCM", 39.5, 65), ("RM", 53, 80),
       ("LW", 68, 10), ("CF", 77, 50), ("RW", 68, 90),
   ],
   "3-5-2": [
       ("GK", 5, 50),
       ("LCB", 14, 25), ("CB", 14, 50), ("RCB", 14, 75),
       ("LM", 62, 10),
       ("LCM", 53, 35), ("CDM", 39.5, 50), ("RCM", 53, 65),
       ("RM", 62, 90),
       ("ST", 77, 35), ("ST", 77, 65),
   ],
   "3-6-1": [
       ("GK", 5, 50),
       ("LCB", 14, 25), ("CB", 14, 50), ("RCB", 14, 75),
       ("LM", 62, 10),
       ("LCM", 53, 30), ("CDM", 39.5, 50), ("RCM", 53, 70),
       ("RM", 62, 90),
       ("CAM", 62, 50),
       ("CF", 77, 50),
   ],
   "5-3-2": [
       ("GK", 5, 50),
       ("LWB", 28, 10),
       ("LCB", 14, 30), ("CB", 14, 50), ("RCB", 14, 70),
       ("RWB", 28, 90),
       ("LCM", 53, 30), ("CDM", 39.5, 50), ("RCM", 53, 70),
       ("ST", 77, 35), ("ST", 77, 65),
   ],
   "5-4-1": [
       ("GK", 5, 50),
       ("LWB", 28, 10),
       ("LCB", 14, 30), ("CB", 14, 50), ("RCB", 14, 70),
       ("RWB", 28, 90),
       ("LM", 62, 15), ("LCM", 39.5, 35),
       ("RCM", 39.5, 65), ("RM", 62, 85),
       ("CF", 77, 50),
   ],
}

MOBILE_FORMATIONS = {
    "4-3-3 (Single Pivot)": [
        ("GK", 3, 42),
        ("LB", 18, 4),
        ("CB", 10, 25),
        ("CB", 10, 60),
        ("RB", 18, 80),
        ("CM", 33, 25),
        ("CDM", 20, 42),
        ("CM", 33, 60),
        ("LW", 51, 4),
        ("CF", 57, 42),
        ("RW", 51, 80),
    ],
    "4-3-3 (Double Pivot)": [
        ("GK", 3, 42),
        ("LB", 18, 4),
        ("CB", 10, 25),
        ("CB", 10, 60),
        ("RB", 18, 80),
        ("CDM", 23, 28),
        ("CDM", 23, 56),
        ("CAM", 36, 42),
        ("LW", 51, 4),
        ("CF", 57, 42),
        ("RW", 51, 80),
    ],
    "4-4-2": [
        ("GK", 3, 42),
        ("LB", 18, 4),
        ("CB", 10, 25),
        ("CB", 10, 60),
        ("RB", 18, 80),
        ("LM", 51, 4),
        ("CM", 32, 25),
        ("CM", 32, 60),
        ("RM", 51, 80),
        ("ST", 57, 30),
        ("ST", 57, 54),
    ],
    "4-4-2 (Diamond)": [
        ("GK", 3, 42),
        ("LB", 18, 4),
        ("CB", 10, 25),
        ("CB", 10, 60),
        ("RB", 18, 80),
        ("CDM", 22, 42),
        ("LCM", 38, 20),
        ("RCM", 38, 65),
        ("CAM", 44, 42),
        ("ST", 57, 30),
        ("ST", 57, 54),
    ],
    "4-4-1-1": [
        ("GK", 3, 42),
        ("LB", 18, 4),
        ("CB", 10, 25),
        ("CB", 10, 60),
        ("RB", 18, 80),
        ("LM", 51, 4),
        ("LCM", 30, 25),
        ("RCM", 30, 60),
        ("RM", 51, 80),
        ("CAM", 38, 42),
        ("CF", 57, 42),
    ],
    "4-3-2-1": [
        ("GK", 3, 42),
        ("LB", 18, 4),
        ("CB", 10, 25),
        ("CB", 10, 60),
        ("RB", 18, 80),
        ("LCM", 33, 19),
        ("CDM", 28, 42),
        ("RCM", 33, 66),
        ("LAM", 50, 23),
        ("RAM", 50, 61),
        ("CF", 57, 42),
    ],
    "4-2-3-1": [
        ("GK", 3, 42),
        ("LB", 18, 4),
        ("CB", 10, 25),
        ("CB", 10, 60),
        ("RB", 18, 80),
        ("CDM", 25, 28),
        ("CDM", 25, 56),
        ("LW", 50, 4),
        ("CAM", 38, 42),
        ("RW", 50, 80),
        ("CF", 57, 42),
    ],

    "4-5-1": [
        ("GK", 3, 42),
        ("LB", 18, 4),
        ("CB", 10, 25),
        ("CB", 10, 60),
        ("RB", 18, 80),
        ("LM", 52, 4),
        ("LCM", 39, 25),
        ("CDM", 28, 42),
        ("RCM", 39, 60),
        ("RM", 52, 80),
        ("CF", 57, 42),
    ],
    "3-4-3": [
        ("GK", 3, 42),
        ("LCB", 16, 18),
        ("CB", 16, 42),
        ("RCB", 16, 66),
        ("LM", 38, 10),
        ("LCM", 30, 28),
        ("RCM", 30, 56),
        ("RM", 38, 74),
        ("LW", 50, 4),
        ("CF", 57, 42),
        ("RW", 50, 80),
    ],
    "3-5-2": [
        ("GK", 3, 42),
        ("LCB", 16, 18),
        ("CB", 16, 42),
        ("RCB", 16, 66),
        ("LM", 50, 4),
        ("LCM", 38, 25),
        ("CDM", 30, 42),
        ("RCM", 38, 60),
        ("RM", 50, 80),
        ("ST", 57, 30),
        ("ST", 57, 54),
    ],
    "3-6-1": [
        ("GK", 3, 42),
        ("LCB", 16, 18),
        ("CB", 16, 42),
        ("RCB", 16, 66),
        ("LM", 50, 4),
        ("LCM", 38, 22),
        ("CDM", 30, 42),
        ("RCM", 38, 62),
        ("RM", 50, 80),
        ("CAM", 44, 42),
        ("CF", 57, 42),
    ],
    "5-3-2": [
        ("GK", 3, 42),
        ("LWB", 28, 2),
        ("LCB", 16, 20),
        ("CB", 16, 42),
        ("RCB", 16, 64),
        ("RWB", 28, 82),
        ("LCM", 38, 24),
        ("CDM", 30, 42),
        ("RCM", 38, 60),
        ("ST", 57, 30),
        ("ST", 57, 54),
    ],
    "5-4-1": [
        ("GK", 3, 42),
        ("LWB", 28, 2),
        ("LCB", 16, 20),
        ("CB", 16, 42),
        ("RCB", 16, 64),
        ("RWB", 28, 82),
        ("LM", 50, 4),
        ("LCM", 36, 25),
        ("RCM", 36, 60),
        ("RM", 50, 80),
        ("CF", 57, 42),
    ],
}
# =====================================
# MOBILE FORMATION TRANSFORM
# =====================================
def transform_mobile_coordinate(x, y):

    # Vertical compression
    mobile_x = (x * 0.78) - 1

    # Horizontal compression
    if y < 50:

        mobile_y = (
            42 - ((50 - y) * 0.76)
        )

    else:

        mobile_y = (
            42 + ((y - 50) * 0.76)
        )

    return mobile_x, mobile_y

# --------------------------------------------------
# LAYOUT
# --------------------------------------------------
app.layout = dbc.Container(
   [
       dcc.Store(id="captain-store", data=None),
       dcc.Store(id="formations-store", data=FORMATIONS),
       # Hidden proxy for JS
       html.Div(id="captain-proxy", style={"display": "none"}),
       html.Div(id="formation-proxy", style={"display": "none"}),
# --------------------------------------------------
# Row 1: Dropdowns 
# --------------------------------------------------
       dbc.Row(
           [
               dbc.Col(
                   dcc.Dropdown(
                       id="formation-dropdown",
                       options=[{'label': formation, 'value': formation} for formation in FORMATIONS],
                       value="4-3-3 (Single Pivot)",
                       placeholder="Formation",
                       multi=False,
                       clearable=False,
                       style={
                           "background-color": "transparent",
                           "color": "black",
                           "font-weight": "bold",
                           "width": "75%",
                           },
                   ),
                   xs=12,
                   sm=6,
                   md=4,
                   lg=2,
                   xl=2,
               ),
               dbc.Col(
                   dcc.Dropdown(
                       id="season-dropdown",
                       options=[{"label": "All-time", "value": "ALL"}] + [{'label': season, 'value': season} for season in df['Season'].unique()],
                       value="2025 - 2026",
                       clearable=False,
                       placeholder="Season",
                       multi=False,
                       style={
                           "background-color": "transparent",
                           "color": "black",
                           "font-weight": "bold",
                           "width": "75%",
                           },
                   ),
                   xs=12,
                   sm=6,
                   md=4,
                   lg=2,
                   xl=2,
               ),
               dbc.Col(
                   dcc.Dropdown(
                       id="position-dropdown",
                       options=[{'label': position, 'value': position} for position in df['Field Position'].unique()],
                       placeholder="Position",
                       multi=True,
                       style={
                           "background-color": "transparent",
                           "color": "black",
                           "font-weight": "bold",
                           "width": "75%",
                           },
                   ),
                   xs=12,
                   sm=6,
                   md=4,
                   lg=2,
                   xl=2,
               ),
               dbc.Col(
                   dcc.Dropdown(
                       id="country-dropdown",
                       options=[{'label': country, 'value': country} for country in df['Country of Origin'].unique()],
                       placeholder="Country",
                       multi=True,
                       style={
                           "background-color": "transparent",
                           "color": "black",
                           "font-weight": "bold",
                           "width": "75%",
                           },
                   ),
                   xs=12,
                   sm=6,
                   md=4,
                   lg=2,
                   xl=2,
               ),
               dbc.Col(
                   dcc.Dropdown(
                       id="player-dropdown",
                       options=[{'label': player, 'value': player} for player in df['Player Name'].unique()],
                       placeholder="Player",
                       multi=True,
                       style={
                           "background-color": "transparent",
                           "color": "black",
                           "font-weight": "bold",
                           "width": "75%",
                           },
                   ),
                   xs=12,
                   sm=6,
                   md=4,
                   lg=2,
                   xl=2,
               ),       
           ],
           className="mb-3",
       ),
# --------------------------------------------------
# Row 2: Buttons  
# --------------------------------------------------
         dbc.Row(
            dbc.Col(html.Div([
                html.Div(
                    [
                        html.Img(
                            src="/assets/green_toggle.png",
                            id="jersey-toggle-btn",
                            className="toolbar-icon",
                            ),
                        html.Img(
                            src="/assets/line_white.png",
                            id="draw-lines-btn",
                            n_clicks=0,
                            className="toggle-icon",
                            ),
                        html.Img(
                               src="/assets/pen_white.png",
                               id="free-draw-btn",
                               className="toggle-icon",
                               ),
                        html.Img(
                           src="/assets/ball.png",
                           id="add-ball-btn",
                           style={
                               "width": "40px",
                               "cursor": "pointer",
                               "marginLeft": "10px"
                               }
                               ),
                        html.Img(
                               src="/assets/flag_white.png",
                               id="flag-toggle-btn",
                               className="toolbar-btn"
                               ),
                    ],
                    className="toolbar-mobile-row toolbar-mobile-row-primary",
                    ),
                html.Div(
                    [
                        html.Img(
                               src="/assets/reset.png",
                               id="reset-btn",
                               className="toolbar-btn"
                               ),
                        html.Img(
                            src="/assets/download.png",
                            id="export-btn",
                            className="export-icon"
                            ),
                        html.Img(
                            src="/assets/opponent_white.png",
                            id="opponent-toggle-btn",
                            className="toolbar-icon",
                            ),
                        dbc.Col(
                            html.Div(
                                html.Div(
                                    [
                                        dcc.Dropdown(
                                            id="opponent-formation-dropdown",
                                            options=[{'label': formation, 'value': formation} for formation in FORMATIONS],
                                            value="4-3-3 (Single Pivot)",
                                            placeholder="Formation",
                                            multi=False,
                                            clearable=False,
                                            style={
                                                "background-color": "transparent",
                                                "color": "black",
                                                "font-weight": "bold",
                                                "width": "180px",
                                                },
                                                )
                                                ],
                                                id="opponent-dropdown-tooltip-target",
                                                style={
                                                    "display": "inline-block",
                                                    "width": "180px",
                                                    },
                                                    ),
                                                    id="opponent-dropdown-container",
                                                    className="opponent-dropdown-hidden",
                                                    ),
                                                    className="toolbar-dropdown-wrapper",
                                                    ),
                    ],
                    className="toolbar-mobile-row toolbar-mobile-row-secondary",
                    ),
                                            ],
                                            className="toolbar-container toolbar-row"
                                            ),
                                            width=12,
                                            ),
                                            className="mb-4 toolbar-shell",
                                            ),
# --------------------------------------------------
# Tooltips
# --------------------------------------------------
                dbc.Tooltip(
                    "Toggle jersey colors between green and white. "
                    "Green icon = active green jerseys.",
                    target="jersey-toggle-btn",
                    placement="bottom",
                    ),
                dbc.Tooltip(
                    "Activate tactical connection mode. "
                    "Click two players to draw a passing connection. "
                    "Green icon = active.",
                    target="draw-lines-btn",
                    placement="bottom",
                    ),
                dbc.Tooltip(
                    "Activate free drawing mode to sketch tactical ideas on the pitch. "
                    "Green icon = active.",
                    target="free-draw-btn",
                    placement="bottom",
                    ),
                dbc.Tooltip(
                    "Add a draggable ball to the pitch.",
                    target="add-ball-btn",
                    placement="bottom",
                    ),
                dbc.Tooltip(
                    "Show or hide country flags above player jerseys. "
                    "Green icon = flags visible.",
                    target="flag-toggle-btn",
                    placement="bottom",
                    ),
                dbc.Tooltip(
                    "Reset the entire board: players, captain, drawings, "
                    "connections, flags, ball and opponents.",
                    target="reset-btn",
                    placement="bottom",
                    ),
                dbc.Tooltip(
                    "Export the current tactical board as an image.",
                    target="export-btn",
                    placement="bottom",
                    ),
                dbc.Tooltip(
                    "Show or hide opponent formation overlay. "
                    "Green icon = opponents visible.",
                    target="opponent-toggle-btn",
                    placement="bottom",
                    ),
                dbc.Tooltip(
                    "Choose the opponent formation displayed on the pitch.",
                    target="opponent-dropdown-tooltip-target",
                    placement="bottom",
                    autohide=True,
                    delay={"show": 200, "hide": 100},
                    ),   
# --------------------------------------------------
# Row 3: Pitch & Table 
# --------------------------------------------------
       html.Div(
           [
               html.Div(
                   id="pitch-wrapper",
                   children=[
                       html.Div(id="pitch", className="pitch-container")
                       ]
                       ),
                html.Div(
                    id="mobile-player-drawer",
                    className="open",
                    children=[
                html.Div(
                    "Players",
                    id="drawer-handle"
                    ),
                html.Div(
                    id="player-table"
                )
            ]
        )
    ],
    className="mobile-layout"
    ),
   ],
   fluid=True,
)

def get_latest_players(df):
   """
   Returns one row per player using latest Indexing
   """
   return (
       df.sort_values("Indexing", ascending=False)
         .drop_duplicates(subset="Player Name", keep="first")
         .sort_values("Sorting", ascending=True)
   )

# --------------------------------------------------
# CAPTAIN → PROXY (JS bridge)
# --------------------------------------------------
@app.callback(
   Output("captain-proxy", "children"),
   Input("captain-store", "data")
)
def sync_captain(captain):
   return captain or ""

@app.callback(
   Output("formation-proxy", "children"),
   Input("formation-dropdown", "value")
)
def sync_formation(f):
   return f or ""

# --------------------------------------------------
# OPPONENT DROPDOWN TOOLTIP
# --------------------------------------------------
@app.callback(
    Output("opponent-dropdown-tooltip", "style"),
    Input("opponent-dropdown-container", "className"),
)
def toggle_opponent_tooltip(class_name):

    if "opponent-dropdown-hidden" in class_name:
        return {"display": "none"}

    return {"display": "block"}

from dash import Input, Output, State, callback_context
from dash.exceptions import PreventUpdate
# --------------------------------------------------
# TABLE + CAPTAIN
# --------------------------------------------------
@app.callback(
   Output("player-table", "children"),
   Output("captain-store", "data"),
   Input("season-dropdown", "value"),
   Input("position-dropdown", "value"),
   Input("country-dropdown", "value"),
   Input("player-dropdown", "value"),
   Input({"type": "captain-toggle", "player": ALL}, "n_clicks"),
   State("captain-store", "data"),
)

def update_cards(selected_season, selected_positions, selected_counry, selected_players, star_clicks, current_captain):
   # start from dataframe copy
   dff = df.copy()
   # Apply season filter (multi)
   if selected_season == "ALL":
       # Get latest record per player
       dff = get_latest_players(dff)
   else:
      dff = dff[dff["Season"] == selected_season]

   # Apply position filter (multi)
   if selected_positions:
       if isinstance(selected_positions, str):
           selected_positions = [selected_positions]
       dff = dff[dff["Field Position"].isin(selected_positions)]
   # Apply position filter (multi)
   if selected_counry:
       if isinstance(selected_counry, str):
           selected_counry = [selected_counry]
       dff = dff[dff["Country of Origin"].isin(selected_counry)]    
   # Apply player filter (multi)
   if selected_players:
       if isinstance(selected_players, str):
           selected_players = [selected_players]
       dff = dff[dff["Player Name"].isin(selected_players)]
   triggered = ctx.triggered_id
   # Default: keep existing captain
   captain = current_captain
   # Only update captain if star clicked
   if isinstance(triggered, dict):
       clicked = triggered["player"]
       captain = None if clicked == current_captain else clicked
# -------------------------
# Build table using captain
# -------------------------
   # HEADER
   table_header = html.Thead(
       html.Tr([
           html.Th("Captain", className="table-header", style={"width": "40px"}),
           html.Th("Player", className="table-header"),
           html.Th("Position", className="table-header"),
           html.Th("Country", className="table-header"),
           ]))        
   # BODY
   rows = []
   for _, row in dff.iterrows():
       is_captain = row["Player Name"] == captain  # ← from State
       rows.append(
   html.Tr(
       [
           # Captain Selection
           html.Td(
               html.Span(
                   "⭐" if is_captain else "☆",
                   id={
                       "type": "captain-toggle",
                       "player": row["Player Name"]
                   },
                   n_clicks=0,
                   className="star",
                   style={"textAlign": "center"},
               ),
           ),
           # Player Name
           html.Td(
               row["Player Name"],
               draggable="true",
               className="draggable-player",
               **{"data-player": row["Player Name"], "data-player-row": row["Player Name"], "data-flag": row["Flag"]},
               style={"textAlign": "center"},
           ),
           # Position
           html.Td(
               row["Abbreviation"],
               style={"textAlign": "center"}
           ),
           # FLAG IMAGE
           html.Td(
               html.Img(
                   src=row["Flag"],
                   className="flag"
               ),
               style={"textAlign": "center"},
           ),
       ],
       className="captain-row" if is_captain else "",
   )
)
   table_body = html.Tbody(rows)    
   table = dbc.Table(
           [table_header, table_body],
           bordered=True,
           hover=True,
           striped=True,
           size="sm",
           className="player-table"
           )    
   
   return html.Div(table, className="table-container"), captain       
# ==========================================================
# UPDATE PITCH WHEN FORMATION CHANGES
# ==========================================================

@app.callback(
   Output("pitch", "children"),
   Input("formation-dropdown", "value"),
)

def update_pitch(formation):

    positions = FORMATIONS[formation]

    # =====================================
    # MOBILE VIEW DETECTION
    # =====================================
    user_agent = flask.request.headers.get(
        "User-Agent",
        ""
    )

    is_mobile = (
        "Mobile" in user_agent
        or "iPhone" in user_agent
        or "Android" in user_agent
    )

    # =====================================
    # PLAYER SLOTS
    # =====================================
    player_slots = []

    mobile_positions = MOBILE_FORMATIONS.get(formation)

    for index, (pos, x, y) in enumerate([
        (p, float(px), float(py))
        for p, px, py in positions
    ]):

        render_x = x
        render_y = y
        mobile_x = None
        mobile_y = None

        if mobile_positions and index < len(mobile_positions):
            _mobile_pos, mobile_x, mobile_y = mobile_positions[index]

        # Apply mobile transform
        if is_mobile:
            if mobile_x is not None and mobile_y is not None:
                render_x = float(mobile_x)
                render_y = float(mobile_y)
            else:
                render_x, render_y = (
                    transform_mobile_coordinate(
                        x,
                        y
                    )
                )

        slot = html.Div(
            [
                html.Img(
                    src="/assets/goalkeeper_player.png"
                    if pos == "GK"
                    else "/assets/green_player.png",
                    className="jersey-img"
                ),

                html.Div(
                    pos,
                    className="position-label"
                ),

                html.Div(
                    "",
                    className="player-name"
                ),
            ],

            className=(
                "position-slot goalkeeper-slot"
                if pos == "GK"
                else "position-slot"
            ),

            draggable="true",

            style={
                # left = horizontal axis
                # top = vertical axis
                "left": f"{render_x}%",
                "top": f"{render_y}%"
            },

            **{
                "data-position": pos,
                "data-original": pos,
                "data-index": index,
                "data-x": x,
                "data-y": y,
                "data-mobile-x": mobile_x if mobile_x is not None else "",
                "data-mobile-y": mobile_y if mobile_y is not None else "",
            },
        )

        player_slots.append(slot)

    # =====================================
    # PITCH
    # =====================================
    return html.Div(

        className="pitch",

        children=[

            # SVG LINES LAYER
            svg.Svg(
                id="connections-layer",
                className="connections-layer"
            ),

            # OPPONENT LAYER
            html.Div(
                id="opponents-layer",
                className="opponents-layer",
            ),

            # PLAYER LAYER
            html.Div(
                className="positions-layer",
                children=player_slots
            ),
        ],
    )

if __name__ == "__main__":
   app.run(debug=True)
