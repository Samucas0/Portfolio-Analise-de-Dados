[🇬🇧 For the English version, click here.](./README.md)

---

# Projeto 4: Primeira Análise da Base de Clientes (CRM)

## 🎯 Objetivo de Negócio
O objetivo deste projeto foi simular a primeira tarefa de um analista de dados ao receber um novo conjunto de dados de clientes: realizar um **diagnóstico inicial**. A análise visa fazer um reconhecimento da base, identificando seu tamanho, a qualidade dos dados (presença de valores faltantes) e a distribuição demográfica (países).

## 📚 Bibliotecas e Conceitos Utilizados
-   **Biblioteca:** `Pandas`
-   **Conceitos Principais:**
    -   DataFrames e Series.
    -   Leitura de Dados: `pd.read_csv()`.
    -   Análise Exploratória: `.head()`, `.info()`, `.describe()`, `.shape`.
    -   Seleção de Dados: Filtragem booleana e `.loc[]`.
    -   Contagem de Frequência: `.value_counts()`.

## 📖 Descrição do Processo
1.  **Exercício Prático (`exercicio_pratico/filtro_clientes_alto_valor.py`):** Para praticar seleção de dados, o primeiro passo foi desenvolver um notebook que carrega o dataset e aplica uma filtragem booleana, isolando e exibindo apenas os clientes de "alto valor" (gasto > R$1.000).
2.  **Projeto Principal (`explorador_clientes.ipynb`):** O projeto principal foi desenvolvido como um relatório que responde a três perguntas de negócio:
    -   O número total de clientes foi obtido com o atributo `.shape`.
    -   A identificação de dados faltantes foi feita com `.info()` e com a contagem direta via `.isnull().sum()`.
    -   A distribuição de clientes por país foi calculada e ordenada com o método `.value_counts()`.
    O notebook foi estruturado com células de Markdown para criar uma narrativa clara.

## 📊 Resultados e Insights
A análise exploratória revelou:
-   **Tamanho da Base:** A base de dados contém 8 clientes.
-   **Qualidade dos Dados:** Foi identificado 1 valor faltante na coluna `Pais`, um ponto de atenção para a qualidade do cadastro.
-   **Distribuição Geográfica:** Os EUA têm a maior concentração de clientes (3).

## 💡 Conclusão
Este projeto cumpriu o objetivo de realizar um diagnóstico rápido e eficiente de um novo dataset. Ferramentas como `.info()` e `.value_counts()` se provaram essenciais para extrair informações valiosas com poucas linhas de code.