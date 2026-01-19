import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px
from data_loader import load_all_players

# Initialize the Dash app
dash.register_page(__name__, path='/top', name="The Top")

df = load_all_players()

# Convert "Weighted Score per Match" from comma-separated to dot-separated floats
df['Weighted Score per Match'] = df['Weighted Score per Match'].astype(str).str.replace(",", ".").astype(float)/100
df['Goals Scored per Match'] = df['Goals Scored per Match'].astype(str).str.replace(",", ".").astype(float)/100
df['Assists per Match'] = df['Assists per Match'].astype(str).str.replace(",", ".").astype(float)/100
df['Goals Conceded per Match'] = df['Goals Conceded per Match'].astype(str).str.replace(",", ".").astype(float)/100

# Layout of the Dash app
layout = html.Div(
    style={"background-color": "transparent", "font-family": "Arial, sans-serif", "padding": "20px", "color": "white"},
    children=[
        # Dropdown filter for metric
        html.Div(
            style={"margin-bottom": "20px", "display": "flex", "justify-content": "center"},
            children=[
                dcc.Dropdown(
                    id="metric-filter",
                    options=[
                        {"label": "Appearences", "value": "Appearences"},
                        {"label": "Goals Scored", "value": "Goals Scored"},
                        {"label": "Assists", "value": "Assists"},
                        {"label": "Goals Conceded", "value": "Goals Conceded"},
                        {"label": "Goals Scored per Match", "value": "Goals Scored per Match"},
                        {"label": "Assists per Match", "value": "Assists per Match"},
                        {"label": "Goals Conceded per Match", "value": "Goals Conceded per Match"},
                        {"label": "Weighted Score per Match", "value": "Weighted Score per Match"},
                    ],
                    placeholder="Metric",
                    value="Appearences",
                    style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "50%",
                    },
                ),

                 dcc.Dropdown(
                    id="season-filter",
                    options=[
                        {"label": season, "value": season} for season in sorted(df["Season"].unique()) if season != ""
                    ],
                    placeholder="Season",
                    value="2025 - 2026",
                    style={
                        "background-color": "transparent",
                        "color": "black",
                        "font-weight": "bold",
                        "width": "45%",
                    },
                ),
            ],
        ),

        html.Div(
            dcc.Graph(id="bar-chart"),
        style={
                "width": "80%",  # Limit the graph to 80% of the page width
                "margin": "0 auto",  # Center the graph horizontally
            },
        ),
    ],
)

# Callback to update the bar chart based on selected metric
@callback(
    Output("bar-chart", "figure"),
    [Input("metric-filter", "value"),Input("season-filter", "value")],
)

def update_chart(selected_metric, selected_season):

    if not selected_metric or not selected_season:
        return px.bar(title="Please select both a metric and a season")

    # Filter the DataFrame based on the selected season
    filtered_df = df[df["Season"] == selected_season]

     # Filter out zero values
    non_zero_df = filtered_df[filtered_df[selected_metric] > 0]

    # Decide whether to take top or bottom 5
    if selected_metric in ["Goals Conceded", "Goals Conceded per Match"]:

        # Defensive metrics → bottom 5, sort ascending
        subset = non_zero_df.nsmallest(5, selected_metric)
        cutoff_value = subset[selected_metric].max()
        final_df = non_zero_df[non_zero_df[selected_metric] <= cutoff_value].sort_values(
            by=selected_metric, ascending=False
        ) # Include ties (ensures all players tied for cutoff are included)

    else:
        # Offensive metrics → top 5, sort descending
        subset = non_zero_df.nlargest(5, selected_metric)
        cutoff_value = subset[selected_metric].min()
        final_df = non_zero_df[non_zero_df[selected_metric] >= cutoff_value].sort_values(
            by=selected_metric, ascending=True
        )

    # Set formatting for text template based on the selected metric
    if (selected_metric == "Weighted Score per Match" or selected_metric == "Goals Conceded per Match" or selected_metric == "Assists per Match" or selected_metric == "Goals Scored per Match"):
        text_template = "%{text:.2f}"  # 2 decimal places
    else:
        text_template = "%{text:.0f}"  # Whole numbers

    # Create the bar chart
    fig = px.bar(
        final_df,
        x=selected_metric,
        y="Player Name",
        orientation="h",
        title=f"Top Players by {selected_metric} in {selected_season}",
        text=selected_metric,  # Add value labels
    )

    # Update colors with gradient
    fig.update_traces(
        marker=dict(
            color=final_df[selected_metric],
            colorscale=[
                [0, "rgba(228, 155, 88, 0.4)"],
                [1, "rgba(228, 155, 88, 1)"],
            ],
            line=dict(color="rgba(0, 0, 0, 0.2)", width=1),
        ),

        texttemplate=text_template,  # Apply formatting
        textposition="outside",  # Place labels outside the bars
        textfont=dict(size=16, color="white"),  # Set text font color to white
        hovertemplate=(
            f"<span style='font-size:14px; font-weight:bold; color:black;'>%{{y}}</span><br>"
            f"<span style='font-size:12px; font-weight:bold; color:black;'>"
            f"{selected_metric}: %{{x}}</span>"
        ),
    )

    # Update layout
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(visible=False),
        yaxis=dict(
            showgrid=False,
            showticklabels=True,  # Keep the ticks but remove the label
            title=None,  # Remove y-axis title
            tickfont=dict(size=16, color="white"),
        ),
        margin=dict(l=0, r=0, t=40, b=20),
        title=dict(
            text=f"<b>Top Players by {selected_metric} in {selected_season}</b>",
            font=dict(color="white"),
            x=0.5,
        ),
        hoverlabel=dict(
            bgcolor="white",
            font=dict(color="black", family="Arial"),
            bordercolor="lightgray"
        ),
    )

    return fig
