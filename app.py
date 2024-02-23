import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("""
TITANIC
Este es un dataset del titanic 
""")

df = pd.read_csv('train.csv')
st.dataframe(df)


option = st.selectbox(
    'Elije de la columna',
    ('Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'))

st.write('You selected:', option)

def his(option):
    if option == 'Embarked':
        embarked_mapping = {'S': 0, 'C': 1, 'Q': 2} 
        df['Embarked'] = df['Embarked'].map(embarked_mapping)


        df.dropna(subset=['Embarked'], inplace=True)


        arr = df['Embarked']


        fig, ax = plt.subplots()
        ax.hist(arr, bins=20)
        print("S: 0, C: 1, Q: 2")

    else:
        arr = df[option]
        fig, ax = plt.subplots()
        ax.hist(arr, bins=20)

    return st.pyplot(fig), max(arr), min(arr)


his(option)
