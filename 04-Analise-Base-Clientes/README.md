[🇧🇷 Para a versão em português, clique aqui.](./LEIA-ME.md)

---

# Project 4: Initial Customer Database Analysis (CRM)

## 🎯 Business Objective
The objective of this project was to simulate a data analyst's first task upon receiving a new customer dataset: performing an **initial diagnosis**. The analysis aims to generate a preliminary overview of the customer base, identifying its size, data quality (presence of missing values), and primary demographic distribution (countries).

## 📚 Libraries and Concepts Used
-   **Library:** `Pandas`
-   **Key Concepts:**
    -   DataFrames and Series.
    -   Data Loading: `pd.read_csv()`.
    -   Exploratory Analysis: `.head()`, `.info()`, `.describe()`, `.shape`.
    -   Data Selection: Boolean filtering and `.loc[]`.
    -   Frequency Counting: `.value_counts()`.

## 📖 Process Description
1.  **Foundational Exercise (`exercicio_pratico/filtro_clientes_alto_valor.py`):** To practice data selection, the first step was to develop a notebook to load the dataset and apply a boolean filter, isolating and displaying only "high-value" customers (total spend > $1,000).
2.  **Main Project (`explorador_clientes.ipynb`):** The main project was structured as a report that answers three key business questions:
    -   The total number of customers was obtained using the `.shape` attribute.
    -   Missing data was identified by interpreting the output of `.info()` and by direct counting with `.isnull().sum()`.
    -   The distribution of customers by country was automatically calculated and ranked using the `.value_counts()` method.
    The notebook was structured with Markdown cells to create a clear narrative.

## 📊 Results & Insights
The exploratory analysis revealed:
-   **Database Size:** The database contains 8 customers.
-   **Data Quality:** 1 missing value was identified in the `Pais` (Country) column, a point of concern for data entry quality.
-   **Geographic Distribution:** The USA has the highest concentration of customers (3), with the remaining countries having 1 customer each.

## 💡 Conclusion
This project fulfilled the objective of performing a quick and efficient diagnosis of a new dataset. Tools like `.info()` and `.value_counts()` proved essential for extracting valuable information about the data's structure and content with very few lines of code.