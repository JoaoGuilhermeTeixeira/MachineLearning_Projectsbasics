# Classificação de Cervejas e Frutas com Árvore de Decisão

Este projeto utiliza Python, pandas e scikit-learn para classificar tipos de cerveja e frutas com base em características específicas, utilizando modelos de árvore de decisão treinados com dados de arquivos Excel.

## Requisitos

- Python 3.13+
- pandas
- scikit-learn
- matplotlib
- openpyxl

## Instalação

Instale as dependências com:

```
pip install pandas scikit-learn matplotlib openpyxl
```

## Como usar

1. Coloque os arquivos `dados_cerveja.xlsx` e `dados_frutas.xlsx` na mesma pasta dos scripts.
2. Execute os scripts `bebidas.py` e `frutas.py` em um ambiente Python.

## Funcionalidades

- Leitura dos dados de cerveja e frutas de arquivos Excel.
- Conversão de variáveis categóricas em numéricas (no caso das cervejas).
- Treinamento de modelos de árvore de decisão.
- Visualização das árvores de decisão.
- Previsão de classe para novos exemplos.

## Exemplo de Previsão

**Cervejas:**
```python
model.predict([[-6,1,1,0]])
```

**Frutas:**
```python
