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


chart_data = pd.DataFrame(
   {
       "col1": df["Survivors"]

   }
)

st.bar_chart(chart_data, x="col1")

grp= df.groupby("Survived")
fig, ax = plt.subplots(figsize(8,6))
for grp_name, grp_data in grp:
  ax.hist(grp_data["Survived"], bins=2)

ax.set_title('Survivors')
ax.set_xlabel("0 no sobrevivientes, 1 sobrevivientes")
ax.legend()
st.pyplot(fig)

