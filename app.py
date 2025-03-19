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
st.subheader("📈 Power BI Report")
st.image("images/wec_report.png", caption="Power BI Visualization", use_container_width=True)

# "More Details" Button with Hidden Info
if st.button("More Details"):
    st.markdown("""
    **Report Insights:**
    - This Power BI report visualizes energy consumption trends across various countries.
    - It highlights key metrics such as **coal**, **gas**, and **oil production**.
    - The report also demonstrates decade correlations with primary energy consumption.
    """)

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

#📸

# Data Table
st.subheader("🗂️ Data Table")
st.dataframe(df)

#Bio
st.sidebar.title("🧑‍💻 Profile")
st.sidebar.markdown("**JIbin James (Data Analyst)**")
st.sidebar.markdown("""
    Hi there, I am a Power BI Developer and analyst.
    - **Experience**: 11 months
    - **Current Position**: AI/ML Intern
    - **Company**: Zummit Infolabs
    - **Skills**: SQL, SSAS, Excel, Power BI, Python, AI/ML
    """)

# Project Links
st.sidebar.title("🔗 Links")
st.sidebar.markdown("- [GitHub Repo](https://github.com/jibinjamesjj)")
st.sidebar.markdown("- [LinkedIn Profile](https://www.linkedin.com/in/jibin-james-58984b143/)")

# Footer
st.markdown("---")
st.markdown("**© 2025 Jibin James - Data Analyst | Visualization Specialist**")
