import dash
from dash import html, dcc, ALL, ctx, Input, Output, State
import dash_bootstrap_components as dbc
from data_loader import load_all_players
# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR, '/assets/lineup.css'], suppress_callback_exceptions=True, meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
df = load_all_players()
# --------------------------------------------------
# FORMATIONS
# --------------------------------------------------
FORMATIONS = {
   "4-3-3": [
       ("GK", 5, 50),
       ("LB", 20, 10), ("CB", 14, 35),
       ("CB", 14, 65), ("RB", 20, 90),
       ("CM", 53, 30), ("CM", 39.5, 50), ("CM", 53, 70),
       ("LW", 68, 10), ("ST", 77, 50), ("RW", 68, 90),
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
       ("LM", 62, 10), ("LCM", 39.5, 35),
       ("RCM", 39.5, 65), ("RM", 62, 90),
       ("CF", 68, 50),
       ("ST", 77, 50),
   ],
   "4-3-2-1": [
       ("GK", 5, 50),
       ("LB", 20, 10), ("CB", 14, 35),
       ("CB", 14, 65), ("RB", 20, 90),
       ("LCM", 53, 30), ("CM", 39.5, 50),
       ("RCM", 53, 70),
       ("LAM", 68, 35), ("RAM", 68, 65),
       ("ST", 77, 50),
   ],
   "4-2-3-1": [
       ("GK", 5, 50),
       ("LB", 20, 10), ("CB", 14, 35),
       ("CB", 14, 65), ("RB", 20, 90),
       ("CDM", 39.5, 35), ("CDM", 39.5, 65),
       ("LW", 62, 10), ("CAM", 62, 50), ("RW", 62, 90),
       ("ST", 77, 50),
   ],
   "4-5-1": [
       ("GK", 5, 50),
       ("LB", 20, 10), ("CB", 14, 35),
       ("CB", 14, 65), ("RB", 20, 90),
       ("LM", 62, 10),
       ("LCM", 53, 35), ("CM", 39.5, 50), ("RCM", 53, 65),
       ("RM", 62, 90),
       ("ST", 77, 50),
   ],
   "3-4-3": [
       ("GK", 5, 50),
       ("LCB", 14, 25), ("CB", 14, 50), ("RCB", 14, 75),
       ("LM", 53, 10), ("LCM", 39.5, 35),
       ("RCM", 39.5, 65), ("RM", 53, 90),
       ("LW", 68, 10), ("ST", 77, 50), ("RW", 68, 90),
   ],
   "3-5-2": [
       ("GK", 5, 50),
       ("LCB", 14, 25), ("CB", 14, 50), ("RCB", 14, 75),
       ("LM", 62, 10),
       ("LCM", 53, 35), ("CM", 39.5, 50), ("RCM", 53, 65),
       ("RM", 62, 90),
       ("ST", 77, 35), ("ST", 77, 65),
   ],
   "3-6-1": [
       ("GK", 5, 50),
       ("LCB", 14, 25), ("CB", 14, 50), ("RCB", 14, 75),
       ("LM", 62, 10),
       ("LCM", 53, 30), ("CM", 39.5, 50), ("RCM", 53, 70),
       ("RM", 62, 90),
       ("CAM", 68, 50),
       ("ST", 77, 50),
   ],
   "5-3-2": [
       ("GK", 5, 50),
       ("LWB", 28, 10),
       ("LCB", 14, 30), ("CB", 14, 50), ("RCB", 14, 70),
       ("RWB", 28, 90),
       ("LCM", 53, 30), ("CM", 39.5, 50), ("RCM", 53, 70),
       ("ST", 77, 35), ("ST", 77, 65),
   ],
   "5-4-1": [
       ("GK", 5, 50),
       ("LWB", 28, 10),
       ("LCB", 14, 30), ("CB", 14, 50), ("RCB", 14, 70),
       ("RWB", 28, 90),
       ("LM", 62, 10), ("LCM", 39.5, 35),
       ("RCM", 39.5, 65), ("RM", 62, 90),
       ("ST", 77, 50),
   ],
}
# --------------------------------------------------
# LAYOUT
# --------------------------------------------------
app.layout = dbc.Container(
   [
       dcc.Store(id="captain-store"),
       dbc.Row(
           [
               dbc.Col(
                   dcc.Dropdown(
                       id="formation-dropdown",
                       options=[{'label': formation, 'value': formation} for formation in FORMATIONS],
                       #options=[{"label": k, "value": k} for k in FORMATIONS],
                       value="4-3-3",
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
                   sm=12,
                   md=3,
                   lg=3,
                   xl=3,
               ),
               dbc.Col(
                   dcc.Dropdown(
                       id="season-dropdown",
                       options=[{'label': season, 'value': season} for season in df['Season'].unique()],
                       value="2025 - 2026",
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
                   sm=12,
                   md=3,
                   lg=3,
                   xl=3,
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
                   sm=12,
                   md=3,
                   lg=3,
                   xl=3,
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
                   sm=12,
                   md=3,
                   lg=3,
                   xl=3,
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
                   sm=12,
                   md=3,
                   lg=3,
                   xl=3,
               ),
               dbc.Col(
                   html.Button("Export PNG", id="export-btn"),
                   xs=12,
                   sm=12,
                   md=3,
                   lg=3,
                   xl=3,
               ),
           ],
           className="mb-4",
       ),
       dbc.Row(
           [
               dbc.Col(
                   html.Div(id="pitch", className="pitch-container"),
                   md=8,
               ),
               dbc.Col(
                   html.Div(id="player-table"),
                   md=4,
               ),
           ]
       ),
   ],
   fluid=True,
)
# ==========================================================
# UPDATE TABLE + CAPTAIN OPTIONS
# ==========================================================
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
   if selected_season:
       if isinstance(selected_season, str):
           selected_season = [selected_season]
       dff = dff[dff["Season"].isin(selected_season)]
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
                   "★" if is_captain else "☆",
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
               **{"data-player": row["Player Name"], "data-player-row": row["Player Name"]},
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
           responsive=True,
           striped=True,
           size="sm",
           className="player-table"
           )    
   return table, captain        
# ==========================================================
# UPDATE PITCH WHEN FORMATION CHANGES
# ==========================================================
@app.callback(
   Output("pitch", "children"),
   Input("formation-dropdown", "value"),
)
def update_pitch(formation):
   positions = FORMATIONS[formation]
   return html.Div(
       className="pitch",
       children=[
           html.Div(
               className="positions-layer",
               children=[
                   html.Div(
                       pos,
                       className="position-slot",
                       **{
                           "data-position": pos,
                           "data-original": pos
                           },
                       style={
                           "left": f"{x}%",
                           "top": f"{y}%"
                       },
                   )
                   for pos, x, y in positions
               ]
           )
       ]
   )
# Run the app
if __name__ == '__main__':
   app.run(debug=True)
