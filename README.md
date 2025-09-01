# Classificação de Cervejas com Árvore de Decisão

Este projeto utiliza Python, pandas e scikit-learn para classificar baseado em Machine Learning tipos de cerveja com base em características como temperatura, tipo de copo, presença de espuma e cor. O modelo de árvore de decisão é treinado usando dados de um arquivo Excel.

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

1. Coloque o arquivo `dados_cerveja.xlsx` na mesma pasta do script.
2. Execute o script `bebidas.py` em um ambiente Python.

## Funcionalidades

- Leitura dos dados de cerveja de um arquivo Excel.
- Conversão de variáveis categóricas em numéricas.
- Treinamento de um modelo de árvore de decisão.
- Visualização da árvore de decisão.
- Previsão de classe para novos exemplos.

## Exemplo de Previsão

```python
model.predict([[-6,1,1,0]])
```
