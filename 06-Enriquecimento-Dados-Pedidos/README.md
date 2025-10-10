[🇧🇷 Para a versão em português, clique aqui.](./LEIA-ME.md)

---

# Project 6: Data Enrichment for Marketing Analysis

## 🎯 Business Objective
The objective of this project was to execute a fundamental data analysis workflow: **enriching** a transactional database (orders) with demographic information from a second database (customers). The final goal was to answer the business question: "In which region do customers spend more, on average, per order?", an insight impossible to obtain from either data source alone.

## 📚 Libraries and Concepts Used
-   **Library:** `Pandas`
-   **Key Concepts:**
    -   Data Joining: `pd.merge()` with a focus on the `how='left'` method.
    -   Handling Missing Data: Identifying `NaN` values resulting from the join and cleaning them with `.dropna()`.
    -   Data Aggregation: Combining `.groupby()` with `.mean()` to calculate the final metric.

## 📖 Process Description
1.  **Foundational Exercise (`exercicio_pratico/tratamento_notas_faltantes.py`):** The preparation for this project began with an exercise focused on data cleaning: using `.fillna()` to replace `NaN`s in a grades column with the column's mean value.
2.  **Main Project (`analise_pedidos_clientes.ipynb`):**
    -   **Extraction:** Two distinct datasets, `pedidos.csv` and `clientes_regiao.csv`, were loaded.
    -   **Transformation (Merge):** A `left merge` was used to join the two DataFrames, with the orders table as the left table. This choice was critical to ensure all orders were kept, even those without a matching customer.
    -   **Transformation (Cleaning):** After the join, rows with null values (representing "orphan orders") were removed using `.dropna()` as they could not be assigned to a region.
    -   **Analysis & Aggregation:** The clean, enriched DataFrame was then grouped by `Regiao` (Region), and the mean of the `Valor_Pedido` (Order Value) was calculated for each group.

## 📊 Results & Insights
The analysis revealed that, on average, customers from the 'Nordeste' (Northeast) region have the highest spend per order. This is a counter-intuitive insight, as other regions might have higher total sales volume but a lower average spend per customer. The process also identified an "orphan order," highlighting a data integrity issue between the company's databases.

## 💡 Conclusion
This project demonstrates a complete, realistic mini-workflow for a data analyst: integrating data from multiple sources, cleaning the result, and performing an aggregation to answer a business question. The distinction between `inner` and `left` join, and `sum` vs `mean`, proved to be fundamental to the accuracy of the analysis.