[🇧🇷 Para a versão em português, clique aqui.](./LEIA-ME.md)

---

# Project 11: Time Series Analysis of Sales Data

## 🎯 Business Objective
The goal of this project is to analyze historical sales data from a superstore to identify long-term trends and seasonal patterns. By transforming daily transactional data into a time-series format, we can answer critical business questions like "Is our business growing over time?" and "Which months are consistently the strongest for sales?", providing key insights for inventory planning and marketing strategies.

## 📚 Libraries and Concepts Used
-   **Libraries:** `Pandas`, `Matplotlib`, `Seaborn`
-   **Key Concepts:**
    -   **Time Series Analysis:** Handling and analyzing data indexed by time.
    -   **Datetime Conversion:** Using `pd.to_datetime` with `dayfirst=True` to handle non-standard date formats.
    -   **Resampling (`.resample()`):** Aggregating data from a daily to a monthly frequency.
    * **Moving Averages (`.rolling()`):** A technique to smooth out short-term volatility and reveal the underlying long-term trend.
    * **Seasonality Detection:** Using `.groupby()` on the datetime index's month component to isolate seasonal patterns.

## 📖 Process Description
1.  **Foundational Exercise (`practice_exercise/quarterly_sales_aggregator.py`):** The day's work began with a focused exercise on the `.resample()` method, aggregating daily sales data into a quarterly summary to practice changing the time frequency of a dataset.
2.  **Main Project (`sales_seasonality_analysis.ipynb`):**
    -   **Data Preparation:** The dataset was loaded, and the `Order Date` column was correctly converted to a datetime format and set as the DataFrame's index.
    -   **Trend Analysis:** Daily sales were resampled into a monthly total. A 6-month moving average was then calculated and plotted on top of the monthly sales data to clearly visualize the long-term growth trend.
    -   **Seasonality Analysis:** To uncover which months perform best on average, the original DataFrame was grouped by the month component of its datetime index (`df.index.month`), and the mean sales for each month were calculated and visualized in a bar chart.

## 📊 Results & Insights
-   **Trend:** The analysis revealed a clear and consistent **upward trend** in sales over the years, indicating healthy business growth. The moving average smooths out the noise and makes this trend undeniable.
-   **Seasonality:** A distinct seasonal pattern emerged, with sales consistently peaking in the last quarter of the year (September through December) and hitting a low point in the first quarter (February).

## 💡 Conclusion
This project demonstrates the ability to transform raw, daily transactional data into strategic insights about business trends and cycles. Identifying both the long-term growth and the predictable seasonality provides immense value for forecasting, inventory management, and the planning of marketing campaigns around peak sales months.