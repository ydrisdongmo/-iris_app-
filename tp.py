import streamlit as st 
# Importation des bibliothèques de base nécessaires
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('MathE dataset(4).csv', delimiter=";" encodage"c1252")
# Statistiques descriptives pour comprendre la distribution des 
# caractéristiques
print(df.head())
print(df.describe())
#comment
# Visualisation de la répartition des classes
sns.countplot(x='Species', data=df)
