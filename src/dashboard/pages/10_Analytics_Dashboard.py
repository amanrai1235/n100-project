import streamlit as st
import pandas as pd
import requests
import plotly.express as px

BASE_URL = "http://127.0.0.1:8000/api/v1"

st.set_page_config(
    page_title="Analytics Dashboard",
    layout="wide"
)

st.title("📈 Financial Analytics Dashboard")

# ----------------------------
# Load Companies
# ----------------------------

companies = requests.get(
    f"{BASE_URL}/companies"
).json()

df = pd.DataFrame(companies)

# ----------------------------
# ROE Chart
# ----------------------------

if "roe_percentage" in df.columns:

    df["roe_percentage"] = (
        pd.to_numeric(df["roe_percentage"], errors="coerce")
        .fillna(0)
    )

    top_roe = (
        df.sort_values(
            "roe_percentage",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        top_roe,
        x="company_name",
        y="roe_percentage",
        title="Top 10 ROE Companies"
    )

    st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# ROCE Chart
# ----------------------------

if "roce_percentage" in df.columns:

    df["roce_percentage"] = (
        pd.to_numeric(df["roce_percentage"], errors="coerce")
        .fillna(0)
    )

    fig = px.scatter(
        df,
        x="roce_percentage",
        y="roe_percentage",
        hover_name="company_name",
        title="ROCE vs ROE"
    )

    st.plotly_chart(fig, use_container_width=True)

# ----------------------------
# Statistics
# ----------------------------

st.subheader("Dataset Statistics")

st.write(df.describe(include="all"))