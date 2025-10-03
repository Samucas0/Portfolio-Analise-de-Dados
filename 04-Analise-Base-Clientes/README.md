# Projeto 4: Primeira Análise da Base de Clientes (CRM)

## 🎯 Objetivo de Negócio
O objetivo deste projeto foi simular a primeira tarefa de um analista de dados ao receber um novo conjunto de dados de clientes: realizar um **diagnóstico inicial**. A análise visa fazer um reconhecimento da base de clientes, identificando seu tamanho, a qualidade dos dados (presença de valores faltantes) e a distribuição demográfica principal (países), gerando um primeiro panorama para guiar futuras análises.

## 📚 Bibliotecas e Conceitos Utilizados
Este projeto marca a introdução à principal biblioteca de manipulação de dados em Python.
-   **Bibliotecas:** `Pandas`
-   **Conceitos Principais:**
    -   **DataFrames e Series:** Estruturas de dados fundamentais do Pandas.
    -   **Leitura de Dados:** `pd.read_csv()` para carregar dados de arquivos.
    -   **Análise Exploratória:** Uso dos métodos `.head()`, `.info()`, `.describe()` e `.shape` para um diagnóstico rápido.
    -   **Seleção de Dados:** Filtragem booleana e uso de `.loc[]` para selecionar subconjuntos de dados.
    -   **Contagem de Frequência:** Uso de `.value_counts()` para sumarizar dados categóricos.

## 📖 Descrição do Processo
A análise foi dividida em duas etapas para garantir a fixação dos conceitos:

1.  **Exercício Prático (`exercicio_pratico/filtro_clientes_alto_valor.ipynb`):**
    Para praticar o conceito central de seleção de dados, o primeiro passo foi desenvolver um notebook que carrega o dataset e aplica uma filtragem booleana. O script isola e exibe apenas os clientes considerados de "alto valor" (gasto total > R$1.000), consolidando o uso do `.loc[]`.

2.  **Desenvolvimento do Projeto Principal (`explorador_clientes.ipynb`):**
    Com a base consolidada, o projeto principal foi desenvolvido como um relatório que responde a três perguntas de negócio essenciais:
    -   O número total de clientes foi obtido através do atributo `.shape`.
    -   A identificação de dados faltantes foi feita tanto pela análise do `.info()` quanto pela contagem direta com `.isnull().sum()`.
    -   A distribuição de clientes por país foi calculada de forma automática e ordenada com o método `.value_counts()`.
    O notebook foi estruturado com células de Markdown para criar uma narrativa clara, transformando o código em um relatório analítico.

## 📊 Resultados e Insights
A análise exploratória do arquivo `clientes.csv` revelou:
-   **Tamanho da Base:** A base de dados contém **8 clientes**.
-   **Qualidade dos Dados:** Foi identificado **1 valor faltante** na coluna `Pais`, o que representa um ponto de atenção para a qualidade do preenchimento cadastral.
-   **Distribuição Geográfica:** O país com a maior concentração de clientes é os **EUA**, com 3 clientes. Os demais países (Brasil, Espanha, Reino Unido, Japão) possuem 1 cliente cada.