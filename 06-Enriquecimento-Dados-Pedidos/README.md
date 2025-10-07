# Projeto 6: Enriquecimento de Dados para Análise de Marketing

## 🎯 Objetivo de Negócio

O objetivo deste projeto foi executar um fluxo de trabalho fundamental em análise de dados: **enriquecer** uma base de dados transacional (pedidos) com informações demográficas de uma segunda base (clientes). A meta final era responder à pergunta de negócio: "Em qual região os clientes gastam mais, em média, por pedido?", um insight impossível de se obter com qualquer uma das fontes de dados isoladamente.

## 📚 Bibliotecas e Conceitos Utilizados

-   **Biblioteca:** `Pandas`
-   **Conceitos Principais:**
    -   **Junção de Dados:** `pd.merge()` com ênfase no método `how='left'` para garantir a integridade dos dados da tabela principal.
    -   **Tratamento de Dados Ausentes:** Identificação de valores nulos (`NaN`) resultantes da junção e limpeza com `.dropna()`.
    -   **Agregação de Dados:** Combinação de `.groupby()` com `.mean()` para calcular a métrica final.

## 📖 Descrição do Processo

1.  **Exercício Prático (`exercicio_pratico/tratamento_notas_faltantes.py`):**
    A preparação para este projeto começou com um exercício focado em uma técnica essencial de limpeza de dados: o preenchimento de valores nulos. O script praticou o uso de `.fillna()` para substituir `NaN`s em uma coluna de notas com o valor da média da própria coluna, garantindo que a integridade estatística do dataset fosse mantida.

2.  **Desenvolvimento do Projeto Principal (`analise_pedidos_clientes.ipynb`):**
    -   **Extração:** Carregamento dos dois datasets distintos: `pedidos.csv` e `clientes_regiao.csv`.
    -   **Transformação (Merge):** Foi utilizado um `left merge` para unir os dois DataFrames, com `df_pedidos` como a tabela da esquerda. Essa escolha foi **crítica e intencional** para cumprir o requisito de manter todos os pedidos, mesmo aqueles sem um cliente correspondente na base de clientes, que se tornam `NaN` após a junção.
    -   **Transformação (Limpeza):** Após a junção, as linhas com dados nulos (representando os "pedidos órfãos") foram removidas com `.dropna()`, pois não poderiam ser atribuídas a uma região para a análise final.
    -   **Análise e Agregação:** O DataFrame limpo e enriquecido foi então agrupado por `Regiao`, e a média do `Valor_Pedido` foi calculada para cada grupo, respondendo diretamente à pergunta de negócio.

## 📊 Resultados e Insights

A análise do gasto médio por região, após a junção e limpeza dos dados, gerou o seguinte resultado:

| Regiao | Valor_Pedido |
| :--- | :--- |
| Nordeste | 500.00 |
| Sudeste | 162.62 |
| Norte | 175.25 |

**Principal Insight:**
-   A análise revelou que, apesar da região **Sudeste** ter o maior volume total de vendas (conforme visto no erro da análise do Dia 5), é a região **Nordeste** que possui o maior gasto médio por pedido. Este é um insight contraintuitivo e muito mais valioso, que só foi possível obter calculando a média em vez da soma.
-   O processo também identificou um pedido "órfão" (ID_Cliente 8), um ponto de atenção sobre a integridade referencial entre as bases de dados da empresa.

## 💡 Conclusão e Próximos Passos

Este projeto demonstrou um fluxo de trabalho de BI completo em pequena escala: integrar dados de múltiplas fontes, limpar o resultado e extrair um insight de negócio que não era aparente inicialmente. A distinção entre `inner` e `left` join, e `sum` vs `mean`, provou ser fundamental para a precisão da análise.

Como próximos passos, esta análise poderia ser expandida para:
1.  Calcular também o **número de clientes únicos** por região para entender melhor a distribuição da base.
2.  Visualizar os resultados com um gráfico de barras para facilitar a comunicação do insight.
3.  Investigar os pedidos "órfãos" para entender a causa da falha de integridade dos dados.