import streamlit as st
import pandas as pd

data_cache = st.cache(pd.read_csv)

data = data_cache("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")

species_label = st.selectbox("Select specie:",data.species.unique())

st.write(data[data.species==species_label])