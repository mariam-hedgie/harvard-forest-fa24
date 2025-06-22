# Harvard Forest CO₂ Flux Analysis

This is my college Python class project.

This project analyzes long-term CO₂ flux data from the Harvard Forest eddy flux tower. The goal is to understand how environmental conditions such as temperature, radiation, and wind affect CO₂ uptake and release in forest ecosystems.

---

## 🌲 Context

Forests play a critical role in regulating the global carbon cycle. This analysis uses real-world data collected at Harvard Forest — the oldest eddy flux tower in the world — to model and visualize carbon flux patterns over time.

---

## 🧪 Tasks 

### 1. Data Reading & Summary
- `readdata(filename)`: Loads the dataset from a `.csv` file.
- `summarizedata(hf)`: Plots the CO₂ time series and summarizes key statistics.

### 2. Missing Data Analysis
- `missingdata(hf)`: Calculates and visualizes the percentage of missing data per year.

### 3. Seasonal Patterns
- `seasonalcycle(hf)`: Visualizes monthly average CO₂ fluxes from 1995–2000.

### 4. Regression Modeling
- `HFregression(hf)`: Builds a regression model to predict CO₂ flux from:
  - Net radiation  
  - Air temperature  
  - Water vapor  
  - Wind speed

### 5. Model Visualization
- Compares actual CO₂ data with model predictions.
- Shows the contribution of each variable over time.

### 6. Long-Term Trends
- `averagecarbon(hf, modelest)`: Plots annual average modeled CO₂ flux to assess whether the forest is a net sink or source.

---

## ▶️ How to Run

### 1. Clone this repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

### 2. (Optional) Set up a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install required libraries

```bash
pip install numpy matplotlib
```

### 4. Run the script

```bash
python projectd.py
```

Make sure your CO₂ flux dataset (`HFdata.csv` or similar) is in the same folder as `projectd.py`.

---

## 🧪 Example Usage in Code

```python
import projectd

hf = projectd.readdata('HFdata.csv')
projectd.summarizedata(hf)
projectd.missingdata(hf)
projectd.seasonalcycle(hf)
model = projectd.HFregression(hf)
projectd.averagecarbon(hf, model)
```

---

## 📊 Outputs

This repository includes:
- `projectd.py`: Full project code  
- `timeseries.png`: CO₂ time series plot  
- `missingdata.png`: Missing data per year  
- `monthlyflux.png`: Monthly flux patterns  
- `modelcomparison.png`: Model vs. data visualization  
- `avgflux.png`: Yearly average modeled flux  

---

## 💡 Note

Negative CO₂ flux values indicate forest **carbon uptake** (sink), while positive values indicate **release** (source). This analysis highlights how seasonal and yearly climate patterns influence forest carbon dynamics.

---

## 📚 Libraries Used

- NumPy  
- Matplotlib  

---

## 👩‍💻 Author

Built with ❤️ as part of a Python course project by [Dr. Mariam Husain](https://github.com/mariam-hedgie)


## 📚 Libraries Used

- NumPy
- Matplotlib
