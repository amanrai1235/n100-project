import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI Financial Insights",
    layout="wide"
)

st.title("🤖 AI Financial Insights Dashboard")

# ----------------------------

portfolio = pd.DataFrame({

    "Company":[
        "TCS",
        "INFY",
        "HDFCBANK",
        "ICICIBANK",
        "RELIANCE",
        "LT",
        "ITC"
    ],

    "Investment":[
        100000,
        80000,
        90000,
        75000,
        110000,
        65000,
        70000
    ],

    "Current Value":[
        122000,
        91000,
        88000,
        79000,
        126000,
        62000,
        76000
    ]

})

portfolio["Profit"] = (
    portfolio["Current Value"]
    - portfolio["Investment"]
)

portfolio["Return %"] = (
    portfolio["Profit"]
    /
    portfolio["Investment"]
)*100

# ----------------------------

def recommendation(r):

    if r >= 20:
        return "BUY"

    elif r >= 5:
        return "HOLD"

    return "SELL"

portfolio["Recommendation"] = portfolio["Return %"].apply(recommendation)

# ----------------------------

average_return = portfolio["Return %"].mean()

if average_return >= 15:
    health = 95
elif average_return >= 10:
    health = 80
elif average_return >= 5:
    health = 65
else:
    health = 45

# ----------------------------

st.metric(
    "Portfolio Health Score",
    f"{health}/100"
)

# ----------------------------

st.subheader("AI Recommendations")

st.dataframe(portfolio)

# ----------------------------

buy = (portfolio["Recommendation"]=="BUY").sum()
hold = (portfolio["Recommendation"]=="HOLD").sum()
sell = (portfolio["Recommendation"]=="SELL").sum()

fig = px.pie(

    values=[buy,hold,sell],

    names=["BUY","HOLD","SELL"],

    title="AI Recommendation Distribution"

)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------

top = portfolio.sort_values(
    "Return %",
    ascending=False
)

st.subheader("Top Performing Stocks")

st.dataframe(top.head())

# ----------------------------

worst = portfolio.sort_values(
    "Return %"
)

st.subheader("Weak Performing Stocks")

st.dataframe(worst.head())

# ----------------------------

st.subheader("Executive Summary")

st.success(f"""
Portfolio Health Score : {health}/100

Average Return : {average_return:.2f} %

BUY Recommendations : {buy}

HOLD Recommendations : {hold}

SELL Recommendations : {sell}

Overall portfolio performance is stable.
""")