# %%
import pandas as pd 

df = pd.read_excel('dados_frutas.xlsx')

df
# %%
y = df['Fruta']

caracteristicas = ['Arredondada', 'Suculenta', 'Vermelha', 'Doce']
x = df[caracteristicas]

# %%
from sklearn import tree

model = tree.DecisionTreeClassifier()

model.fit(x, y)
# %%
import matplotlib.pyplot as plt

plt.figure(dpi=400, figsize=[4,4])

tree.plot_tree(model,
               feature_names=caracteristicas,
               class_names=model.classes_,
               filled=True)
# %%
model.predict([[0,1,0,0]])