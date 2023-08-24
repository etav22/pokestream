import pandas as pd
import streamlit as st

from pokestream.components import POKEMOJI, create_histogram
from pokestream.core import get_pokemon

# Read in the original datset
df_pokemon = pd.read_csv("./data/PokemonStats.csv", index_col=0)

# Add a selectbox to the sidebar:
pokemon: str = st.sidebar.selectbox("Choose your pokemon!", df_pokemon["Name"].unique())

# Query the API for the selected pokemon
pokemon_json = get_pokemon(pokemon.lower())

if pokemon_json:
    # Get the pokemon's row from the original dataset
    pokemon_choose_df = df_pokemon[df_pokemon["Name"] == pokemon]
    pokemon_stats = pokemon_choose_df.to_dict("records")[0]

    # Header takes on the value of the selectbox
    st.header(pokemon)
    st.sidebar.image(pokemon_json["sprites"]["front_default"], width=300)

    # Write out the pokemon's type
    type_1 = POKEMOJI[pokemon_stats["Type1"]]
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        f"<h2 style='text-align: center';'>Type: {type_1} {pokemon_stats['Type1']} </h2>",
        unsafe_allow_html=True,
    )
    try:
        type_2 = POKEMOJI[pokemon_stats["Type2"]]
        st.sidebar.markdown(
            f"<h2 style='text-align: center';'>Type 2: {type_2} {pokemon_stats['Type2']} </h2>",
            unsafe_allow_html=True,
        )
    except KeyError:
        pass

    st.write(f"Here are some stats on {pokemon}!")

    # Display the pokemon's stats
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    cols = [c1, c2, c3, c4, c5, c6, c7]
    display_stats = [stat for stat in pokemon_stats if stat not in ["Name", "Type1", "Type2", "Height", "Weight"]]
    for i, stat in enumerate(display_stats):
        delta = int(pokemon_stats[stat] - df_pokemon[stat].mean())
        cols[i].metric(label=stat, value=pokemon_stats[stat], delta=delta)
    st.write("*Delta is compared to average of all pokemon*")
    st.write("---")

    # Create plotly distribution graph
    fig_dict = {}
    for stat in display_stats:
        fig_dict[stat] = create_histogram(df_pokemon, pokemon_stats, stat)

    # Create plotly scatter plots
    chosen_stat = st.selectbox("Stat", display_stats, index=0)
    bin_step = st.slider("Bin Range", min_value=1, max_value=50, value=10, step=1)
    stat_fig = create_histogram(df_pokemon, pokemon_stats, chosen_stat, bin_size=bin_step)
    st.plotly_chart(stat_fig, use_container_width=True)
else:
    st.error("Pokemon not found.")
