[🇧🇷 Para a versão em português, clique aqui.](./LEIA-ME.md)

---

# Project 14: Time Series Trends & NLP Sentiment Analysis

## 🎯 Business Objective
This project serves as a consolidation of advanced analytical skills, tackling two distinct but critical business domains: **Time Series Analysis** and **Natural Language Processing (NLP)**.
1.  **Time Series:** To understand sales trends over time, separate signal from noise, and identify weekly seasonality patterns to optimize staffing or marketing.
2.  **NLP:** To analyze unstructured customer feedback (reviews), automate sentiment scoring, and identify the root causes of customer churn or satisfaction.

## 📚 Libraries and Concepts Used
-   **Libraries:** `Pandas`, `Numpy`, `Matplotlib`, `Seaborn`, `TextBlob`, `WordCloud`
-   **Key Concepts:**
    -   **Time Series:** Resampling (`.resample()`), Moving Averages (`.rolling()`), and Datetime properties (`.dt` accessor).
    -   **NLP:** Sentiment Polarity Scoring, Text Preprocessing, Word Clouds for unstructured text visualization.
    -   **Correlation:** Analyzing the relationship between review length and customer satisfaction.

## 📖 Process Description
1.  **Foundational Exercise (`practice_exercise/stock_moving_avg.py`):**
    We started by analyzing stock market trends using Window Functions. We generated random walk data and applied a 7-day and 30-day Rolling Mean to smooth out volatility and visualize the underlying price trend.

2.  **Main Project - Part 1: Time Series (`sales_trend_analysis.ipynb`):**
    -   **Simulation:** Generated hourly sales data for a full year, injecting a pattern where weekends have higher revenue.
    -   **Analysis:** We aggregated data to daily/weekly levels and used a 30-Day Moving Average to visualize growth. We also analyzed seasonality by Day of Week to confirm the "Weekend Spike" hypothesis.

3.  **Main Project - Part 2: Sentiment Analysis (`product_review_analysis.ipynb`):**
    -   **Data Generation:** Created a synthetic dataset of 500 product reviews using text templates to mimic positive, negative, and neutral feedback.
    -   **Feature Engineering:** Calculated `Sentiment_Score` (using TextBlob) and `Review_Length`.
    -   **Visualization:** Created a ranking of best products based on sentiment and a Word Cloud highlighting common terms in negative reviews (e.g., "Battery", "Broken").

## 📊 Results & Insights
-   **Time Series:** Successfully identified that Saturdays and Sundays drive ~$100/hour more revenue than weekdays, validating the need for increased weekend resources.
-   **NLP:** Discovered a correlation between review sentiment and rating. The Word Cloud provided immediate visual cues on product defects, showing that "Battery" issues are the primary driver of negative reviews.
-   **Versatility:** Demonstrated the ability to handle both structured temporal data and unstructured text data within the same analytical framework.

## 💡 Conclusion
This project bridges the gap between quantitative and qualitative analysis. By mastering Time Series, we answer "When are sales happening?". By mastering NLP, we answer "Why are customers buying (or leaving)?". Together, they form a complete toolkit for modern Data Engineering and Analysis.