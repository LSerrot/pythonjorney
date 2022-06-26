#### SIMPLE STOCK PRICE #### ENTENDI MUITO POUCO DISSO AQUI...

import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""

## ACOMPANHADOR DE PREÇOS DA GOOGLE

Será que essa porra ainda vai dar errado um dia?
""")

# define the ticker symbol
tickerSymbol = 'GOOGL'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDF = tickerData.history(period = '1d', start = '2010-5-31', end = '2022-12-30')

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)