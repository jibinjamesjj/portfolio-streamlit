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

st.markdown("### ⬇️Here are some other charts that I created")

# Data for top 5 songs
data = {
    "Song Name": [
        "Die With a Smile", 
        "APT.", 
        "Seven", 
        "Flowers", 
        "luther (with sza)"
    ],
    "Total Streams (Millions)": [2238, 1000, 2236, 2236, 1000]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Layout
st.subheader("🎵 Top 5 Trending Songs - March 2025")
st.write("Here are the most streamed songs of March 2025 with their total streams:")

# Two-column layout for organized display
col1, col2 = st.columns([1, 1])  # Adjust ratios to manage width

with col1:
    st.write("💽 Total Streams (in Millions)")
    # Horizontal Bar Chart
    fig = px.bar(
        df, 
        x="Total Streams (Millions)", 
        y="Song Name", 
        orientation='h',  # Horizontal bar chart
        text="Total Streams (Millions)",
        color="Song Name",  # Optional for colorful chart
    )
    fig.update_traces(textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Centered Content
    st.markdown(
        """
        <div style="display: flex; height: 100%; align-items: center; 
                    justify-content: center; text-align: center; 
                    flex-direction: column;">
            <p>Oh! And while you skim through the portfolio, <br>
            you can click below and listen to the top tracks.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Centered Button
    centered_button = st.columns([3, 1, 3])  # Creates space to align the button in the center
    with centered_button[1]: 
        if st.button("🎧 Listen here"):
            st.markdown(
                """
                <div style="display: flex; justify-content: center;">
                    <iframe src="https://open.spotify.com/embed/playlist/4FzLms9h928aX5UaHgoXHv" 
                            width="300" height="380" frameborder="0" 
                            allowtransparency="true" allow="encrypted-media">
                    </iframe>
                </div>
                """,
                unsafe_allow_html=True
            )# # Bar Chart Visualization
# st.subheader("💽 Total Streams (in Millions)")
# st.bar_chart(df.set_index("Song Name"), title="💽 Total Streams (in Millions)")

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
