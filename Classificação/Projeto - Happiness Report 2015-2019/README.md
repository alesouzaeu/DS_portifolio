# happinesspredictor 
**Deploy** *https://happinesspredictor.herokuapp.com*   


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

Para a importação, utilizamos

### Etapa 3 - Preparação dos dados

Para preparar os dados, utilizou-se métodos e funções que permitiram:
1. Eliminar as colunas desnecessárias e que não eram comuns a todos os datasets.
2. Unificar as tabelas, agrupando-as por região, atribuindo assim média dos atributos a cada coluna.
 
### Etapa 4 - Análise exploratória
O próximo passo, após a manipulação dos dados, foi analisar o dataframe quanto aos seguintes quesitos:
1. Identificar o tipo de cada categoria;
2. Perceber se existem dados nulos no dataframe. 
3. Exibir a descrição estatística dos dados.
4. Definir a variável binária de saída, com base na nota de felicidade. (Happiness Score)
5. Analisara dispersão de cada variável a ser utilizada. 
6. Identificar quais possuem alguma relação.
7. Visualizar a distribuição da quantidade de regiões **Felizes** X **Infelizes**


### Etapa 5 - Modelagem 


### Etapa 6 - Comunicação e visualização

### Etapa 7 - Implementação e manutenção
