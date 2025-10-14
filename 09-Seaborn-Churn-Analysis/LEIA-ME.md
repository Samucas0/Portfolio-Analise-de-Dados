[🇬🇧 For the English version, click here.](./README.md)

---

# Projeto 9: Análise de Fatores de Risco para Churn de Clientes

## 🎯 Objetivo de Negócio
O objetivo deste projeto é realizar uma análise exploratória de dados (EDA) em um dataset de clientes de uma empresa de telecomunicações para identificar os principais fatores associados ao cancelamento de clientes (churn). Através da visualização dos dados com a biblioteca Seaborn, buscamos descobrir padrões e responder a perguntas críticas de negócio, como "Clientes com contratos mensais cancelam mais?" e "A distribuição da cobrança mensal é diferente para os clientes que cancelam?".

## 📚 Bibliotecas e Conceitos Utilizados
Este projeto introduz o Seaborn, uma poderosa biblioteca de visualização de dados estatísticos construída sobre o Matplotlib.
-   **Bibliotecas:** `Pandas`, `Matplotlib`, `Seaborn`
-   **Conceitos Principais:**
    -   **Visualização Estatística:** Uso de gráficos projetados para revelar relações e distribuições.
    -   **`countplot()` com `hue`:** Para comparar a contagem de uma categoria (Churn) dentro de outra (Contrato).
    -   **`boxplot()`:** Para comparar a distribuição de uma variável numérica (Cobrança Mensal) entre diferentes categorias (status de Churn).

## 📖 Descrição do Processo
1.  **Exercício Prático (`practice_exercise/seaborn_tips_exploration.py`):** O dia começou com a exploração de um dataset clássico (`tips`) para praticar a criação de gráficos estatísticos fundamentais como `countplot` e `boxplot`, entendendo como o Seaborn simplifica essas visualizações.
2.  **Projeto Principal (`churn_risk_analysis.ipynb`):**
    -   **Carregamento dos Dados:** O dataset "Telco Customer Churn" foi carregado em um DataFrame Pandas.
    -   **Hipótese 1 (Contrato vs. Churn):** Um `countplot` foi utilizado para visualizar o número de clientes para cada tipo de `Contrato`, segmentado pelo status de `Churn` usando o parâmetro `hue`.
    -   **Hipótese 2 (Cobrança Mensal vs. Churn):** Um `boxplot` foi gerado para comparar a distribuição estatística da `Cobrança Mensal` para clientes que cancelaram versus os que não cancelaram.

## 📊 Resultados e Insights
A análise gerou insights claros e acionáveis:
-   O `countplot` mostrou de forma esmagadora que os clientes com **contratos Mensais (Month-to-month)** representam a grande maioria dos casos de churn, indicando um fator de risco crítico.
-   O `boxplot` revelou que os clientes que **cancelaram tendem a ter uma cobrança mensal mediana mais alta**, sugerindo que preços mais altos podem ser um motivo significativo para o cancelamento.

## 💡 Conclusão
Este projeto demonstra o poder da visualização estatística para validar rapidamente hipóteses de negócio. Com apenas dois gráficos, o Seaborn nos permitiu identificar dois dos mais significantes preditores de churn: contratos de curto prazo e taxas mensais mais altas. Esta análise fornece uma base sólida para estratégias de retenção baseadas em dados.