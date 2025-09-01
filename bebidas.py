# %%
import pandas as pd
df= pd.read_excel('dados_cerveja.xlsx')

df

# %%
y = df['classe']
caracteristica = ['temperatura','copo','espuma','cor']
x = df[caracteristica].replace({'mud':1,'pint':0,'sim':1,'não':0, 'clara':1,'escura':0})

# %%
from sklearn import tree 

model =tree.DecisionTreeClassifier()

model.fit(x, y)

# %%
import matplotlib.pyplot as plt

plt.figure(dpi=400, figsize=[4,4])

tree.plot_tree(model,
               feature_names=caracteristica,
               class_names=model.classes_,
               filled=True)
# %%
model.predict([[-6,1,1,0]])
