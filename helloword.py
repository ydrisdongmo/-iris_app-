import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.title('PREMIERE TP DE IA ')
st.write("hello word!")
print(df.describe())
# Visualisation de la répartition des classes
sns.countplot(x='species', data=df)
plt.title('Distribution des espèces d\'iris')
plt.show()
