# Profit Forecasting System

## About This Project

This is a retail and food service sales forecasting system that uses machine learning to predict future sales trends. It's built to help businesses and policymakers make data-driven decisions by providing automated, accurate sales forecasts with interactive visualizations.

The project demonstrates a complete time-series forecasting workflow, from data preprocessing to model training and deployment, implemented in both a Jupyter notebook for exploration and a Streamlit application for practical use.

## What It Does

* **Automated Forecasting:** Generates monthly sales predictions for the next 1-36 months using machine learning
* **Trend Analysis:** Visualizes long-term sales trends, seasonal patterns, and holiday effects
* **Interactive Dashboard:** Provides an intuitive web interface for exploring forecasts and adjusting parameters
* **Data Export:** Allows users to download forecast results in CSV format for further analysis

## The Problem I'm Solving

### The Challenge

Businesses and policymakers face significant challenges in predicting retail and food service sales due to fluctuating demand, seasonal patterns (particularly around holidays), and long-term economic trends. Traditional spreadsheet-based forecasting is manual, error-prone, difficult to visualize, and cannot easily handle complex time-series patterns.

### My Solution

I built this project to:

* Automate monthly sales forecasting for strategic planning periods (1-36 months)
* Transform complex time-series data into actionable insights through interactive visualizations
* Replace error-prone manual processes with consistent, reproducible machine learning predictions
* Provide decision-makers with an intuitive tool that requires no technical expertise to use
* Enable businesses to anticipate market changes and optimize inventory, staffing, and budgeting

## How to Get Started

1. **Get the Code**

   ```bash
   git clone https://github.com/CodeWithNafisat/Profit-Forecasting.git
   cd Profit-Forecasting/RetailAndSales
   ```

2. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**

   ```bash
   streamlit run app.py
   ```

4. **Access the Dashboard**
   Open your browser and navigate to `http://localhost:8501` to use the forecasting system.

---

## How to Use It

* Use the sidebar slider to select your forecast horizon (1-36 months)
* Click "Run Forecast" to generate predictions based on historical data
* Explore the interactive plots showing historical trends and future predictions
* Analyze seasonality and trend components to understand underlying patterns
* Download forecast results as CSV for integration with other business systems

## Technical Architecture

**Tools & Technologies:**  
- **Framework:** Streamlit for interactive dashboard  
- **Forecasting Engine:** Facebook Prophet for time-series modeling  
- **Data Processing:** Pandas, NumPy  
- **Visualization:** Plotly for interactive charts  
- **Model Persistence:** Joblib for saving trained models  
- **Development Environment:** Jupyter Notebook for exploratory analysis  

**Key Features:**
- Automated monthly forecasting with confidence intervals
- Interactive visualization of trends and seasonality
- Export functionality for business intelligence integration
- Pre-trained model for immediate use
- Customizable forecast horizons for different planning needs

---

## Project Layout

```
Profit-Forecasting/
│
├── RetailAndSales/
│   ├── app.py                      # Main Streamlit application
│   ├── Sales.ipynb                 # Jupyter notebook for data exploration and model training
│   ├── Us_Retail_Sales.pkl         # Pre-trained forecasting model
│   ├── requirements.txt            # Python dependencies
│   └── README.md                   # Project documentation
│
├── LICENSE                         # MIT License
└── README.md                       # Main project documentation
```

## Data Source

* **Primary Dataset:** U.S. Census Bureau Monthly Retail Trade and Food Services (RSAFS) 
* **Direct Access:** [FRED Economic Data - RSAFS](https://fred.stlouisfed.org/series/RSAFS)
* **CSV Download:** [RSAFS.csv](https://fred.stlouisfed.org/graph/fredgraph.csv?id=RSAFS)
* **Frequency:** Monthly data suitable for seasonal trend analysis

## Output & Results

**Forecast Components:**
* **Prediction Table:** Monthly sales forecasts with upper/lower confidence bounds
* **Main Forecast Plot:** Interactive visualization of historical data and future predictions
* **Trend Analysis:** Decomposition of long-term growth/decline patterns
* **Seasonality Plots:** Weekly and yearly cyclical patterns in sales data

**Performance:** The model captures both trend and seasonal components, providing reliable forecasts for business planning with quantified uncertainty intervals.

---

## License

This project is licensed under the MIT License. See the LICENSE file for complete details.
