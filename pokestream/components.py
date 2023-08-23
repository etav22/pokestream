import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st


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

    fig = ff.create_distplot(hist_data=[df_pokemon[stat]], group_labels=[stat], bin_size=bin_size, show_rug=True)
    fig.update(layout_title_text=f"{stat} Distribution")
    fig.add_vline(x=pokemon_stats[stat], line_width=1, line_dash="dot", line_color="red")

    return fig
