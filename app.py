import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("""
HOLA MUNDO
hola hola hola
""")
st.header("holi")
st.markdown("*juan*")

df = pd.read_csv('train.csv')
st.dataframe(df)


option = st.selectbox(
    'Elije de la columna',
    ('Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'))

st.write('You selected:', option)

arr = df['Survived']
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)


