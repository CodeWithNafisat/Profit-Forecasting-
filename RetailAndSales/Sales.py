import pandas as pd
import joblib
import streamlit as st
from prophet.plot import plot_plotly
import plotly.express as ex

@st.cache_resource
def load_model():
    return joblib.load('Us_Retail_Sales.pkl')
model = load_model()

st.title('📈 Profit Forecasting App')
st.header('Time Series for Retail & food services Sales in millions of USD')

st.sidebar.markdown('Use the sidebar slider to choose how many months (1–36) you want to forecast.')
periods = st.sidebar.slider('Select Months to Forecast', min_value = 1, max_value = 36, value = 12)
st.sidebar.subheader('Note')
st.sidebar.markdown('My app utilizes a time series forecasting model trained on the US Retail and Food Services Sales (RSAFS) which track monthly retail stores and food Services in united State. My app provides accurate and informative predictions to help business and individuals make informed decisions.')

st.write('Click the “Run forecast” button to generate predictions.')    
if st.button('Run forecast'):
    future = model.make_future_dataframe(periods = periods, freq = 'M')
    forecast = model.predict(future)

    st.subheader(f'Forecast for the next {periods} Month')
    st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods))
    csv = forecast.to_csv(index = False).encode('utf-8')
    st.write('Download results as a CSV file for further offline analysis.')
    st.download_button('Download Csv file', data = csv, file_name = "forecast_rsafs.csv", mime = "text/csv")

    fig =  plot_plotly(model, forecast)
    fig.update_layout(title_text = 'Retail & food services Sales in millions of USD', xaxis_title = 'Year', yaxis_title = 'Sales', plot_bgcolor="white")
    st.plotly_chart(fig, use_container_width = True)

    st.subheader('Explore trend and seasonality plots to understand sales behavior.')
    st.write('Trend and seasonality Plot')
    fig2 = model.plot_components(forecast)
    fig2.title_text = 'Trend and Yearly Seasonality'
    st.pyplot(fig2)

    st.markdown('Trend: is the long term directional movement, it either it is increasing or decreasing in sales.')
    st.markdown('Yerly Seasonality: repeating pattern within a year. Example: Holiday spike (sales increasing during holiday)')
    

