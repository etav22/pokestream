"""Main page that displays the pokedex information for a selected pokemon."""
import pandas as pd
import streamlit as st
from st_pages import show_pages_from_config

import pokestream.components as pc
from pokestream.core import get_pokemon

show_pages_from_config()

# Read in the original datset
df_pokemon = pd.read_csv("./data/PokemonStats.csv", index_col=0)

# Add a selectbox to the sidebar:
st.sidebar.markdown("# Gotta Catch 'Em All!")
pokemon: str = st.sidebar.selectbox("Choose your pokemon!", df_pokemon["Name"].unique())

# Query the API for the selected pokemon
pokemon_json = get_pokemon(pokemon.lower())

if pokemon_json:
    # Get the pokemon's row from the original dataset
    pokemon_choose_df = df_pokemon[df_pokemon["Name"] == pokemon]
    pokemon_stats = pokemon_choose_df.to_dict("records")[0]

    # ==== Sidebar ====
    with st.sidebar:
        # Pokemon's Sprite
        sprite = st.radio("Pokemon Sprite", ["Base", "Shiny"], index=0)
        if sprite == "Base":
            st.image(pokemon_json["sprites"]["front_default"], width=300)
        else:
            st.image(pokemon_json["sprites"]["front_shiny"], width=300)

    # ==== Main page ====
    st.markdown(f"# {pokemon} {pc.POKEMOJI[pokemon_stats['Type1']]}")
    st.write(f"Here are some stats on {pokemon}!")

    #! Need to add more general descriptors of pokemon (e.g. both types, height, weight, evolutions etc.)

    # Display the pokemon's stats
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    cols = [c1, c2, c3, c4, c5, c6, c7]
    display_stats = [stat for stat in pokemon_stats if stat not in ["Name", "Type1", "Type2", "Height", "Weight"]]
    for i, stat in enumerate(display_stats):
        delta = int(pokemon_stats[stat] - df_pokemon[stat].mean())
        cols[i].metric(label=stat, value=pokemon_stats[stat], delta=delta)
    st.write("*Delta is compared to average of all pokemon*")

    # Create plotly polar plot
    scatterpolar = pc.create_scatter_polar(pokemon_stats, display_stats)
    st.plotly_chart(scatterpolar, use_container_width=True)

    # ==== Comparison page ====
    st.write("---")
    st.markdown("### Compare to other pokemon!")

    # Create plotly distribution plots
    chosen_stat = st.selectbox("Stat", display_stats, index=0)
    bin_step = st.slider("Bin Range", min_value=1, max_value=50, value=10, step=1)
    stat_fig = pc.create_histogram(df_pokemon, pokemon_stats, chosen_stat, bin_size=bin_step)
    st.plotly_chart(stat_fig, use_container_width=True)

    # Create scatterplot
    c1, c2 = st.columns(2)
    stat_1 = c1.selectbox("Stat 1", display_stats, index=0)
    stat_2 = c2.selectbox("Stat 2", display_stats, index=1)
    scatter_fig = pc.create_scatter_compare(df_pokemon, pokemon_stats, stat_1, stat_2)
    st.plotly_chart(scatter_fig, use_container_width=True)
else:
    st.error("Pokemon not found.")
