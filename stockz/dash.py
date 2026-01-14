

# ============================================================================
# SECTION 1: IMPORT LIBRARIES
# ============================================================================

import streamlit as st      # Web app framework - builds interface
import pandas as pd         # Data tables (like Excel in Python)
import plotly.express as px # Simple interactive charts

# ============================================================================
# SECTION 2: PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Clinic Risk Dashboard",
    
    layout="wide"

)

# ============================================================================
# SECTION 3: DATA
# ============================================================================

page_bg = """
<style>
.stApp {
    background-color: #3a5311; 
}
body, .stApp {
    color: black;  
}
</style>
h1 {
    text-align: center;
    color: #f0f8ff;  
}

"""
st.markdown(page_bg, unsafe_allow_html=True)




# Define the risk assessment table as a dictionary
data = {
    "Risk Area": [
        "Ransomware",
        "Phishing",
        "Outdated Medical Devices",
        "Insider Threats",
        "Physical Theft",
        "Natural Disasters / Power Outages"
    ],
    "Description": [
        "Malicious software could lock systems and demand payment.",
        "Fake emails or messages tricking staff into revealing credentials.",
        "Older devices lack updates, vulnerable to attack.",
        "Employees mishandle or misuse data.",
        "Portable devices or equipment stolen with data on them.",
        "Storms or outages could disrupt clinical operations."
    ],
    "Impact": ["Very High", "High", "High", "High", "Medium", "Very High"],
    "Likelihood": ["Medium-High", "High", "Medium", "Medium", "Medium", "Low"],
    "Risk Level": ["High", "High", "Medium", "Medium", "Medium", "Medium"],
    "Compliance": [
        "HIPAA, NIST",
        "HIPAA, NIST",
        "HITECH, NIST",
        "HIPAA, NIST",
        "HITECH, State Laws",
        "OSHA, NIST"
    ]
}

df = pd.DataFrame(data)

# ============================================================================
# SECTION 4: DASHBOARD LAYOUT
# ============================================================================

# Title and intro
st.title("Clinic Risk Assessment Dashboard Demo")
st.markdown("This dashboard displays cybersecurity risks for a medical clinic. "
            "Use the filters and chart to explore risk levels.")

st.markdown("---")

# -----------------------
# Risk Table with Filter
# -----------------------
st.header("Risk Table")

# Dropdown filter
choice = st.selectbox("Filter by Risk Level:", ["All", "High", "Medium", "Low"])

if choice != "All":
    filtered_df = df[df["Risk Level"] == choice]
else:
    filtered_df = df

# Show the filtered table
# st.dataframe(filtered_df)
st.dataframe(filtered_df, use_container_width=True, height=300)


st.markdown("---")

# -----------------------
# Bar Chart Visualization
# -----------------------
st.header("Risks by Level")

risk_counts = df["Risk Level"].value_counts().reset_index()
risk_counts.columns = ["Risk Level", "Count"]

# Create chart
fig = px.bar(
    risk_counts,
    x="Risk Level",
    y="Count",
    color="Risk Level",
    title="Number of Risks by Level",
    text="Count",
    color_discrete_map={
        "High": "red",
        "Medium": "orange",
        "Low": "green"
    }
)

# Show chart
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# -----------------------
# Details Section
# -----------------------
st.header("Detailed Risk Information")

for i, row in df.iterrows():
    with st.expander(f"{row['Risk Area']} ({row['Risk Level']})"):
        st.write(f"**Description:** {row['Description']}")
        st.write(f"**Impact:** {row['Impact']}")
        st.write(f"**Likelihood:** {row['Likelihood']}")
        st.write(f"**Compliance:** {row['Compliance']}")

