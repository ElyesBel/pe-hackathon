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

df = pd.read_excel('data/DataForTable2.1WHR2023.xls')

df

# On peut difficilement définir une colonne comme indice, on va garder la colonne NaN

# Pour départager les pays entre eux, on va tenter de regarder les pays ayant les valeurs maximales pour les critères donnés par chaque colonne. Il faudra trouver une pondération des différents critères, sinon le nombre de données à analyser et à mettre en regard sera trop important.
#
# On a des données glissantes sur les ans pour chaque pays, on pourra donc aussi essayer de considérer l'amélioration des données du "bonheur" de chaque pays ces dernières années.

#
