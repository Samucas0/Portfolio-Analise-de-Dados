[🇬🇧 For the English version, click here.](./README.md)

---

# Projeto 6: Enriquecimento de Dados de Pedidos para Análise de Marketing

## 🎯 Objetivo de Negócio
O objetivo deste projeto foi executar um fluxo de trabalho fundamental em análise de dados: **enriquecer** uma base de dados de pedidos com informações demográficas de uma base de clientes. A meta final era responder à pergunta: "Em qual região os clientes gastam mais, em média, por pedido?", um insight impossível de se obter com as fontes de dados isoladas.

## 📚 Bibliotecas e Conceitos Utilizados
-   **Biblioteca:** `Pandas`
-   **Conceitos Principais:**
    -   Junção de Dados: `pd.merge()` com ênfase no método `how='left'`.
    -   Tratamento de Dados Ausentes: Identificação de `NaN`s e limpeza com `.dropna()`.
    -   Agregação de Dados: Combinação de `.groupby()` com `.mean()`.

## 📖 Descrição do Processo
1.  **Exercício Prático (`exercicio_pratico/tratamento_notas_faltantes.py`):** A preparação começou com um exercício focado em limpeza, usando `.fillna()` para substituir valores nulos com a média da coluna, uma técnica essencial para lidar com dados do mundo real.
2.  **Projeto Principal (`analise_pedidos_clientes.ipynb`):**
    -   **Extração:** Carregamento de dois datasets: `pedidos.csv` e `clientes_regiao.csv`.
    -   **Transformação (Merge):** Foi utilizado um `left merge` para unir os DataFrames, mantendo todos os registros de pedidos, mesmo aqueles sem um cliente correspondente.
    -   **Transformação (Limpeza):** Após a junção, as linhas com dados nulos ("pedidos órfãos") foram removidas com `.dropna()` para não interferir na análise final.
    -   **Análise e Agregação:** O DataFrame limpo e enriquecido foi agrupado por `Regiao`, e a média do `Valor_Pedido` foi calculada para cada grupo.

## 📊 Resultados e Insights
A análise revelou que, em média, os clientes da região 'Nordeste' têm o maior gasto por pedido. Este é um insight contraintuitivo, já que outras regiões poderiam ter um volume total de vendas maior, mas um gasto médio por cliente menor. O processo também identificou um "pedido órfão", um ponto de atenção sobre a integridade dos dados da empresa.

## 💡 Conclusão
Este projeto demonstrou um fluxo de BI completo em pequena escala: integrar dados de múltiplas fontes, limpar o resultado e extrair um insight de negócio. A distinção entre `inner` e `left` join, e `sum` vs `mean`, provou ser fundamental para a precisão da análise.