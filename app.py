import pandas as pd
import streamlit as st

from pokestream.components import create_histogram
from pokestream.core import get_pokemon

# Read in the original datset
df_pokemon = pd.read_csv("./data/PokemonStats.csv", index_col=0)

# Add a selectbox to the sidebar:
pokemon: str = st.sidebar.selectbox("Choose your pokemon!", df_pokemon["Name"].unique())
# Query the API for the selected pokemon
pokemon_json = get_pokemon(pokemon.lower())

if pokemon_json:
    # Header takes on the value of the selectbox
    st.header(pokemon)
    st.sidebar.image(pokemon_json["sprites"]["front_default"], width=300)

    # Get the pokemon's row from the original dataset
    pokemon_choose_df = df_pokemon[df_pokemon["Name"] == pokemon]
    pokemon_stats = pokemon_choose_df.to_dict("records")[0]

    st.write(f"Here are some stats on {pokemon}!")

    # Display the pokemon's stats
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    cols = [c1, c2, c3, c4, c5, c6, c7]
    display_stats = [stat for stat in pokemon_stats if stat not in ["Name", "Type1", "Type2", "Height", "Weight"]]
    for i, stat in enumerate(display_stats):
        cols[i].metric(label=stat, value=pokemon_stats[stat])

    # Create plotly distribution graph
    fig_dict = {}
    for stat in display_stats:
        fig_dict[stat] = create_histogram(df_pokemon, pokemon_stats, stat)

    # Create plotly scatter plots
    st.plotly_chart(fig_dict["Total"], use_container_width=True)
    st.plotly_chart(fig_dict["HP"], use_container_width=True)
    st.plotly_chart(fig_dict["Attack"], use_container_width=True)
    st.plotly_chart(fig_dict["Defense"], use_container_width=True)
    st.plotly_chart(fig_dict["SpAtk"], use_container_width=True)
    st.plotly_chart(fig_dict["SpDef"], use_container_width=True)
    st.plotly_chart(fig_dict["Speed"], use_container_width=True)


else:
    st.error("Pokemon not found.")
