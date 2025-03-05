
# Importation des bibliothèques de base nécessaires
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np  # Importer NumPy

df = pd.read_csv('MathE dataset(4).csv', delimiter=";" encoding='cp1252')
# Afficher les premières lignes du jeu de données
print(df.head())

# Statistiques descriptives pour comprendre la distribution des caractéristiques
print(df.describe())

# Visualisation de la répartition des classes
sns.countplot(x='Species', data=df)
plt.title('Distribution des espèces d\'iris')
plt.show()

effectifs=df['Species'].value_counts()
print(effectifs)
