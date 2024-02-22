import streamlit as st
import pandas as pd
import numpy as np

st.title("""
HOLA MUNDO
hola hola hola
""")
st.header("holi")
st.markdown("*juan*")

df = pd.read_csv('train.csv')
st.dataframe(df)

chart_data = pd.DataFrame(df["Survived"], columns=["a"])

st.bar_chart(chart_data)

