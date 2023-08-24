from typing import Any, Dict

import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st

POKEMOJI = {
    "Normal": "😐",
    "Fire": "🔥",
    "Water": "💧",
    "Electric": "⚡",
    "Grass": "🌿",
    "Ice": "🧊",
    "Fighting": "🥊",
    "Poison": "☠️",
    "Ground": "🌍",
    "Flying": "🦅",
    "Psychic": "🧠",
    "Bug": "🐛",
    "Rock": "🪨",
    "Ghost": "👻",
    "Dragon": "🐉",
    "Dark": "🌑",
    "Steel": "⚙️",
    "Fairy": "🧚",
}

POKECOLOR = {
    "Normal": "#A8A77A",
    "Fire": "#EE8130",
    "Water": "#6390F0",
    "Electric": "#F7D02C",
    "Grass": "#7AC74C",
    "Ice": "#96D9D6",
    "Fighting": "#C22E28",
    "Poison": "#A33EA1",
    "Ground": "#E2BF65",
    "Flying": "#A98FF3",
    "Psychic": "#F95587",
    "Bug": "#A6B91A",
    "Rock": "#B6A136",
    "Ghost": "#735797",
    "Dragon": "#6F35FC",
    "Dark": "#705746",
    "Steel": "#B7B7CE",
    "Fairy": "#D685AD",
}


def create_histogram(
    df_pokemon: pd.DataFrame,
    pokemon_stats: Dict[str, Any],
    stat: str,
    bin_size: int = 10,
) -> go.Histogram | None:
    """Create a histogram of the given stat.

    Args:
    ----
        df_pokemon (pd.DataFrame): Entire pokemon dataset.
        pokemon_stats (dict): Stats of the selected pokemon.
        stat (str): Stat to create histogram of.
        bin_size (int, optional): Bin size of the graph. Defaults to 10.

    Returns:
    -------
        go.Histogram | None : Plotly histogram.
    """
    # Check if stat is in the dataset
    if stat not in df_pokemon.columns:
        st.error(f"{stat} not found in dataset.")
        return None

    fig = ff.create_distplot(
        hist_data=[df_pokemon[stat]],
        group_labels=[stat],
        bin_size=bin_size,
        colors=[POKECOLOR[pokemon_stats["Type1"]]],
        show_rug=True,
    )
    fig.update(layout_title_text=f"{stat} Distribution")
    fig.add_vline(
        x=pokemon_stats[stat],
        line_width=1,
        line_dash="dot",
        line_color="red",
        annotation={"text": "Current Pokemon", "font": {"color": "red"}},
    )

    return fig


def create_scatter_compare(
    df_pokemon: pd.DataFrame,
    pokemon_stats: Dict[str, Any],
    stat_1: str,
    stat_2: str,
) -> go.Figure | None:
    """Create a scatterplot comparing two of the pokemon's stats.

    Args:
    ----
        df_pokemon (pd.DataFrame): Entire pokemon dataset.
        pokemon_stats (dict): Stats of the selected pokemon.
        stat_1 (str): First stat to compare.
        stat_2 (str): Second stat to compare.

    Returns:
    -------
        go.Figure | None: Plotly scatterplot.
    """
    if (stat_1 not in df_pokemon.columns) or (stat_2 not in df_pokemon.columns):
        st.error(f"{stat_1} or {stat_2} not found in dataset.")
        return None

    fig = go.Figure()

    # Create scatterplot of all pokemon
    fig.add_trace(
        go.Scatter(
            x=df_pokemon[stat_1],
            y=df_pokemon[stat_2],
            mode="markers",
            marker={"color": POKECOLOR[pokemon_stats["Type1"]]},
            name="All Pokemon",
            hovertemplate=df_pokemon["Name"],
        ),
    )
    # Create point for current pokemon
    fig.add_trace(
        go.Scatter(
            x=[pokemon_stats[stat_1]],
            y=[pokemon_stats[stat_2]],
            mode="markers",
            marker={"color": "red"},
            name="Current Pokemon",
        ),
    )

    fig.update_layout(
        title=f"{stat_1} vs {stat_2}",
        xaxis_title=f"{stat_1}",
        yaxis_title=f"{stat_2}",
    )

    return fig
