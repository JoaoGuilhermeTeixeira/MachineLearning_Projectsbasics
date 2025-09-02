# %%
import pandas as pd

df = pd.read_parquet("dados_clones.parquet")

df

df['General Jedi encarregado'] = df['General Jedi encarregado'].str.strip()

 # %%
y=df['Status ']

df['General Jedi encarregado'] = df['General Jedi encarregado'].replace({
    'Yoda': 1,
    'Shaak Ti': 2,
    'Obi-Wan Kenobi': 3,
    'Mace Windu': 4,
    'Aayla Secura': 5
})

caracteristicas = ['Massa(em kilos)', 'General Jedi encarregado', 'Estatura(cm)', 'Tempo de existência(em meses)']
x = df[caracteristicas]

# %%
from sklearn import tree

model = tree.DecisionTreeClassifier(max_depth=3) 
model.fit(x, y)  


# %%
import matplotlib.pyplot as plt

plt.figure(dpi=400, figsize=[4,4])
tree.plot_tree(model,
               feature_names=caracteristicas,
               class_names=model.classes_,
               filled=True)


