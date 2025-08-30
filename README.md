# Profit-Forecasting-
Problem Statement & Objective

Problem:
Businesses and policymakers often struggle with predicting retail and food service sales due to fluctuating demand, seasonal patterns (e.g., holidays), and long-term economic trends. Traditional spreadsheets make forecasting manual, error-prone, and difficult to visualize.

Objective:
  1. This project leverages machine learning and interactive dashboards to:
  
  2. Automate monthly sales forecasting for the next 1–36 months.
  
  3. Visualize trends and seasonality in retail & food services data.
  
  4. Allow users to download forecast results in CSV format.
  
  5. Provide a simple, interactive interface for business decision-making.

Step-by-Step Setup Instructions

  1. Download or clone the repository from GitHub.
  
  2. Install the required Python libraries listed in the requirements file (Streamlit, Prophet, Pandas, Plotly, Joblib).
  
  3. Make sure the pre-trained model file (Us_Retail_Sales.pkl) is available in the project folder.
  
  4. Start the Streamlit app by running the main script.
  
  5. Open your browser at the local Streamlit address (usually http://localhost:8501/).

Usage Guide & Examples

 . Use the sidebar slider to choose how many months (1–36) you want to forecast.
  
  . Click the “Run forecast” button to generate predictions.
  
  . View forecast results in both table format and interactive plots.
  
  . Explore trend and seasonality plots to understand sales behavior.
  
  . Download results as a CSV file for further offline analysis.

📊 Example Outputs

  . Forecast DataFrame: Table of predicted sales with confidence intervals.
  
  . Main Forecast Plot: Interactive time series showing historical and predicted sales.
  

📊 Dataset

* **Original Dataset**: [U.S. Census Bureau – Monthly Retail Trade (RSAFS)](https://fred.stlouisfed.org/series/RSAFS)
* **Direct Download (CSV)**: [RSAFS.csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=RSAFS)
* **Pre-trained Model**: `Us_Retail_Sales.pkl` (included in repo).
* **Notebook**: `Sales.ipynb` (exploration, training, evaluation).

