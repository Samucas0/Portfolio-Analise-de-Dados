[🇧🇷 Para a versão em português, clique aqui.](./LEIA-ME.md)

---

# Project 1: Financial Transaction Batch Validator

## 🎯 Business Objective
The objective of this project was to develop a Python script to perform the first essential step in any financial analysis: **the validation and cleaning of raw data**. The tool automates the processing of a daily batch of transactions, separating valid from invalid entries and calculating key metrics for a quick management report, thus ensuring the reliability of subsequent analyses.

## 📚 Libraries and Concepts Used
-   Python 3 Fundamentals
-   Data Structures: Lists
-   Control Flow: `for` Loops
-   Conditional Logic: `if/else`
-   Variable Manipulation & Mathematical Operators

## 📖 Process Description
1.  **Foundational Exercise (`exercicio_pratico/filtro_pares.py`):** Before tackling the business problem, a smaller script was developed to practice list iteration and conditional logic by filtering even numbers from user input.
2.  **Main Project (`analise_transacoes.py`):** The core logic was applied to the business problem. The script iterates through a list of transactions, validates each one based on business rules (value > 0), segments them into "valid" and "invalid" lists, and calculates the sum, maximum, and minimum valid values in a single pass.

## 📊 Results & Insights
The script successfully processed the data batch, identifying key metrics and data quality issues. The main insight was the identification of invalid transactions (negative or null), which pose a risk to data integrity and require investigation before further analysis.

## 💡 Conclusion
This foundational project demonstrates the ability to automate data quality assurance tasks, an essential, error-prone manual process. It establishes the base for building more complex analytical workflows.