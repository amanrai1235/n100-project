import streamlit as st
import pandas as pd
import requests

BASE_URL = "http://127.0.0.1:8000/api/v1"

st.set_page_config(
    page_title="Financial API Dashboard",
    layout="wide"
)

st.title("📊 Financial Intelligence Dashboard")

# ----------------------------
# Companies
# ----------------------------

st.header("Companies")

companies = requests.get(
    f"{BASE_URL}/companies"
).json()

df = pd.DataFrame(companies)

st.write("Total Companies:", len(df))
st.dataframe(df)

# ----------------------------
# Screener
# ----------------------------

st.header("Stock Screener")

roe = st.slider(
    "Minimum ROE",
    0,
    50,
    15
)

opm = st.slider(
    "Minimum OPM",
    0,
    50,
    10
)

screened = requests.get(
    f"{BASE_URL}/screener",
    params={
        "min_roe": roe,
        "min_opm": opm
    }
).json()

st.write("Matching Companies:", len(screened))
st.dataframe(pd.DataFrame(screened))

# ----------------------------
# Sector Summary
# ----------------------------

st.header("Sector Summary")

sector = requests.get(
    f"{BASE_URL}/sectors"
).json()

st.dataframe(pd.DataFrame(sector))