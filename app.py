"""
# My first app
Here's our first attempt at using data to create a table:
"""
import streamlit as st
import pandas as pd
from pokestream.core import get_pokemon

# Read in the original datset
df_pokemon = pd.read_csv('./data/PokemonStats.csv')

# Add a selectbox to the sidebar:
pokemon: str = st.sidebar.selectbox(
    'Choose your pokemon!',
    df_pokemon['Name'].unique()
)

# Query the API for the selected pokemon
pokemon_json = get_pokemon(pokemon.lower())

if pokemon_json:
    # Header takes on the value of the selectbox
    st.header(pokemon)
    st.sidebar.image(pokemon_json['sprites']['front_default'], width=300)


    st.write("Here's our first attempt at using data to create a table:")
    if st.checkbox('Show dataframe'):
        st.write(pd.read_csv('./data/PokemonStats.csv'))
else:
    st.error('Pokemon not found.')
