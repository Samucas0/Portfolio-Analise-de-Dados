[🇧🇷 Para a versão em português, clique aqui.](./LEIA-ME.md)

---

# Project 15: Interactive Sales Dashboard with Streamlit

<img width="1365" height="767" alt="Captura de tela 2026-02-04 115228" src="https://github.com/user-attachments/assets/cd38a6ae-fa22-4646-9b6a-d9678e1d7b3d" />
<img width="1365" height="767" alt="Captura de tela 2026-02-04 115237" src="https://github.com/user-attachments/assets/0d2bad51-bef3-4971-ae43-458b330653d3" />


## 🎯 Business Objective
The goal of this project is to move beyond static reports (like PDFs or Excel sheets) and build a **Self-Service BI Tool**. By creating an interactive web application, we empower stakeholders (managers, directors) to explore sales data, apply filters dynamically, and answer their own questions without needing to request a new SQL query from the data team.

## 💡 The Learning Curve
This project marked a significant milestone in my journey. Unlike standard analysis scripts, building a web application required a deep dive into **Environment Management** and **Software Engineering** concepts.
I dedicated significant time to mastering the "behind-the-scenes" infrastructure: configuring virtual environments (`.venv`), managing dependencies with `pip`, and understanding how to deploy a local server via terminal. This experience bridged the gap between being a Data Analyst and becoming a Data Engineer.

## 📚 Libraries and Concepts Used
-   **Streamlit:** For converting Python scripts into a deployable web app instantly.
-   **Plotly Express:** For creating interactive charts (zoom, hover, tooltips).
-   **Pandas:** For data manipulation and filtering query logic.
-   **Numpy:** For generating realistic synthetic sales data.

## 🚀 How to Run
1.  Ensure you have the dependencies installed:
    ```bash
    pip install streamlit plotly pandas
    ```
2.  Run the application from your terminal:
    ```bash
    streamlit run 15-Streamlit-Sales-Dashboard/app.py
    ```
3.  The dashboard will open automatically in your browser (usually at `http://localhost:8501`).

## 📊 Key Features
-   **Dynamic Filtering:** Sidebar controls allow users to slice data by Region and Product.
-   **KPI Metrics:** Real-time calculation of Total Revenue, Average Ticket, and Units Sold based on active filters.
-   **Interactive Visualizations:**
    -   *Bar Chart:* Ranking products by revenue performance.
    -   *Line Chart:* analyzing monthly sales trends to identify seasonality.
