import streamlit as st
import pandas as pd
import numpy as np

st.header("Jazkay Magbanua Caingles")

st.write("Welcome to my first Streamlit app!")

name = st.text_input("What's your name?")
if name:
    st.success(f"Hello, {name}!")

st.subheader("Sample Data")
df = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.dataframe(df)
st.line_chart(df)

num = st.slider("Pick a number", 0, 100, 25)
st.write("You picked:", num)