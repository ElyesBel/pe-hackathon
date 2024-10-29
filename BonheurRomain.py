# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Bonheur.xls')
df1 = df[df['year'] == 2022]
df1



# +
df1.plot(kind='scatter', x='Log GDP per capita', y='Generosity', alpha=0.6, figsize=(10, 6))

# Titre et affichage
plt.title('Nuage de points : Generosity vs Log GDP per capita')
plt.show()
# -

on ne remarque pas de corrélation entre la générosité et le GDP

# +
df1.plot(kind='scatter', x='Log GDP per capita', y='Life Ladder', alpha=0.6, figsize=(10, 6))

# Titre et affichage
plt.title('Nuage de points : Life Ladder vs Log GDP per capita')
plt.show()

# +
## l'indice de Life Ladder semble linéairement corrélé au GDP

# +
df1.plot(kind='scatter', x='Log GDP per capita', y='Healthy life expectancy at birth', alpha=0.6, figsize=(10, 6))

# Titre et affichage
plt.title('Nuage de points : Healthy life expectancy at birth vs Log GDP per capita')
plt.show()

# +
## L'espérance de vie en bonne santé est aussi corrélé au GDP
# -

df2 = df.groupby('year')['Healthy life expectancy at birth'].mean()
df3 = df.groupby('year')['Life Ladder'].mean()
df4 = df.groupby('year')['Perceptions of corruption'].mean()






# +
# Tracer le graphique
df2.plot(x='year', y='Healthy life expectancy at birth', kind='line', marker='o', figsize=(10, 6))

# Ajouter un titre et des labels
plt.title('Esperance de vie en bonne santé par Année')
plt.xlabel('Year')
plt.ylabel('Healthy life expectancy at birth')
plt.grid(True)
plt.show()

# +
# Tracer le graphique
df3.plot(x='year', y='Life Ladder', kind='line', marker='o', figsize=(10, 6))

# Ajouter un titre et des labels
plt.title('Life Ladder par Année')
plt.xlabel('Year')
plt.ylabel('Life Ladder')
plt.grid(True)
plt.show()

# +
# Tracer le graphique
df4.plot(x='year', y='Perceptions of corruption', kind='line', marker='o', figsize=(10, 6))

# Ajouter un titre et des labels
plt.title('Perceptions of corruption par Année')
plt.xlabel('Year')
plt.ylabel('Perceptions of corruption')
plt.grid(True)
plt.show()
# -










