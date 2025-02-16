import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger le jeu de données Iris
df = sns.load_dataset('iris')

# Titre de l'application
st.title("SPREMIERE TP DE IA")
st.write("Hello world!")

# Afficher les statistiques descriptives
st.write(df.describe())

# Visualisation de la répartition des classes
plt.figure(figsize=(10, 6))
sns.countplot(x='species', data=df)  # Correction du nom de la colonne
plt.title('Distribution des espèces d\'iris')
st.pyplot()  # Affichage du graphique avec Streamlit
