import dash
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
from data_loader import load_ratings_helper

# Initialize the Dash app
dash.register_page(__name__, path='/ratings', name="Ratings")
CATEGORY_TOOLTIPS = {
   "PAC": {"title": "Pace", "desc": "Acceleration, Sprint Speed"},
   "SHO": {"title": "Shooting", "desc": "Positioning, Finishing, Shot Power, Long Shots, Volleys, Penalties"},
   "PAS": {"title": "Passing", "desc": "Vision, Crossing, Free Kick Accuracy, Short Passing, Long Passing, Curve"},
   "DRI": {"title": "Dribbling", "desc": "Agility, Balance, Reactions, Ball Control, Dribbling, Composure"},
   "PHY": {"title": "Physicality", "desc": "Jumping, Stamina, Strength, Aggression"},
   "DEF": {"title": "Defense", "desc": "Interceptions, Heading, Accuracy, Def Awareness, Standing Tackle, Sliding Tackle"},
   "TAC": {"title": "Tactical Intelligence", "desc": "Scanning, Anticipation, Decision-Making, Adaptability, Communication, Game Intelligence"},
   "GK": {"title": "Goalkeeping", "desc": "GK Diving, GK Handling, GK Kicking, GK Positioning, GK Reflexes"}
}
df = load_ratings_helper()
# Ensure required columns exist
required_cols = ["Player", "Season", "Field Position", "Role", "Main Position", "Flag",
                "Average Rating", "Number of Ratings", "Comments", "PAC", "SHO", "PAS", "DRI", "PHY", "DEF", "TAC", "GK"]
for c in required_cols:
   if c not in df.columns:
       df[c] = None
# Convert numeric-ish columns to numeric and make integers for display
num_cols = ["Average Rating", "Number of Ratings", "PAC", "SHO", "PAS", "DRI", "PHY", "DEF", "TAC", "GK"]
for c in num_cols:
   # handle comma decimal separators too, coerce invalid -> NaN
   df[c] = df[c].astype(str).str.replace(",", ".").replace({"nan": ""})
   df[c] = pd.to_numeric(df[c], errors="coerce")
# Helper to format integer display, show em dash for missing
def as_int_display(x):
   if pd.isna(x):
       return "â€”"
   try:
       return str(int(round(x)))
   except Exception:
       return "â€”"
CATEGORIES = ["PAC", "SHO", "PAS", "DRI", "PHY", "DEF", "TAC", "GK"]

# Layout of the Dash app
layout = dbc.Container(
   [
       html.Div(
           html.A(
               html.Div(
                   html.Img(src="/assets/sticker.png", className="sticker-image"),
                   className="sticker-wrapper"
               ),
               href="https://forms.fillout.com/t/cYF92QeD4jus",
               target="_blank"
           ),
           className="sticker-container"
       ),
       dbc.Row(
           [
               dbc.Col(
                   dcc.Dropdown(
                       id="season-dropdown",
                       options=[{'label': season, 'value': season} for season in df['Season'].unique()],
                       value="2025 - 2026",
                       placeholder="Squad",
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
                       options=[{'label': country, 'value': country} for country in df['Nationality'].unique()],
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
                       options=[{'label': player, 'value': player} for player in df['Player'].unique()],
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
           ],
           className="mb-4",
       ),
       # Cards container
       dbc.Row(id="cards-container", className="g-4", justify="center"),
   ],
   fluid=True,
)

@callback(
   Output("cards-container", "children"),
   [
       Input("season-dropdown", "value"),
       Input("position-dropdown", "value"),
       Input("country-dropdown", "value"),
       Input("player-dropdown", "value"),
   ],
)
def update_cards(selected_season, selected_positions, selected_counry, selected_players):
   """
   Build a card per player matching filters.
   - selected_players: list or None
   - selected_season: single value or None
   - selected_positions: list or None
   """
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
       dff = dff[dff["Nationality"].isin(selected_counry)]    
   # Apply player filter (multi)
   if selected_players:
       if isinstance(selected_players, str):
           selected_players = [selected_players]
       dff = dff[dff["Player"].isin(selected_players)]
   # If no rows, return a user message
   if dff.empty:
       return [
           dbc.Col(
               html.Div("No players match the selection.", style={"color": "white", "padding": "20px", "textAlign": "center"}),
               width=12,
           )
       ]
   # group by player to ensure one card per player (if sheet has multiple rows per player/season, aggregate)
   # We'll take the first Flag/Main Position and compute mean Average Rating + mean category values
   grouped = (
       dff.groupby("Player", sort=False)
       .agg(
           {
               "Average Rating": "mean",
               "Number of Ratings": "sum",  # or "mean" depending on your data logic
               "Role": lambda x: x.dropna().iloc[0] if len(x.dropna()) > 0 else None,
               "Main Position": lambda x: x.dropna().iloc[0] if len(x.dropna()) > 0 else None,
               "Flag": lambda x: x.dropna().iloc[0] if len(x.dropna()) > 0 else None,
               "Field Position": lambda x: ", ".join(sorted(x.dropna().unique())),
               "Comments": lambda x: x.dropna().iloc[0] if len(x.dropna()) > 0 else None,
               **{cat: "mean" for cat in CATEGORIES if cat in dff.columns},
           }
       )
       .reset_index()
   )

   cols = []
   for _, row in grouped.iterrows():
       player = row["Player"]
       main_pos = row.get("Main Position", "") or ""
       flag = row.get("Flag", "") or ""
       avg_rating = as_int_display(row.get("Average Rating", None))
       num_ratings = as_int_display(row.get("Number of Ratings", None))
       role = row.get("Role", "")
       comments = row.get("Comments", "") or ""
       SPECIAL_GK_PLAYERS = {"tiziano", "deni p."} # Players who should always see the GK category even if their role is not "Goalkeeper"
       if str(role).strip().lower() == "goalkeeper" or str(player).strip().lower() in SPECIAL_GK_PLAYERS:
           cats_to_show = CATEGORIES  # include GK
       else:
           cats_to_show = [c for c in CATEGORIES if c != "GK"]  # exclude GK
       cat_vals = [as_int_display(row.get(cat, None)) for cat in cats_to_show]
       # Replace " / " with newlines for nicer tooltip formatting
       comments_tooltip = comments.replace(" / ", "\n")
       # --- CATEGORY HEADERS + TOOLTIPS (FIXED VERSION) ---
       category_header_row = html.Div(
           [
               html.Div(
                   [
                       # the category label
                       html.Div(
                           cat,
                           id=f"cat-{player}-{cat}",
                           style={
                               "fontWeight": "700",
                               "fontSize": "16px",
                               "textAlign": "center",
                               "whiteSpace": "nowrap",
                               "overflow": "visible",
                               "flex": "1 1 0",
                               "minWidth": "0",
                               "padding": "0 5px",
                               "color": "rgb(67,48,9)"
                           },
                       ),
                       # the tooltip (now correctly bound as sibling)
                       dbc.Popover(
                           [
                               html.Div(
                                   [
                                       html.Div(
                                           CATEGORY_TOOLTIPS[cat]["title"],
                                           style={"fontWeight": "700", "fontSize": "15px", "marginBottom": "4px"},
                                       ),
                                       html.Div(
                                           [
                                               html.Div(line)
                                               for line in CATEGORY_TOOLTIPS[cat]["desc"].split(", ")
                                           ],
                                           style={"fontSize": "13px", "whiteSpace": "normal"},
                                       ),
                                   ]
                               )
                           ],
                           target=f"cat-{player}-{cat}",
                           body=True,
                           trigger="hover",
                           placement="top",
                           style={
                               "backgroundColor": "white",  # white background
                               "color": "black",             # black text
                               "border": "1px solid rgba(0,0,0,0.1)",  # optional subtle border
                               "boxShadow": "0 2px 6px rgba(0,0,0,0.15)",  # optional shadow for readability
                               "padding": "8px",
                           },
                       ),
                   ],
                   style={
                       "flex": "1 1 0",
                       "textAlign": "center",
                       "minWidth": "0",           # allows flex-shrink to actually wor
                   },
               )
               for cat in cats_to_show
           ],
           style={
               "display": "flex",
               "flexWrap": "nowrap",
               "justifyContent": "space-between",
               "marginTop": "12px",
               "width": "100%",
           },
       )
       # Card content arranged vertically (column)
       card_body = html.Div(
           [
               # Average Rating - top
               html.Div([
                   html.Div(avg_rating, id=f"avg-rating-{player}", style={"fontSize": "30px", "fontWeight": "700", "textAlign": "center", "lineHeight": "1.0", "color": "rgb(67,48,9)"}),
                   dbc.Tooltip(f"Number of Ratings: {num_ratings}",
                           target=f"avg-rating-{player}",
                           placement="top",
                           style={"fontSize": "13px", "backgroundColor": "white"})],
                   style={"marginBottom": "6px"}),
               # Main position - under rating
               html.Div([
                   html.Div(main_pos, id=f"position-{player}", style={"fontSize": "22px", "opacity": 0.9, "textAlign": "center", "marginTop": "4px", "color": "rgb(67,48,9)"}),
                   dbc.Tooltip(f"Primary Position: {role}",
                           target=f"position-{player}",
                           placement="top",
                           style={"fontSize": "13px"})],
                   style={"marginBottom": "8px"}),
               # flag + player name row (horizontal)
               html.Div(
                   [
                       html.Img(src=flag, style={"height": "28px", "width": "auto", "marginRight": "8px", "display": "inline-block", "verticalAlign": "middle"}),
                       html.Span(player, id=f"player-name-{player}", style={"fontSize": "18px", "fontWeight": "600", "verticalAlign": "middle", "display": "inline-block", "color": "rgb(67,48,9)"}),
                       dbc.Tooltip(
                           comments_tooltip,
                           target=f"player-name-{player}",
                           placement="bottom",
                           style={"whiteSpace": "pre-line", "fontSize": "13px"},
                           ),
                   ],
                   style={"display": "flex", "alignItems": "center", "justifyContent": "center", "marginTop": "8px"},
               ),
               # categories headers row (full width)
               category_header_row,
               # categories values row (full width, directly under headers)
               html.Div(
                   [html.Div(val, style={"fontSize": "17px", "textAlign": "center", "whiteSpace": "nowrap", "overflow": "hidden", "textOverflow": "ellipsis", "flex": "1 1 0", "minWidth": "0", "padding": "0 2px", "color": "rgb(67,48,9)"}) for val in cat_vals],
                   style={"display": "flex", "flexWrap": "nowrap", "justifyContent": "space-between", "marginTop": "3px", "width": "100%"},
               ),
           ],
           style={
               "display": "flex",
               "flexDirection": "column",   # enforce vertical stacking
               "alignItems": "center",
               "justifyContent": "flex-start",
               "height": "100%",
               "gap": "4px",
           },
       )
       card = dbc.Card(
           dbc.CardBody(card_body, style={"padding": "10px", "height": "100%"}),
           className="player-card",
           style={
               "border": "1px solid rgba(255,255,255,0.12)",
               "borderRadius": "10px",
               "width": "100%",      # allow card to take full column width
               "minWidth": "300px",  # optional: set a minimum width
               "maxWidth": "500px",  # optional maximum width
               "height": "240px",  # enough vertical space
               "display": "flex",
               "flexDirection": "column",
               "justifyContent": "center",
           },
       )
       cols.append(dbc.Col(card, xs=12, sm=6, md=4, lg=3, xl=2, style={"display": "flex", "justifyContent": "center"}))
       
   return cols
