# macroeconomic-keynesian-cross-visualizer
An interactive Python simulator to model macroeconomic equilibrium, calculate the investment multiplier and visualize the Keynesian Cross

## Features
* **Interactive UI:** Modify the Autonomous Consumption ($C_0$), Planned Investment ($I$), and Marginal Propensity to Consume ($c$) using real-time sliders and text boxes.
* **Instant Calculations:** Automatically calculates and displays the **Investment Multiplier ($k$)** and the **Equilibrium Income ($Y$)**.
* **Sensitivity Analysis:** Generates a detailed data table projecting income levels and planned spending in the terminal before launching the graphical interface.
* **Dynamic Plotting:** Uses `matplotlib` to render the 45-degree reference line and the Aggregate Demand curve, automatically finding the intersection point.

* <img width="1311" height="931" alt="image" src="https://github.com/user-attachments/assets/681469f4-b5e5-4098-aa5d-1f97f04c14b0" />


## 🛠️ Technologies Used
* **Python 3**
* **NumPy:** For generating evenly spaced data ranges.
* **Matplotlib:** For rendering the interactive graph, sliders, and text boxes.

## ⚙️ How to Run
1. Ensure you have Python installed along with the required libraries:
   ```bash
   pip install numpy matplotlib
   ```
2. Run the script from your terminal:
   ```
   python simulador.py
   ```
3. Enter the initial parameters in the terminal when prompted.
4. Interact with the sliders in the graphical window to see real-time macroeconomic changes

---

## Author

**Juan Pablo Quezada**
B.Sc. in Intelligent Computing Engineering
Universidad Autónoma de Aguascalientes (UAA)
