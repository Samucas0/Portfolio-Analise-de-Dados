[🇧🇷 Para a versão em português, clique aqui.](./LEIA-ME.md)

---

# Project 8: Visual Report on Raw Material Cost Variation

## 🎯 Business Objective
The objective of this project was to create a clear and informative visual report to track the price fluctuation of key raw materials over time. Instead of just presenting a table of numbers, the goal was to use data visualization to immediately highlight trends, peaks, and troughs, enabling faster and more intuitive decision-making for the supply chain and finance teams.

## 📚 Libraries and Concepts Used
This project introduces the foundational library for data visualization in Python.
-   **Library:** `Matplotlib`
-   **Key Concepts:**
    -   **Line Charts (`plt.plot`):** Used to show the evolution of a variable over time.
    -   **Bar Charts (`plt.bar`):** Used to compare quantities across different categories.
    -   **Chart Customization:** Adding titles, labels (`xlabel`, `ylabel`), and legends (`legend`).
    -   **Annotations (`plt.annotate`):** The key skill of this project, used to programmatically highlight and add comments to specific data points of interest, guiding the viewer's attention.

## 📖 Process Description
1.  **Foundational Exercise (`practice_exercise/sales_goals_chart.py`):**
    The day started with a practical exercise to compare categorical data. A bar chart was created to show the performance of different sellers, and a horizontal line (`plt.axhline`) was added to represent a common sales goal, practicing the combination of different plot types.

2.  **Main Project (`raw_material_cost_report.ipynb`):**
    -   **Data Simulation:** Fictional monthly cost data was created for three raw materials (Steel, Copper, Aluminum).
    -   **Dynamic Plotting:** A `for` loop was implemented to plot the cost evolution for each material, making the code scalable and clean.
    -   **Insight Highlighting:** The `plt.annotate()` function was used to automatically find and label the highest cost peak for 'Copper' and the lowest cost point for 'Steel'. This transforms the chart from a simple visualization into an analytical tool that actively points out key events.

## 📊 Result
The final output is a line chart that not only displays the cost trends for all materials but also uses arrows and text annotations to explicitly draw attention to the most significant price variations, providing immediate insights without requiring manual analysis from the viewer.

## 💡 Conclusion
This project demonstrates the fundamental principle of data storytelling: a good visualization is not just about showing the data, but about **communicating the insight** hidden within it. The use of annotations proved to be a powerful technique to guide the narrative and make the report's conclusions instantly understandable.