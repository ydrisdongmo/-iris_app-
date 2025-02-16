import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger le jeu de données Iris
df = sns.load_dataset('iris')

# Titre de l'application
st.title("PREMIER TP SUR L'INTELLIGENCE ARTIFICIELLE")
st.write("Hello world!")

# Afficher les statistiques descriptives
st.write(df.describe())

# Visualisation de la répartition des classes
fig, ax = plt.subplots(figsize=(10, 6))  # Créer une figure et un axe
sns.countplot(x='species', data=df, ax=ax)  # Tracer sur l'axe spécifié
ax.set_title('Distribution des espèces d\'iris')  # Définir le titre

# Affichage du graphique avec Streamlit
st.pyplot(fig)
