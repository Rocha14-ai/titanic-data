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

chart_data = pd.df(columns=["Survived"])

st.bar_chart(x=chart_data)
