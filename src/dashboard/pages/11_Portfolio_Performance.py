import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Portfolio Dashboard",
    layout="wide"
)

st.title("📈 Portfolio Performance Dashboard")

# Sample Portfolio

portfolio = pd.DataFrame({

    "Company":[
        "TCS",
        "INFY",
        "HDFCBANK",
        "RELIANCE",
        "ICICIBANK",
        "LT",
        "ITC"
    ],

    "Investment":[
        150000,
        120000,
        100000,
        90000,
        80000,
        70000,
        60000
    ],

    "Current Value":[
        175000,
        128000,
        115000,
        98000,
        83000,
        72000,
        63000
    ]

})

portfolio["Profit"] = (
    portfolio["Current Value"]
    - portfolio["Investment"]
)

portfolio["Return %"] = (
    portfolio["Profit"]
    / portfolio["Investment"]
) * 100

# -----------------------

st.subheader("Portfolio")

st.dataframe(portfolio)

# -----------------------

total_investment = portfolio["Investment"].sum()
total_value = portfolio["Current Value"].sum()
total_profit = portfolio["Profit"].sum()

col1,col2,col3 = st.columns(3)

col1.metric(
    "Investment",
    f"₹{total_investment:,.0f}"
)

col2.metric(
    "Current Value",
    f"₹{total_value:,.0f}"
)

col3.metric(
    "Profit",
    f"₹{total_profit:,.0f}"
)

# -----------------------

pie = px.pie(

    portfolio,

    names="Company",

    values="Current Value",

    title="Portfolio Allocation"

)

st.plotly_chart(
    pie,
    use_container_width=True
)

# -----------------------

bar = px.bar(

    portfolio,

    x="Company",

    y="Return %",

    color="Return %",

    title="Returns by Company"

)

st.plotly_chart(
    bar,
    use_container_width=True
)