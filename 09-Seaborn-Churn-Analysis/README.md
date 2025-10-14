[🇧🇷 Para a versão em português, clique aqui.](./LEIA-ME.md)

---

# Project 9: Risk Factor Analysis for Customer Churn

## 🎯 Business Objective
The objective of this project is to perform an exploratory data analysis (EDA) on a telecommunications company's customer dataset to identify key factors associated with customer churn. By visualizing the data with Seaborn, we aim to uncover patterns and answer critical business questions, such as "Do customers with month-to-month contracts churn more?" and "Is the monthly charge distribution different for customers who churn?".

## 📚 Libraries and Concepts Used
This project introduces Seaborn, a powerful statistical data visualization library built on top of Matplotlib.
-   **Libraries:** `Pandas`, `Matplotlib`, `Seaborn`
-   **Key Concepts:**
    -   **Statistical Visualization:** Using plots designed to reveal relationships and distributions.
    -   **`countplot()` with `hue`:** To compare the count of a category (Churn) within another category (Contract).
    -   **`boxplot()`:** To compare the distribution of a numerical variable (Monthly Charges) across different categories (Churn status).

## 📖 Process Description
1.  **Foundational Exercise (`practice_exercise/seaborn_tips_exploration.py`):** The day began by exploring a classic dataset (`tips`) to practice creating fundamental statistical plots like `countplot` and `boxplot`, understanding how Seaborn simplifies these visualizations.
2.  **Main Project (`churn_risk_analysis.ipynb`):**
    -   **Data Loading:** The "Telco Customer Churn" dataset was loaded into a Pandas DataFrame.
    -   **Hypothesis 1 (Contract vs. Churn):** A `countplot` was used to visualize the number of customers for each `Contract` type, segmented by the `Churn` status using the `hue` parameter. This provided an immediate visual comparison.
    -   **Hypothesis 2 (Monthly Charges vs. Churn):** A `boxplot` was generated to compare the statistical distribution (median, quartiles, outliers) of `MonthlyCharges` for customers who churned versus those who did not.

## 📊 Results & Insights
The analysis yielded clear, actionable insights:
-   The `countplot` overwhelmingly showed that customers on **Month-to-month contracts** represent the vast majority of churn cases, indicating a critical risk factor.
-   The `boxplot` revealed that customers who **churned tend to have a higher median monthly charge**, suggesting that higher prices could be a significant driver of customer cancellation.

## 💡 Conclusion
This project demonstrates the power of statistical visualization to quickly validate business hypotheses. With just two plots, Seaborn allowed us to identify two of the most significant predictors of customer churn: short-term contracts and higher monthly fees. This analysis provides a solid foundation for data-driven retention strategies.