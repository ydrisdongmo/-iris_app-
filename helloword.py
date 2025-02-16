import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('iris')
st.title("SPREMIERE TP DE IA ")
st.write("hello word!")
print(df.describe())
# Visualisation de la répartition des classes
sns.countplot(x='Species', data=df)
plt.title('Distribution des espèces d\'iris')
plt.show()
