[🇧🇷 Para a versão em português, clique aqui.](./LEIA-ME.md)

---

# Project 5: Sales Management Report by Product Category

## 🎯 Business Objective
The objective of this project is to transform a list of raw sales transactions into a summarized management report. The analysis aims to group data by product category to calculate essential KPIs (Key Performance Indicators) such as total revenue, number of sales, and average ticket price, providing a clear view of each category's performance for decision-making.

## 📚 Libraries and Concepts Used
-   **Library:** `Pandas`
-   **Key Concepts:**
    -   `.groupby()`: The core tool for splitting data into groups based on a category.
    -   Aggregation Functions: `.sum()`, `.mean()`, `.count()`.
    -   `.agg()`: The advanced method for applying multiple aggregations in a single operation.
    -   Column Renaming: `.rename()` to format the final DataFrame into a professional report.

## 📖 Process Description
1.  **Foundational Exercise (`exercicio_pratico/custo_medio_categoria.py`):** To warm up, the concept of aggregation was practiced in isolation, using `groupby()` combined with `.mean()` to calculate the average cost per category.
2.  **Main Project (`relatorio_gerencial_vendas.ipynb`):**
    -   **Grouping:** The sales DataFrame was grouped by the `Categoria` (Category) column.
    -   **Multiple Aggregation:** The `.agg()` method was used to calculate the sum (`sum`), count (`count`), and mean (`mean`) of the `Valor` (Value) column for each group in a single line of code.
    -   **Report Formatting:** The columns of the resulting DataFrame were renamed to more descriptive and clear names (e.g., `sum` to `Total Revenue ($)`), transforming the technical output into a readable business report.

## 📊 Results & Insights
The analysis resulted in a management report summarizing the performance of each product category, highlighting that the 'Electronics' category is the highest-grossing, while 'Apparel' has a significantly higher average ticket price than 'Books'.

## 💡 Conclusion
This project demonstrates the ability to turn raw transactional data into an aggregated report that generates business insights. The use of `.groupby().agg()` proved to be an extremely efficient and powerful tool for creating management summaries.