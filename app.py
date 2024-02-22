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

df['Pclass'].plot(kind='hist')
