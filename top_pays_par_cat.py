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

df = pd.read_excel('data/DataForTable2.1WHR2023.xls')
df

# On va afficher un top 5 des valeurs maximales de chaque colonne par an.

# +
colonnes_analysees = [col for col in df.columns if col not in ['Country name', 'year']]
result_li = []
for col in colonnes_analysees:
    for year, group in df.groupby('year'):
        top_5 = group.nlargest(5, col)[['Country name', col]]
        li_ordonnee = top_5['Country name'].tolist()
        result_li.append({'Donnée':col, 'Année':year, 'Top 5':li_ordonnee})

resultats_df = pd.DataFrame(result_li)
resultats_df.to_csv('top_5_bonheur_par_catégorie&an.csv', index=False)
# -

res = pd.read_csv('top_5_bonheur_par_catégorie&an.csv', index_col='Donnée')
res

# Le bonheur n'est pas censé être grandement variable d'une année sur l'autre : si un pays est dans le top 5 une année, il n'est pas loin les autres années a priori ; on va donc regrouper par colonne tous les pays qui ont été dans le top5 au moins une année.



res = pd.DataFrame(res.groupby(['Donnée'])['Top 5'].agg(lambda x: ' '.join(x)))
res
res.to_csv('top pays par catégorie.csv', header=['Pays les + cool'])

dff = pd.read_csv('top pays par catégorie.csv', index_col='Donnée')
dff
