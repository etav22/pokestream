"""The types page of the Pokestream app compares the stats of different pokemon types."""
import streamlit as st

from app import df_pokemon
from pokestream.components import create_violin_plot

st.markdown("# Pokemon Stats Across Types")

# Create violin plot with selector for every stat but name and type
display_stats = [stat for stat in df_pokemon.columns if stat not in ["Name", "Type1", "Type2"]]
stat = st.selectbox("Stat", display_stats)

violin = create_violin_plot(df_pokemon, stat)
st.plotly_chart(violin, use_container_width=True)
