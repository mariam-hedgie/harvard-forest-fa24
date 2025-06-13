# Harvard Forest CO₂ Flux Analysis

This is my college python class' projectd

This project analyzes long-term CO₂ flux data from the Harvard Forest eddy flux tower. The goal is to understand how environmental conditions such as temperature, radiation, and wind affect CO₂ uptake and release in forest ecosystems.

## 🌲 Project Context

Forests play a critical role in regulating the global carbon cycle. This analysis uses real-world data collected at Harvard Forest — the oldest eddy flux tower in the world — to model and visualize carbon flux patterns over time.

## 🧪 Tasks Overview

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

## 📊 Outputs

This repository includes:
- `projectd.py`: Full project code
- `timeseries.png`: CO₂ time series plot
- `missingdata.png`: Missing data per year
- `monthlyflux.png`: Monthly flux patterns
- `modelcomparison.png`: Model vs. data visualization
- `avgflux.png`: Yearly average modeled flux

## 💡 Key Insight

Negative CO₂ flux values indicate forest **carbon uptake** (sink), while positive values indicate **release** (source). This analysis highlights how seasonal and yearly climate patterns influence forest carbon dynamics.

## 🧰 Technologies Used

- Python
- NumPy
- Matplotlib
