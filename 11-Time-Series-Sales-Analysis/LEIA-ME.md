[🇬🇧 For the English version, click here.](./README.md)

---

# Projeto 11: Análise de Séries Temporais de Vendas

## 🎯 Objetivo de Negócio
O objetivo deste projeto é analisar dados históricos de vendas de uma grande loja para identificar tendências de longo prazo e padrões de sazonalidade. Ao transformar dados transacionais diários em um formato de série temporal, podemos responder a perguntas críticas de negócio como "Nosso negócio está crescendo ao longo do tempo?" e "Quais meses são consistentemente os mais fortes em vendas?", fornecendo insights para o planejamento de estoque e estratégias de marketing.

## 📚 Bibliotecas e Conceitos Utilizados
-   **Bibliotecas:** `Pandas`, `Matplotlib`, `Seaborn`
-   **Conceitos Principais:**
    -   **Análise de Séries Temporais:** Manipulação e análise de dados indexados por tempo.
    -   **Conversão de Datas:** Uso de `pd.to_datetime` com `dayfirst=True` para lidar com formatos de data não-padrão.
    -   **Reamostragem (`.resample()`):** Agregação de dados de uma frequência diária para mensal.
    * **Médias Móveis (`.rolling()`):** Técnica para suavizar a volatilidade de curto prazo e revelar a tendência de longo prazo.
    * **Detecção de Sazonalidade:** Uso de `.groupby()` no componente de mês do índice de data para isolar padrões sazonais.

## 📖 Descrição do Processo
1.  **Exercício Prático (`practice_exercise/quarterly_sales_aggregator.py`):** O trabalho do dia começou com um exercício focado no método `.resample()`, agregando dados de vendas diárias em um resumo trimestral para praticar a mudança na frequência de tempo de um dataset.
2.  **Projeto Principal (`sales_seasonality_analysis.ipynb`):**
    -   **Preparação dos Dados:** O dataset foi carregado, e a coluna `Order Date` foi corretamente convertida para o formato datetime e definida como o índice do DataFrame.
    -   **Análise de Tendência:** As vendas diárias foram reamostradas para um total mensal. Uma média móvel de 6 meses foi então calculada e plotada sobre os dados de vendas mensais para visualizar claramente a tendência de crescimento a longo prazo.
    -   **Análise de Sazonalidade:** Para descobrir quais meses performam melhor na média, o DataFrame original foi agrupado pelo componente de mês de seu índice de data (`df.index.month`), e a média de vendas para cada mês foi calculada e visualizada em um gráfico de barras.

## 📊 Resultados e Insights
-   **Tendência:** A análise revelou uma clara e consistente **tendência de alta** nas vendas ao longo dos anos, indicando um crescimento saudável do negócio. A média móvel suaviza o ruído e torna essa tendência inegável.
-   **Sazonalidade:** Um padrão sazonal distinto emergiu, com as vendas atingindo picos consistentemente no último trimestre do ano (Setembro a Dezembro) e um ponto baixo no primeiro trimestre (Fevereiro).

## 💡 Conclusão
Este projeto demonstra a capacidade de transformar dados transacionais brutos e diários em insights estratégicos sobre as tendências e os ciclos do negócio. Identificar tanto o crescimento de longo prazo quanto a sazonalidade previsível fornece um valor imenso para projeções (forecasting), gestão de estoque e o planejamento de campanhas de marketing em torno dos meses de pico de vendas.