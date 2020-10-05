# happinesspredictor 
**Deploy** *https://happinesspredictor.herokuapp.com*   

## Bibliotecas utilizadas:

    - import pandas as pd
    - import numpy as np
    - import matplotlib.pyplot as plt
    - from sklearn.preprocessing import StandardScaler
    - from sklearn.ensemble import RandomForestClassifier
    - from sklearn.metrics import confusion_matrix
    - from sklearn.metrics import classification_report,f1_score,precision_score,average_precision_score,recall_score,accuracy_score
    - from sklearn.metrics import roc_curve, roc_auc_score
    - from sklearn.linear_model import LogisticRegression
    - import pickle
    - Streamlit

## O que é World Happiness Report?

O Happines Report é uma pesquisa histórica sobre o índice de felicidade global. Nele são classificados cerca de 156 países de acordo com o grau de felicidade de seus cidadãos. Essa classificação toma por critérios fatores sociais, como:

- GDP (Análogo ao PIB brasileiro - Produto Interno Bruto);
- Family;
- Health;
- Freedom;
- Corruption;
- Generosity;
- Etc...

### Etapa 1 - O problema

Com o intuito de criar um modelo preditivo capaz de prever a **Felicidade** ou **Infelicidade** de determinada região e quais as principais condições que afetarão seus resultados futuros. Este piloto pode ser utilizado em pesquisas de clima organizacional e de sentimento de uma determinada sociedade.

### Etapa 2 - Coleta ou importação de dados

Os datasets utilizados neste estudo podem ser encontrados no kaggle, por meio do link abaixo:
https://www.kaggle.com/unsdsn/world-happiness


### Etapa 3 - Preparação dos dados

Para preparar os dados, utilizou-se métodos e funções que permitiram:
1. Eliminar as colunas desnecessárias e que não eram comuns a todos os datasets.
2. Unificar as tabelas, agrupando-as por região, atribuindo assim média dos atributos a cada coluna.
 
### Etapa 4 - Análise exploratória
O próximo passo, após a manipulação dos dados, foi analisar o dataframe quanto aos seguintes quesitos para:
1. Identificar o tipo de cada categoria;
2. Perceber se existem dados nulos no dataframe; 
3. Exibir a descrição estatística dos dados;
4. Definir a variável binária de saída, com base na nota de felicidade (Happiness Score);
5. Visualizar a distribuição da quantidade de regiões **Felizes** X **Infelizes**;
6. Identificar quais possuem alguma relação;
7. perceber a dispersão de cada variável a ser utilizada; 
8. Explorar as variáveis a serem trabalhadas no modelo, para identificar outliers frente a variável de saída;
9. Obter insights sociais diante das visualizações.
10.Transformar variáveis categóricas em numéricas.

### Etapa 5 - Modelagem 
1. Importação e implementação do modelo de classificação RandomForest;
2. Métricas de avaliação do modelo RandomForest;
3. Importação e implementação de um segundo modelo. Logistic Regression;
4. Métricas de avaliação do modelo Logistic Regression;
5. Análise comparativa entre os modelos. (Curva ROC)


### Etapa 6 - Comunicação e visualização

1. Elaboração de apresentação do processo de Data Science.

### Etapa 7 - Implementação e manutenção

# Deployment do modelo com melhor desempenho - RandomForest.

Utilizou-se o Streamlit e Heroku para implementar este deploy.
**Deploy** *https://happinesspredictor.herokuapp.com*   
