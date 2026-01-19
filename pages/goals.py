import dash
from dash import dcc, dash_table, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from data_loader import load_chart_data, load_goals

# Initialize the Dash app
dash.register_page(__name__, path='/goals', name="Goals")

chart_prep_df = load_chart_data()

goals_df = load_goals()

# Handle decimal separator conversion
chart_prep_df['Average Goals Scored per Match'] = chart_prep_df['Average Goals Scored per Match'].astype(str).str.replace(",", ".").astype(float)/100
chart_prep_df['Average Goals Conceded per Match'] = chart_prep_df['Average Goals Conceded per Match'].astype(str).str.replace(",", ".").astype(float)/100
goals_df['% of Goals Scored'] = goals_df['% of Goals Scored'].astype(str).str.replace(",", ".").astype(float)
goals_df['% of Goals Conceded'] = goals_df['% of Goals Conceded'].astype(str).str.replace(",", ".").astype(float)
goals_df['Average Goals Scored'] = goals_df['Average Goals Scored'].astype(str).str.replace(",", ".").astype(float)/100
goals_df['Average Goals Conceded'] = goals_df['Average Goals Conceded'].astype(str).str.replace(",", ".").astype(float)/100

# Layout of the Dash app
layout = dbc.Container([
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='combo-chart')
                ], xs=12, sm=12, md=12, lg=6, xl=6, className="mb-4"),
            dbc.Col([
                dcc.Dropdown(
                id='season-dropdown',
                options=[{'label': season, 'value': season} for season in sorted(goals_df['Season'].unique())],
                value="2025 - 2026",
                multi=False,
                placeholder="Season",
                style={
                    "background-color": "transparent",
                    "color": "black",
                    "font-weight": "bold",
                    "width": "50%",
                    },
                className="mb-3"
                ),
        dbc.Row([
            dbc.Col([
                dbc.RadioItems(
                    id='time-toggle',
                    options=[
                        {"label": "Halves", "value": "Half"},
                        {"label": "Minutes", "value": "Minutes"}
                        ],
                    value="Half",
                    labelStyle={'display': 'inline-block', 'margin-right': '15px'},
                    inline=True
                    ),
            ], width=4),
            dbc.Col([
                dbc.RadioItems(
                    id='avg-toggle',
                    options=[
                        {"label": "Average Goals Scored", "value": "Average Goals Scored"},
                        {"label": "Average Goals Conceded", "value": "Average Goals Conceded"}
                        ],
                    value="Average Goals Scored",
                    labelStyle={'display': 'inline-block', 'margin-right': '15px'},
                    inline=True
                    ), 
            ], width=4),
            dbc.Col([
                dbc.RadioItems(
                    id='percent-toggle',
                    options=[
                        {"label": "% of Goals Scored", "value": "% of Goals Scored"},
                        {"label": "% of Goals Conceded", "value": "% of Goals Conceded"}
                        ],
                    value="% of Goals Scored",
                    labelStyle={'display': 'inline-block', 'margin-right': '15px'},
                    inline=True
                    ),
            ], width=4),
        ], justify="center", className="mb-4"),           

                dash_table.DataTable(
                    id='goals-table',
                    style_table={'overflowX': 'auto'},
                    style_cell={'backgroundColor': 'rgb(0, 43, 54)', 'color': 'white', 'fontWeight': 'bold', 'textAlign': 'center', },
                    style_header={
                        'backgroundColor': 'rgb(0, 43, 54)',
                        'color': 'white',
                        'fontWeight': 'bold',
                        'textAlign': 'center',
                        "whiteSpace": "normal",
                        },
                    page_size=10,
                    tooltip_delay=0, 
                    tooltip_duration=4000, 
                    tooltip={
                    '% of Goals Scored': 'Only Goals Scored and Conceded from League and Cup matches have been taken into account.',
                    '% of Goals Conceded': 'Only Goals Scored and Conceded from League and Cup matches have been taken into account.',
                    'Average Goals Scored': 'Only Goals Scored and Conceded from League and Cup matches have been taken into account.',
                    'Average Goals Conceded': 'Only Goals Scored and Conceded from League and Cup matches have been taken into account.',
                    'type': 'markdown',
                    'use_with': 'both',  # both refers to header & data cell
                    }
                    )
                    ], xs=12, sm=12, md=12, lg=6, xl=6),
                    ]),

        dbc.Row([
            dbc.Col([
                dcc.Graph(id='avg-line-chart')
                ], xs=12, sm=12, md=12, lg=6, xl=6),
                ]),
], fluid=True)

# Callback to update the charts and the table based on the filters and the toggles
@callback(
    Output('combo-chart', 'figure'),
    Output('avg-line-chart', 'figure'),
    Output('goals-table', 'data'),
    Output('goals-table', 'columns'),
    Input('season-dropdown', 'value'),
    Input('time-toggle', 'value'),
    Input('avg-toggle', 'value'),
    Input('percent-toggle', 'value')
)

def update_dashboard(season, time_col, avg_metric, percent_metric):

    # Combo chart
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        x=chart_prep_df['Season'],
        y=chart_prep_df['Goals Scored'],
        name='Goals Scored',
        marker=dict(color="rgb(0, 123, 164)", line=dict(width=0)),
        #marker_color="rgb(0, 123, 164)",
        text=chart_prep_df['Goals Scored'],
        textposition="auto",
        textfont=dict(color="white", size=14, family="Arial")
    ))

    fig1.add_trace(go.Bar(
        x=chart_prep_df['Season'],
        y=[-x for x in chart_prep_df['Goals Conceded']],
        name='Goals Conceded',
        marker=dict(color="rgb(228, 155, 88)", line=dict(width=0)),
        #marker_color="rgb(228, 155, 88)",
        text=chart_prep_df['Goals Conceded'],
        textposition="auto",
        textfont=dict(color="white", size=14, family="Arial")
    ))

    fig1.add_trace(go.Scatter(
        x=chart_prep_df['Season'],
        y=chart_prep_df['Goals Difference'],
        name='Goals Difference',
        mode='lines+markers+text',
        text=chart_prep_df['Goals Difference'],
        textposition='top center',
        textfont=dict(color="white", size=14, family="Arial"),
        marker=dict(color="rgb(228, 99, 88)")
    ))

    # Update layout
    fig1.update_layout(
        autosize=True,
        height=None,  # Let container decide
        hovermode=False,  # Disable hover tooltip
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(
            showline=False,
            showgrid=False,
            tickmode="array",
            tickvals=chart_prep_df["Season"],
            ticktext=chart_prep_df["Season"],  # Display season labels
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
        ),
        barmode='relative'
    )

    # Line chart for averages
    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(
        x=chart_prep_df['Season'], y=chart_prep_df['Average Goals Scored per Match'],
        mode='lines+markers+text', name='Average Goals Scored', line=dict(color="rgb(0, 123, 164)", width=2), text=chart_prep_df['Average Goals Scored per Match'], textposition="top center", textfont=dict(color="white", size=14, family="Arial")
    ))

    fig2.add_trace(go.Scatter(
        x=chart_prep_df['Season'], y=chart_prep_df['Average Goals Conceded per Match'],
        mode='lines+markers+text', name='Average Goals Conceded', line=dict(color="rgb(228, 155, 88)", width=2), text=chart_prep_df['Average Goals Conceded per Match'], textposition="top center", textfont=dict(color="white", size=14, family="Arial")
    ))

    # Update layout to remove outer border lines and y-axis
    fig2.update_layout(
        autosize=True,
        height=None,  # Let container decide
        hovermode=False,  # Disable hover tooltip
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(
            showline=False,
            showgrid=False,
            tickmode="array",
            tickvals=chart_prep_df["Season"],
            ticktext=chart_prep_df["Season"],  # Display season labels
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

    # Table data preparation
    # Apply filters for Season
    if season:
        if isinstance(season, str): # Ensure selected_seasons is treated as a list for filtering
            season = [season]
        filtered = goals_df[goals_df["Season"].isin(season)] # Filter dataframe based on selected seasons
    table_data = filtered.groupby(time_col).agg({
        avg_metric: 'mean',
        percent_metric: 'sum'
    }).reset_index()

    table_data[avg_metric] = table_data[avg_metric].round(2)
    table_data[percent_metric] = table_data[percent_metric].map(lambda x: f"{x:.0f}%")
    columns = [
        {'name': time_col, 'id': time_col},
        {'name': avg_metric, 'id': avg_metric},
        {'name': percent_metric, 'id': percent_metric}
    ]

    return fig1, fig2, table_data.to_dict('records'), columns
