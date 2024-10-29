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
df.head()


# %%

# %%
