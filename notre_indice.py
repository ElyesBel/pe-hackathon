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
a= df['Healthy life expectancy at birth'].max()
df['healthy life exp norm']= df['Healthy life expectancy at birth']/a
b= df['Life Ladder'].max()
df['life ladder norm']= df['Life Ladder']/b
df['non_corru']= 1-df['Perceptions of corruption']
df['notre indice du bonheur'] = (
    0.3 * df['healthy life exp norm'] +
    0.3 * df['life ladder norm'] +
    0.3 * df['Freedom to make life choices'] +
    0.1 * df['non_corru']
)


# %% [markdown]
# Indice du bonheur en 2022 pour chaque pays

# %%
df_22 = df[df['year']==2022]
plt.figure(figsize=(150, 30))
plt.bar(df_22['Country name'],df_22['notre indice du bonheur'])
plt.xlabel('Pays', fontsize=50)
plt.ylabel('indice du bonheur', fontsize=50)
plt.title("Histogramme de la valeur de l'indice du bonheur par pays", fontsize=60)
plt.show()

# %% [markdown]
# Évolution de l'indice du bonheur pour quelques pays:

# %%
df_fr=df[df['Country name']=='France']
df_afg=df[df['Country name']=='Afghanistan']
df_br=df[df['Country name']=='Brazil']
df_sl=df[df['Country name']=='Sierra Leone']
df_us=df[df['Country name']=='United States']

plt.scatter(df_fr['year'], df_fr['notre indice du bonheur'], color='blue', label='France')
plt.scatter(df_afg['year'], df_afg['notre indice du bonheur'], color='red',label='Afghanistan')
plt.scatter(df_br['year'], df_br['notre indice du bonheur'], color='green',label='Brésil')
plt.scatter(df_sl['year'], df_sl['notre indice du bonheur'], color='gray',label='Sierra Leone')
plt.scatter(df_us['year'], df_us['notre indice du bonheur'], color='yellow',label='États Unis')

plt.title("Évolution de l'indice du bonheur pour quelques pays")
plt.xlabel("Année")
plt.ylabel("Valeur de l'indice")
plt.legend()
plt.show()

# %% [markdown]
# stats descriptives de la colonne de l'indice du bonheur

# %%
df['notre indice du bonheur'].describe()

# %%
