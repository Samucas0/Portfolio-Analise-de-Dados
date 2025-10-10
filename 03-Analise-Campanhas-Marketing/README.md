[🇧🇷 Para a versão em português, clique aqui.](./LEIA-ME.md)

---

# Project 3: Marketing Campaign Performance Analysis (A/B Test)

## 🎯 Business Objective
The objective of this project was to perform a comparative A/B test analysis on two simulated marketing campaigns. The analysis aims to determine which campaign generated better results (higher click volume) and which was more consistent (lower variance), providing a clear, data-driven recommendation for future marketing investments.

## 📚 Libraries and Concepts Used
-   **Library:** `NumPy`
-   **Key Concepts:**
    -   NumPy Arrays (`ndarray`) for efficient numerical computation.
    -   Statistical Aggregation Functions (`.sum()`, `.mean()`, `.std()`).
    -   Modularization with Functions to create reusable analysis blocks.
    -   Conditional Logic (`if/else`) to automate the final recommendation.

## 📖 Process Description
1.  **Foundational Exercise (`exercicio_pratico/calculadora_faturamento_numpy.py`):** To solidify the concept of **vectorization**, an initial script was developed to calculate revenue from arrays of prices and quantities, demonstrating NumPy's power to perform element-wise operations without `for` loops.
2.  **Main Project (`analise_teste_ab.ipynb`):**
    -   **Data Simulation:** Two NumPy arrays were created to simulate the daily clicks of each campaign.
    -   **Modular Analysis:** A function, `analyze_campaign()`, was created to receive a data array and return a dictionary with key metrics (mean, standard deviation, total).
    -   **Processing & Comparison:** The function was called for each campaign, and the results were stored.
    -   **Automated Conclusion:** Using conditional logic, the script compares the performance (mean) and stability (std) metrics to automatically generate a final recommendation.

## 📊 Results & Insights
The analysis generated a comparative report showing that **Campaign 2** was the clear winner, as it not only produced a higher total and average number of clicks (superior performance) but did so with significantly less daily variation (higher stability).

## 💡 Conclusion
This project demonstrates the application of basic statistical analysis to make an informed business decision. Using NumPy allowed for clean and fast calculations, while the code structure transformed a simple calculation into a small decision-support system.