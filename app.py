import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Page title
st.title("📊 Crypto, Oil & Stock Market Analysis Dashboard")

# Connect database
conn = sqlite3.connect("market_analysis.db")

# Sidebar
st.sidebar.title("Navigation")
option = st.sidebar.selectbox(
    "Select Dataset",
    ("Cryptocurrencies", "Bitcoin Prices", "Oil Prices", "Stock Prices")
)

# -----------------------------
# CRYPTO DATA
# -----------------------------
if option == "Cryptocurrencies":

    st.header("Top Cryptocurrencies")

    query = """
    SELECT name, symbol, market_cap
    FROM cryptocurrencies
    ORDER BY market_cap DESC
    LIMIT 10
    """

    df = pd.read_sql(query, conn)

    st.dataframe(df)

    fig = px.bar(
        df,
        x="name",
        y="market_cap",
        title="Top 10 Cryptocurrencies by Market Cap"
    )

    st.plotly_chart(fig)


# -----------------------------
# BITCOIN
# -----------------------------
elif option == "Bitcoin Prices":

    st.header("Bitcoin Price Trend")

    query = "SELECT date, price_usd FROM bitcoin_prices"

    df = pd.read_sql(query, conn)

    fig = px.line(
        df,
        x="date",
        y="price_usd",
        title="Bitcoin Price Over Time"
    )

    st.plotly_chart(fig)


# -----------------------------
# OIL
# -----------------------------
elif option == "Oil Prices":

    st.header("Oil Price Trend")

    query = "SELECT Date, Price FROM oil_prices"

    df = pd.read_sql(query, conn)

    fig = px.line(
        df,
        x="Date",
        y="Price",
        title="Oil Price Over Time"
    )

    st.plotly_chart(fig)


# -----------------------------
# STOCKS
# -----------------------------
elif option == "Stock Prices":

    st.header("Stock Closing Prices")

    query = "SELECT Date, Close FROM stock_prices"

    df = pd.read_sql(query, conn)

    fig = px.line(
        df,
        x="Date",
        y="Close",
        title="Stock Market Trend"
    )

    st.plotly_chart(fig)