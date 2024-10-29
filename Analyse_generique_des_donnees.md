---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.4
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- #region editable=true slideshow={"slide_type": ""} -->
**ANALYSE GÉNÉRIQUE DES DONNÉES**
<!-- #endregion -->

```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
```

```python
df=pd.read_excel('data_bonheur.xls')
df.head(20)
```

1) <u>Taille du dataset</u>

```python
taille=df.shape
print(taille)
```

On a donc 9 critères pour chaque couple pays et année


Sur combien de pays l'étude est menée ? Quels sont-ils ?

```python
pays = df['Country name'].unique()
print(pays,len(pays))

```

<!-- #region editable=true slideshow={"slide_type": ""} -->
Quels sont les critères qui rentrent en compte dans l'indice du bonheur ?
<!-- #endregion -->

* Life Ladder : indice qui montre la position personnelle sur le chemin de l'évolution et du succès
* GPD per capita : combien chaque pays produit, divisé par le nombre de personnes dans le pays. Le PIB par habitant donne des informations sur la taille de l'économie et sur la performance de celle-ci.
* Social support : avoir quelqu'un sur qui compter en cas de problème.  
* Healthy life expectancy : Plus précis que l'espérance de vie car prend en compte la santé physique et mentale.
La santé mentale est un élément clé du bien-être subjectif et constitue également un facteur de risque pour la santé physique future et la longévité. La santé mentale influence et détermine de nombreux choix, comportements et résultats individuels.
* Freedom to make life choices : inclut également les droits de l'homme. Ces droits sont inhérents à tous les êtres humains, indépendamment de la race, du sexe, de la nationalité, de l'ethnie, de la langue, de la religion ou de tout autre statut. Les droits de l'homme comprennent le droit à la vie et à la liberté, la liberté contre l'esclavage et la torture, la liberté d'opinion et d'expression, le droit au travail et à l'éducation, et bien d'autres. Chacun a droit à ces droits sans discrimination.
* Generosity : un indicateur clair d'un engagement communautaire positif et un moyen central par lequel les humains se connectent les uns aux autres. Les recherches montrent que, dans toutes les cultures, dès la petite enfance, les individus sont attirés par des comportements qui profitent aux autres.
* Perception of Corruption : Les gens font-ils confiance à leurs gouvernements et ont-ils confiance en la bienveillance des autres ?
* Positive aspect
* Negative aspect



2. <u>Cohérence entre les types des colonnes et leur contenu</u>



Quels sont les types des différentes données ?

```python
print(df.dtypes)
```

Toutes les données sont des flottants (sauf les années) ce qui est logique puisqu'il s'agit d'indices numériques sur différentes échelles.

```python
for colonne in df.columns:
    print(len(df[colonne].unique()))
```

Les données sont réparties sur 165 pays, 18 années, et au total 2199 couples (pays,année). Certaines catégories ont des indices identiques pour plusieurs couples donnés.

```python
print(df.isnull().sum())
```

Certaines valeurs sont manquantes, notamment sur la perception de la corruption et la générosité.


3. <u>Statistiques descriptives des colonnes</u>

```python
for colonne in df.columns:
    statistiques = df[colonne].describe()
    print(statistiques)
```

```python

```
