import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Page Configuration
st.set_page_config(page_title="Jibin James Portfolio", layout="wide")

# Title and Introduction
st.title("📊 My Data Visualization Portfolio")
st.markdown("### Welcome to my portfolio page. Here I showcase my data analysis/visualization projects and skills")

# # Display the saved Power BI screenshot image
# st.subheader("📈 Power BI Report")
# st.image("images/wec_report.png", caption="Power BI Visualization", use_container_width=True)

# List of Power BI report image paths
report_images = [
    "images/wec_report.png",
    "images/gct_report.png"
]

# Insights for each report
report_insights = [
    "Energy Consumption Insights over various factors",
    "Cybersecurity incidents overview with financial loss breakdown and response times."
]

# Detailed insights for the "More Details" button
detailed_insights = [
    """
    **Detailed Insights**
    - This Power BI report visualizes energy consumption trends across various countries.
    - It highlights key metrics such as **coal**, **gas**, and **oil production**.
    - The report also demonstrates decade correlations with primary energy consumption.
    """,
    """
    **Detailed Insights**
    - Identifies security vulnerabilities by category.
    - Correlates incident response times with financial loss.
    - Suggests optimal defense mechanisms for future incidents.
    """
]

# Session state to track the current image index
if 'current_index' not in st.session_state:
    st.session_state['current_index'] = 0

# Navigation logic
col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    if st.button("⬅️ Previous") and st.session_state['current_index'] > 0:
        st.session_state['current_index'] -= 1

with col3:
    if st.button("Next ➡️") and st.session_state['current_index'] < len(report_images) - 1:
        st.session_state['current_index'] += 1

# Display the selected image and its insight
current_index = st.session_state['current_index']
st.image(report_images[current_index], caption=f"Report {current_index + 1}", use_container_width=True)
st.markdown(f"**Insight:** {report_insights[current_index]}")

# "More Details" button for additional insights
if st.button("More Details"):
    st.markdown(detailed_insights[current_index])

# "More Details" Button with Hidden Info
# if st.button("More Details"):
#     st.markdown("""
#     **Report Insights:**
#     - This Power BI report visualizes energy consumption trends across various countries.
#     - It highlights key metrics such as **coal**, **gas**, and **oil production**.
#     - The report also demonstrates decade correlations with primary energy consumption.
#     """)
#Space Mission report
st.markdown("### Here's something exciting that I tried today!")
st.image("images/SM_report.png", caption="Report", use_container_width=True)
st.markdown("**Insight:** Space mission details, including the cost and location analysis.")

st.markdown("### ⬇️Here are some other charts that I created")
st.write("")

# Data for top 5 songs
data = {
    "Song Name": [
        "Back to Friends", 
        "Ordinary", 
        "Golden", 
        "Just Keep Watching", 
        "Tears"
    ],
    "Total Streams (Millions)": [898.99, 1100, 692.77, 318.42, 134.99]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Layout
st.subheader("🎵 Top 5 Current Trending Songs")
st.write("Here are the most trending songs with their total streams:")

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

st.markdown("### Feel free to listen to some top tracks whilst you are here.")
if st.button("Click to Listen"):
    st.header("Top Songs of September 2025")
    st.markdown(
        """
        <iframe src="https://open.spotify.com/embed/playlist/4FzLms9h928aX5UaHgoXHv" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
        """,
        unsafe_allow_html=True,
    )
st.write("")

#Programming languages viz
st.subheader("📟 Programming Languages Market Share - September 2025")
def plot_language_share():
    data = {
        'Language': ['Python', 'C++', 'C', 'Java', 'C#', 'JavaScript', 'Visual Basic', 'Go', 'Delphi/Object Pascal', 'Perl'],
        'Share': [25.98, 8.80, 8.65, 8.35, 6.38, 3.22, 2.84, 2.32, 2.26, 2.03]
    }

    fig = px.pie(
        data, 
        names='Language', 
        values='Share', 
        title='Programming Language Market Share (September 2025)',
        hole=0.3,
        width=500,  # Reduced size
        height=400   # Reduced size
    )

    st.plotly_chart(fig)
plot_language_share()

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
    - **Experience**: 1 year & 4 months
    - **Expertise**: Data and AI
    - **Qualification**: Master of Computer Applications (MCA)
    - **Skills**: SQL, SSAS, Excel, Power BI, Python, AI/ML
    """)

# Project Links
st.sidebar.title("🔗 Links")
st.sidebar.markdown("- [GitHub Repo](https://github.com/jibinjamesjj)")
st.sidebar.markdown("- [Certifications](https://drive.google.com/drive/folders/1jNAAu1mnxrHEP4BWUQNOVSyDwvI9OfKX)")
st.sidebar.markdown("- [LinkedIn Profile](https://www.linkedin.com/in/jibin-james-58984b143/)")

# Footer
st.markdown("---")
st.markdown("**© 2025 Jibin James - Data Analyst | Visualization Specialist**")
