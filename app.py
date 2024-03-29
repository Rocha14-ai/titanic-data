import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("""
TITANIC
Este es un dataset del titanic 
""")

df = pd.read_csv('train.csv')
st.write('Introduce el PassengerId o usa 0 para ver a todos')
number = int(st.number_input("Insert a number", value=None, placeholder="Type a number..."))

if number is not None:
    st.write('The current index is ', number)
    number1 = int(number) - 1

    def tabla(number=1):
        if number == 0:
            def highlight_survived_row(row):
                color = 'green' if row['Survived'] == 1 else 'red'
                return [f'background-color: {color}'] * len(row)

            styled_df = df.style.apply(highlight_survived_row, axis=1)

            st.dataframe(styled_df)
        else:
            st.dataframe(df.iloc[number1:number])

    tabla(number)
else:
    st.write('Please enter a number')


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

    return st.pyplot(fig)



his(option)


