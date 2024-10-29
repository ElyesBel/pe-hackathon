# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.read_excel('data_bonheur.xls')


# %%
df.head()

# %%
df.dtypes

# %% jupyter={"outputs_hidden": true}
df_fr=df[df['Country name']=='France']
df_fr
df_fr.set_index('year')

# %% jupyter={"outputs_hidden": true}
critere= df_fr.columns[2:]
critere

# %% jupyter={"outputs_hidden": true}
for c in critere:
    plt.scatter(df_fr['year'], df_fr[c], color='pink')
    plt.title(f"Évolution de {c} en France")
    plt.xlabel("Année")
    plt.ylabel(f"Valeur de l'indice du {c}")
    plt.legend()
    plt.show()

# %% [markdown]
# On a tracé l'évolution de chaque critère qui pourrait participer à l'évaluation du bonheur en France, au fil des années, de 2005 à 2022. On remarque que l'espérance de vie a augmenté de façon très linéaire, la perception de la corruption a diminué, mais les autres critères ont des valeurs qui varient aléatoirement au cours des années autour d'une valeur moyenne.

# %% [markdown]
# Regardons maintenant si les valeurs des colonnes, pour la France, sont corrélées. On utilise pour cela la méthode corr() de pandas:
#

# %% jupyter={"outputs_hidden": true}
import seaborn as sns

matrice_correlation = df_fr[critere].corr()

print(matrice_correlation)

plt.figure(figsize=(10, 8))
sns.heatmap(matrice_correlation , annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title("Corrélation des critères d'évaluation du bonehur français")
plt.show()


# %%
df_2022=df[df['year']==2022]
df_2022.set_index('Country name')
crit=df_2022.columns[2:]

# %%
print(df_2022['Country name'].shape)
print(df_2022[crit].shape)
crit

# %%
for c in crit :
    plt.figure(figsize=(110, 30))
    plt.bar(df_2022['Country name'], df_2022[c])
    plt.xlabel('Pays', fontsize=50)
    plt.ylabel(f'Valeur du {c}', fontsize=50)
    plt.title(f'Histogramme de la valeur du {c} par pays', fontsize=60)
    plt.show()

# %%

# %%
