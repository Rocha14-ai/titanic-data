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


grp= df.groupby("Survived")

for grp_name, grp_data in grp:
  ax.hist(grp_data["Survived"], bins=2)

ax.set_title('Survivors')
ax.set_xlabel("0 no sobrevivientes, 1 sobrevivientes")
ax.legend()
st.pyplot(fig)
