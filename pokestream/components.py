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
    pokemon_stats: dict,
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
