"""
# My first app
Here's our first attempt at using data to create a table:
"""
import streamlit as st
import pandas as pd
from pokestream.core import get_pokemon
from loguru import logger

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
    st.sidebar.subheader(f'Type 1: {pokemon_stats["Type1"]}')
    if df_pokemon["Type2"] is None:
        st.sidebar.subheader(f'Type 2: {pokemon_stats["Type2"]}')

    st.write(f"Here are some stats on {pokemon}!")
    if st.checkbox("Show dataframe"):
        st.write(pokemon_choose_df)
        logger.info(pokemon_choose_df)
else:
    st.error("Pokemon not found.")
