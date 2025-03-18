import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Page Configuration
st.set_page_config(page_title="Jibin James Portfolio", layout="wide")

# Title and Introduction
st.title("📊 My Data Visualization Portfolio")
st.markdown("### Welcome to my portfolio page. Here I showcase my data analysis/visualization projects and skills")

# Display the saved Power BI screenshot image
st.subheader("📸 Power BI Visualization Sample")
st.image("images/sample_viz.png", caption="Power BI Visualization", use_column_width=True)

# Sample Dataset
@st.cache_data
def load_data():
    data = pd.DataFrame({
        'Date': pd.date_range(start='2024-01-01', periods=12, freq='M'),
        'Energy Consumption (kWh)': [300, 450, 500, 600, 700, 800, 650, 750, 850, 900, 1000, 1100]
    })
    return data

df = load_data()

# Visualization - Line Chart
st.subheader("📈 World Energy Consumption - Analysis")
fig = px.line(df, x='Date', y='Energy Consumption (kWh)', title='Monthly Energy Consumption')
st.plotly_chart(fig, use_container_width=True)

# Data Table
st.subheader("🗂️ Data Table")
st.dataframe(df)

# Project Links
st.sidebar.title("🔗 Project Links")
st.sidebar.markdown("- [GitHub Repo](https://github.com/jibinjamesjj)")
st.sidebar.markdown("- [LinkedIn Profile](https://www.linkedin.com/in/jibin-james-58984b143/)")

# Footer
st.markdown("---")
st.markdown("**© 2025 Jibin James - Data Analyst | Visualization Specialist**")
