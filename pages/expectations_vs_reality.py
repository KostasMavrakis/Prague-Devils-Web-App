import dash
from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import re
from data_loader import load_reality_check

TOOLTIP_CONTENT = {

    "Shooting": {

        "internal": {
            "title": "Shooting",
            "lines": [
                "Positioning",
                "Finishing",
                "Shot Power",
                "Long Shots",
                "Volleys",
                "Penalties"
            ]
        },

        "external": {
            "title": "Max Shot Speed",
            "lines": [
                "Fastest shot taken."
            ]
        }
    },

    "Speed": {

        "internal": {
            "title": "Pace",
            "lines": [
                "Acceleration",
                "Sprint Speed"
            ]
        },

        "external": {
            "title": "Max Speed",
            "lines": [
                "Maximum speed the player achieved."
            ]
        }
    },

    "Stamina": {

        "internal": {
            "title": "Physicality",
            "lines": [
                "Jumping",
                "Stamina",
                "Strength",
                "Aggression"
            ]
        },

        "external": {
            "title": "Stamina Score",
            "lines": [
                "Stamina Score = 0.5 × Normalized Distance/min + 0.3 × Normalized HSR/min + 0.2 × Normalized High-Intensity Distance/min",
                "",
                "Each metric in the formula is converted to a normalized score by dividing each player's individual values by the Team's average. This is done, because the metrics are not naturally comparable, as they use different scales. Normalization reflects performance relative to the Team. It reduces the impact of outliers and makes weights meaningful.",
                "",
                "Distance per minute: Distance the player covered, divided by the duration of the session.",
                "",
                "High Speed Running (HSR): Distance covered over 5,5 m/s.",
                "",
                "High Intensity Distance: Combination of all of the player's High Speed Running and the distance covered while accelerating and decelerating.",
            ]
        }
    }
}

# =====================================================
# PAGE REGISTRATION
# =====================================================

dash.register_page(__name__, path="/reality_check", name="Expectations vs Reality")

# =====================================================
# LOAD DATA
# =====================================================

df = load_reality_check()
df = df.fillna("")

# Convert values from comma-separated to dot-separated floats
df['STATSports Max Speed (m/s)'] = df['STATSports Max Speed (m/s)'].astype(str).str.replace(",", ".").astype(float)/100
df['Max Shot Speed (km/h)'] = df['Max Shot Speed (km/h)'].astype(str).str.replace(",", ".").astype(float)/100
df['Stamina Score'] = df['Stamina Score'].astype(str).str.replace(",", ".").astype(float)/100

CHART_TOP_MARGIN = 10
CHART_BOTTOM_MARGIN = 20
PLAYER_ROW_HEIGHT = 38


def get_flag_src(flag_value):
    flag_value = str(flag_value or "").strip()

    match = re.search(r'src=["\']([^"\']+)["\']', flag_value)

    if match:
        return match.group(1)

    return flag_value

# =====================================================
# METRIC MAPPING
# =====================================================
METRIC_MAPPING = {
    "Shooting": {
        "internal": "Shooting",
        "external": "Max Shot Speed (km/h)"
    },
    "Speed": {
        "internal": "Pace",
        "external": "STATSports Max Speed (m/s)"
    },
    "Stamina": {
        "internal": "Physicality",
        "external": "Stamina Score"
    }
}

# =====================================================
# TOOLTIP METRIC MAPPING
# =====================================================
TOOLTIP_METRIC_MAPPING = {
    "Shooting": {
        "internal_label": "Shooting",
        "external_label": "Max Shot Speed (km/h)",
        "ranking_column": "Shooting Ranking",
    },
    "Speed": {
        "internal_label": "Pace",
        "external_label": "Max Speed (m/s)",
        "ranking_column": "Speed Ranking",
    },
    "Stamina": {
        "internal_label": "Physicality",
        "external_label": "Stamina Score",
        "ranking_column": "Stamina Ranking",
    }
}
# =====================================================
# DROPDOWN OPTIONS
# =====================================================

position_options = sorted(
    [
        p for p in
        df["Field Position"].dropna().unique()
        if str(p).strip()
    ]
)

nationality_options = sorted(
    [
        n for n in
        df["Nationality"].dropna().unique()
        if str(n).strip()
    ]
)

player_options = sorted(
    [
        p for p in
        df["Player"].dropna().unique()
        if str(p).strip()
    ]
)


# =====================================================
# LAYOUT
# =====================================================

layout = dbc.Container(
    fluid=True,
    className="reality-check-page",
    children=[

        dbc.Row([

            dbc.Col(
                dcc.Dropdown(
                    id="rc-metric-dropdown",
                    options=[
                        {
                            "label": "Shooting",
                            "value": "Shooting"
                        },
                        {
                            "label": "Speed",
                            "value": "Speed"
                        },
                        {
                            "label": "Stamina",
                            "value": "Stamina"
                        }
                    ],
                    value="Speed",
                    clearable=False,
                    style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "75%",
                    },
                ),
                md=3
            ),

            dbc.Col(
                dcc.Dropdown(
                    id="rc-position-dropdown",
                    options=['Goalkeepers','Defenders','Midfielders','Forwards'],
                    placeholder="Position",
                    style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "75%",
                    },
                ),
                md=3
            ),

            dbc.Col(
                dcc.Dropdown(
                    id="rc-nationality-dropdown",
                    options=[{"label": x, "value": x} for x in nationality_options],
                    placeholder="Country",
                    style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "75%",
                    },
                ),
                md=3
            ),

            dbc.Col(
                dcc.Dropdown(
                    id="rc-player-dropdown",
                    options=[{"label": x, "value": x} for x in player_options],
                    placeholder="Player",
                    style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "75%",
                    },
                ),
                md=3
            ),
        ]),

        html.Br(),

        dbc.Row([
            dbc.Col(
                html.Div(
                    id="rc-ranking-panel"
                ),
                width="auto",
                className="rc-ranking-col"
            ),
            dbc.Col(
                [
                    html.Div(
                        id="rc-internal-title",
                        className="rc-chart-title"
                        ),
                    dbc.Tooltip(
                        id="rc-internal-tooltip",
                        target="rc-internal-title",
                        placement="top",
                        autohide=True,
                        delay={
                            "show": 500,
                            "hide": 2000
                            }
                    ),
                    dcc.Graph(
                        id="rc-chart-internal",
                        config={
                            "displayModeBar": False
                            }
                    )
                ],
                className="rc-internal-chart-col"
            ),            
            dbc.Col(
                [
                    html.Div(
                        id="rc-external-title",
                        className="rc-chart-title"
                    ),
                    dbc.Tooltip(
                        id="rc-external-tooltip",
                        target="rc-external-title",
                        placement="top",
                        autohide=True,
                        delay={
                            "show": 500,
                            "hide": 2000
                            }
                    ),
                    dcc.Graph(
                        id="rc-chart-external",
                        config={
                            "displayModeBar": False
                            }
                    )
                ],
                className="rc-external-chart-col"
            )
        ], className="reality-chart-row")
    ]
)

# =====================================================
# CALLBACK
# =====================================================

@callback(
    Output("rc-chart-internal","figure"),
    Output("rc-chart-external","figure"),
    Output("rc-ranking-panel","children"),
    Output("rc-internal-title","children"),
    Output("rc-external-title","children"),
    Output("rc-internal-tooltip","children"),
    Output("rc-external-tooltip","children"),
    Input("rc-position-dropdown","value"),
    Input("rc-nationality-dropdown","value"),
    Input("rc-player-dropdown","value"),
    Input("rc-metric-dropdown","value")
)

def update_reality_check(
    position,
    nationality,
    player,
    metric
):

    filtered = df.copy()

    # =====================================
    # FILTERS
    # =====================================

    if position:
        filtered = filtered[
            filtered["Field Position"] == position
        ]

    if nationality:
        filtered = filtered[
            filtered["Nationality"] == nationality
        ]

    if player:
        filtered = filtered[
            filtered["Player"] == player
        ]

    # =====================================
    # METRICS
    # =====================================

    internal_col = (
        METRIC_MAPPING[metric]["internal"]
    )

    external_col = (
        METRIC_MAPPING[metric]["external"]
    )

    filtered[internal_col] = pd.to_numeric(
        filtered[internal_col],
        errors="coerce"
    )

    filtered[external_col] = pd.to_numeric(
        filtered[external_col],
        errors="coerce"
    )

    filtered = filtered.sort_values(
        internal_col,
        ascending=False
    )

    filtered = filtered.reset_index(
        drop=True
    )

    filtered["Rank"] = (
        filtered.index + 1
    )

    chart_height = (
        CHART_BOTTOM_MARGIN +
        max(1, len(filtered)) * PLAYER_ROW_HEIGHT
    )

    internal_title = (
        f"Expectations: {internal_col}"
        )
    external_title = (
        f"Reality: {external_col}"
        )
    
    internal_tooltip_data = (
        TOOLTIP_CONTENT[metric]["internal"]
        )
    
    external_tooltip_data = (
        TOOLTIP_CONTENT[metric]["external"]
        )
    
    internal_tooltip = html.Div(
        [
            html.Div(
                internal_tooltip_data["title"],
                style={
                    "fontWeight": "bold",
                    "fontSize": "15px",
                    "marginBottom": "6px"
                    }
                )
        ] +
        [
            html.Div(
                line,
                style={
                    "fontSize": "12px"
                }
            )

            for line in internal_tooltip_data["lines"]
        ]
    )

    external_tooltip = html.Div(
        [
            html.Div(
                external_tooltip_data["title"],
                style={
                    "fontWeight": "bold",
                    "fontSize": "15px",
                    "marginBottom": "6px"
                    }
                )
        ] +
        [
            html.Div(
                line,
                style={
                    "fontSize": "12px"
                    }
                )
                for line in external_tooltip_data["lines"]
        ]
    )
    # =====================================
    # CHART 1
    # =====================================

    internal_hover = []
    
    metric_label = TOOLTIP_METRIC_MAPPING[metric]["internal_label"]
    for _, row in filtered.iterrows():
        internal_hover.append(
            f"<b style='font-size:15px'>{row['Player']}</b><br>"
            f"Position: {row['Main Position']}<br>"
            f"# of Ratings: {row['Number of Ratings']}<br>"
            f"Average Rating: {row['Average Rating']}<br>"
            f"{metric_label}: {row[internal_col]}"
        )

    fig_internal = go.Figure()

    fig_internal.add_bar(
        y=filtered["Player"],
        x=filtered[internal_col],
        orientation="h",
        marker_color="rgb(0,123,164)",
        text=filtered[internal_col],
        textposition="outside",
        hovertext=internal_hover,
        hoverinfo="text"
    )

    fig_internal.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(visible=False),
        font=dict(color="white"),
        yaxis=dict(
            showticklabels=False,
            autorange="reversed"
        ),
        margin=dict(
            l=10,
            r=30,
            t=CHART_TOP_MARGIN,
            b=CHART_BOTTOM_MARGIN
        ),
        hoverlabel=dict(
            bgcolor="white",
            font=dict(
                color="black",
                size=12
                ),
            bordercolor="rgb(200,200,200)"
        ),
        height=chart_height
    )

    fig_internal.update_traces(
    textfont=dict(
        color="white",
        size=13
        )
    )

    # =====================================
    # CHART 2
    # =====================================
    external_hover = []
    external_metric = TOOLTIP_METRIC_MAPPING[metric]["external_label"]
    ranking_column = TOOLTIP_METRIC_MAPPING[metric]["ranking_column"]
    for _, row in filtered.iterrows():
        external_hover.append(
            f"<b style='font-size:15px'>{row['Player']}</b><br>"
            f"Position: {row['Main Position']}<br>"
            f"Tracking Date: {row['Tracking Date']}<br>"
            f"Competition: {row['Competition']}<br>"
            f"{external_metric}: {row[external_col]}<br>"
            f"Ranking: {row[ranking_column]}"
        )

    fig_external = go.Figure()

    fig_external.add_bar(
        y=filtered["Player"],
        x=filtered[external_col],
        orientation="h",
        marker_color="rgb(228,155,88)",
        text=filtered[external_col],
        textposition="outside",
        hovertext=external_hover,
        hoverinfo="text"
    )

    fig_external.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(visible=False),
        font=dict(color="white"),
        yaxis=dict(
            showticklabels=False,
            autorange="reversed"
        ),
        margin=dict(
            l=10,
            r=30,
            t=CHART_TOP_MARGIN,
            b=CHART_BOTTOM_MARGIN
        ),
        hoverlabel=dict(
            bgcolor="white",
            font=dict(
                color="black",
                size=12
                ),
            bordercolor="rgb(200,200,200)"
        ),
        height=chart_height
    )

    fig_external.update_traces(
    textfont=dict(
        color="white",
        size=13
        )
    )

    # =====================================
    # RANKING PANEL
    # =====================================

    ranking_rows = [
        html.Div(
            className="player-ranking-header",
            children=[
                html.Div("#", className="ranking-index"),
                html.Div("Player", className="ranking-player"),
                html.Div("Country", className="ranking-flag-header"),
                html.Div("Position", className="ranking-position"),
            ]
        )
    ]

    for row_index, (_, row) in enumerate(filtered.iterrows()):

        flag_tooltip_id = f"rc-flag-tooltip-target-{row_index}"
        position_tooltip_id = f"rc-position-tooltip-target-{row_index}"

        ranking_rows.append(

            html.Div(

                className="player-ranking-row",

                children=[

                    html.Div(
                        row["Rank"],
                        className="ranking-index"
                    ),

                    html.Div(
                        row["Player"],
                        className="ranking-player"
                    ),

                    html.Img(
                        src=get_flag_src(row["Flag"]),
                        id=flag_tooltip_id,
                        className="ranking-flag"
                    ),

                    html.Div(
                        row["Main Position"],
                        id=position_tooltip_id,
                        className="ranking-position"
                    ),

                    dbc.Tooltip(
                        row["Nationality"],
                        target=flag_tooltip_id,
                        placement="top",
                        autohide=True,
                        delay={"show": 200, "hide": 100},
                    ),

                    dbc.Tooltip(
                        row["Role"],
                        target=position_tooltip_id,
                        placement="top",
                        autohide=True,
                        delay={"show": 200, "hide": 100},
                    )

                ]
            )
        )

    return (
        fig_internal,
        fig_external,
        html.Div(
            ranking_rows,
            className="player-ranking-panel"
            ),
        internal_title,
        external_title,
        internal_tooltip,
        external_tooltip
        )
