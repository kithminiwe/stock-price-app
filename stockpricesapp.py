import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.write("""
# Stock Price App

Shown are the stock **closing price** and ***volume*** of some high tech companies!
""")

# define the ticker symbol
tickerSymbol = 'MSFT AAPL GOOG'
symbols = tickerSymbol.split(' ')

# get data on this ticker
df = yf.download(tickerSymbol,period="10y",group_by="ticker")

# df.info

col1, col2 = st.columns(2)

for symbol in symbols:
    col1.subheader("Closing Price of "+symbol)
    col1.line_chart(df[symbol].Close)
    
    col2.subheader("Volume Price of "+symbol)
    col2.line_chart(df[symbol].Volume)
    
