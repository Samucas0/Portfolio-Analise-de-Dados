[🇧🇷 Para a versão em português, clique aqui.](./LEIA-ME.md)

---

# Project 12: RFM Feature Engineering for Customer Segmentation

## 🎯 Business Objective
The goal of this project is to transform a raw, transactional log dataset (where each row is an *item*) into a structured, customer-centric DataFrame (where each row is a *customer*). By engineering the three core RFM features (Recency, Frequency, Monetary), we can create the foundation for advanced customer segmentation. This allows a business to move from analyzing individual sales to understanding customer behavior, identifying high-value, at-risk, and lost customers.

## 📚 Libraries and Concepts Used
-   **Libraries:** `Pandas`, `Numpy`
-   **Key Concepts:**
    -   **Feature Engineering:** The core theme; creating new, informative columns (`TotalValue`, `Recency`, `Frequency`, `Monetary`) from raw data.
    -   **Row-Level Features (`.apply()`):** Using a custom function with `.apply()` to create a new categorical column based on the logic of a single row.
    -   **Aggregation-Level Features (`.groupby().agg()`):** Using a `groupby` operation to "compress" information from many rows (all transactions for one customer) into single summary features (`sum`, `nunique`, `lambda` logic).
    -   **Data Cleaning:** Handling encoding issues (`'latin1'`), filtering irrelevant data (`.dropna()`), and removing invalid entries (negative quantities).
    -   **Datetime Handling:** Using `pd.to_datetime` and `pd.Timedelta` to calculate date differences for Recency.

## 📖 Process Description
1.  **Foundational Exercise (`practice_exercise/age_categorizer.py`):** The day's work began with a focused exercise on row-level feature engineering. A custom function was defined to categorize ages and then applied using the `.apply()` method to create a new `age_group` column, practicing the creation of categorical features.
2.  **Main Project (`rfm_customer_segmentation.ipynb`):**
    -   **Data Preparation:** The 'Online Retail' dataset was loaded, handling a non-standard `'latin1'` encoding. The data was cleaned by removing canceled orders (negative `Quantity`) and entries with a null `CustomerID`.
    -   **Row-Level Feature Engineering:** A `TotalValue` column was created by multiplying `Quantity` and `UnitPrice`. The `InvoiceDate` column was converted to the proper datetime format.
    -   **Aggregation (RFM) Engineering:** A `snapshot_date` (representing "today") was defined. The DataFrame was then grouped by `CustomerID` and the `.agg()` method was used to calculate the three RFM features:
        -   **Recency (R):** Days since the last purchase (calculated using a `lambda` function).
        -   **Frequency (F):** Count of unique `InvoiceNo` entries.
        -   **Monetary (M):** Sum of the `TotalValue` column.

## 📊 Results & Insights
-   **Transformation:** The primary result is a new, powerful DataFrame where each row uniquely represents a *customer* and their calculated R, F, and M scores. The dataset was successfully transformed from **transaction-level** to **customer-level**.
-   **Key Learning:** This project highlighted the two main types of feature engineering: row-level (using `.apply()`) and aggregation-level (using `.groupby().agg()`). Both are essential, and the choice depends on the problem.
-   **Business Value:** The final `rfm_df` is now ready for the *analysis* step. A business can now easily filter for "Best Customers" (Low R, High F, High M) or "At-Risk Customers" (High R, High F).

## 💡 Conclusion
This project demonstrates the critical ability to manipulate and restructure raw data to build meaningful, behavioral features. By creating the RFM table, we have successfully translated a simple log of transactions into a strategic tool for understanding customer personas, enabling targeted marketing, and making data-driven decisions to improve customer retention.