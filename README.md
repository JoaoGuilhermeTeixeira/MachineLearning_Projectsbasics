# Classificação de Cervejas, Frutas e Clones de Star Wars com Árvore de Decisão

Este repositório utiliza Python, pandas e scikit-learn para classificar tipos de cerveja, frutas e analisar clones de Star Wars com base em características específicas, utilizando modelos de árvore de decisão treinados com dados de arquivos Excel e Parquet.

## Requisitos

- Python 3.13+
- pandas
- scikit-learn
- matplotlib
- openpyxl
- pyarrow (para o projeto Star Wars)

## Instalação

Instale as dependências com:

```
pip install pandas scikit-learn matplotlib openpyxl pyarrow
```

## Como usar

1. Coloque os arquivos `dados_cerveja.xlsx` e `dados_frutas.xlsx` na mesma pasta dos scripts.
2. Execute os scripts `bebidas.py` e `frutas.py` em um ambiente Python.
3. Para o projeto Star Wars, coloque o arquivo `dados_clones.parquet` na mesma pasta e execute o script `Clones.py`.

## Funcionalidades

- Leitura dos dados de cerveja e frutas de arquivos Excel.
- Leitura dos dados de clones de Star Wars de arquivo Parquet.
- Conversão de variáveis categóricas em numéricas (cervejas e clones).
- Treinamento de modelos de árvore de decisão.
- Visualização das árvores de decisão.
- Previsão de classe para novos exemplos.

## Projetos

### 1. Cervejas

Classificação de tipos de cerveja com base em características químicas e sensoriais.

**Exemplo de Previsão:**
```python
model.predict([[-6,1,1,0]])
```
<img width="1320" height="1312" alt="image" src="https://github.com/user-attachments/assets/c2cdcd11-c985-4957-a380-f4693cbd4b84" />



### 2. Frutas

Classificação de frutas com base em características físicas e nutricionais.

**Exemplo de Previsão:**
```python
model.predict([[0,1,0,0]])
```

<img width="1320" height="1312" alt="image" src="https://github.com/user-attachments/assets/5cee5bc3-56eb-4d8a-b09a-dc9523c7b24a" />




### 3. Star Wars - Análise de Clones

Este projeto utiliza Machine Learning para identificar quais generais Jedi estão associados ao maior número de clones mortos em batalha.  
Utiliza um modelo de árvore de decisão (`DecisionTreeClassifier`) para analisar características dos clones, como massa, estatura, tempo de existência e o general responsável.  
O objetivo é ajudar a identificar padrões que causam maior perca de clones e possíveis problemas que geram essas percas nas tropas sob comando de cada general.

<img width="1320" height="1312" alt="image" src="https://github.com/user-attachments/assets/3ee40c4c-307c-4109-af08-0e9bd4f7dd08" />


**Como executar:**
```bash
python Clones.py
```

O script irá carregar os dados dos clones, treinar o modelo e exibir a árvore de decisão que mostra a relação entre os generais Jedi e o status dos clones (vivos/mortos).

---

Sinta-se à vontade para contribuir com melhorias ou novas análises!
