[🇧🇷 Para a versão em português, clique aqui.](./LEIA-ME.md)

---

# Project 13: Executive Sales Dashboard with Pivot Tables

## 🎯 Business Objective
The goal of this project is to transform raw, granular transactional data into a high-level executive dashboard. By using advanced reshaping techniques, we aim to answer critical business questions such as "Who is the top-performing sales representative?" and "Which employee specializes in which product category?". This creates a tool for management to make quick decisions regarding performance bonuses and resource allocation without sifting through thousands of rows.

## 📚 Libraries and Concepts Used
-   **Libraries:** `Pandas`, `Seaborn`, `Numpy`
-   **Key Concepts:**
    -   **Data Reshaping (`.pivot_table()`):** Transforming long-format transaction logs into wide-format matrices for side-by-side comparison.
    -   **Frequency Analysis (`.crosstab()`):** Counting occurrences between categorical variables to understand distributions and rates.
    -   **Data Styling (`.style`):** Using Pandas Styler to apply heatmaps, data bars, and currency formatting, turning a DataFrame into a presentation-ready report.
    -   **Data Simulation:** Generating realistic mock sales data with `Numpy` to simulate business scenarios.

## 📖 Process Description
1.  **Foundational Exercise (`practice_exercise/titanic_crosstab_analysis.py`):**
    The day began with a focused script on the difference between raw counts and normalized rates. We used `pd.crosstab()` on the Titanic dataset to prove that while 3rd class had more passengers, 1st class had a significantly higher *survival rate* (percentage).

2.  **Main Project (`sales_rep_performance_panel.ipynb`):**
    -   **Data Generation:** A synthetic dataset of 1,500 sales transactions was created, simulating a Pareto distribution where a few large deals exist among many smaller ones.
    -   **Matrix Creation:** We used `pivot_table` to aggregate sales amounts, setting `Sales_Rep` as rows and `Category` as columns. This instantly revealed the strengths and weaknesses of each team member.
    -   **Dashboard Styling:** We applied a gradient heatmap (Greens) to highlight category specialists and added data bars to the "Total Revenue" column to visually flag top performers.

## 📊 Results & Insights
-   **Transformation:** We successfully converted a 1,500-row dataset into a concise 6x5 matrix.
-   **Strategic Insight:** The dashboard clearly distinguishes between "Generalists" (who sell well across all categories) and "Specialists" (who dominate a single niche like Hardware or Consulting).
-   **Business Value:** This project demonstrates how to move beyond basic data dump exports and provide stakeholders with a visual, interactive tool that requires zero additional BI software.

## 💡 Conclusion
This project highlights the power of Pandas not just for calculation, but for *communication*. By mastering pivot tables and styling, an analyst can deliver actionable intelligence directly within a Python notebook, bridging the gap between raw code and business strategy.