[🇧🇷 Para a versão em português, clique aqui.](./LEIA-ME.md)

---

# Project 2: Mini Inventory Management System

## 🎯 Business Objective
The objective of this project was to develop an interactive console application to automate basic inventory control. The tool aims to replace manual tracking processes, centralizing the addition, removal, and reporting of stock items, ensuring greater control and reducing the potential for operational errors.

## 📚 Libraries and Concepts Used
-   **Libraries:** `re` (for user input handling)
-   **Key Concepts:**
    -   **Functions:** Modularizing code into reusable blocks with single responsibilities.
    -   **Dictionaries:** Used as the core data structure to store inventory.
    -   **Conditional Logic:** `if/elif/else` to control the interactive menu flow.
    -   **Loops:** `while` to keep the application running and `for` to iterate over the inventory.
    -   **Exception Handling:** `try-except` to gracefully handle invalid user inputs.

## 📖 Process Description
1.  **Foundational Exercise (`exercicio_pratico/calculadora_estoque.py`):** First, a simple script was developed to practice creating a function that operates on a dictionary, solidifying the day's main concept.
2.  **Modularization:** The main application was broken down into three core functions: `add_item()`, `remove_item()`, and `generate_stock_report()`.
3.  **Interactive Interface:** The main execution block (`if __name__ == "__main__":`) contains a `while True` loop that creates a console menu, turning the script into an interactive application.
4.  **Robustness:** Input validations and a `try-except` block were implemented to ensure the program does not crash on invalid (e.g., non-numeric) user input.

## 📊 Result
The final result is a functional console application that simulates a real inventory management system, capable of handling user interactions, updating data, and generating reports in real-time.

## 💡 Conclusion
This project was a fundamental step from writing linear scripts to building structured, reusable applications. The key lesson was the importance of separating a complex problem into smaller, manageable parts through functions, and creating a robust, user-facing interactive experience.