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

chart_data = pd.DataFrame(df, columns=["Survived"])

st.bar_chart(chart_data)

arr = df['Survived']
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)


