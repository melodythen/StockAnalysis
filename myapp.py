import streamlit as st 
import yfinance as yf
import pandas as pd 
import yahoo_fin.stock_info as si
import time 
##MAIN BODY ##

st.header("Simple Stock Price Anaylzer")

tickerSymbol = ""
tickerSymbol = st.text_input("Input Stock Ticker")


st.markdown( tickerSymbol + " Stock")
if tickerSymbol != "" :
    st.text("Live Price of " + tickerSymbol + " :  $"+ str(si.get_live_price(tickerSymbol)))

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period= '1d', start= '2015-07-01', end = '2020-07-01')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

## END OF MAIN BODY ##

##SIDE BAR ##

raw_topwinners = si.get_day_gainers()
raw_toplosers = si.get_day_losers()
advancedinfo_proceed = False

tex = st.empty()


advancedinfo = st.sidebar.multiselect("Advanced Information", list(raw_toplosers.columns[1:]))
time.sleep(5)

advancedinfo_proceed = st.sidebar.checkbox("Apply")
button_reset = st.sidebar.checkbox("Reset")
st.sidebar.subheader("Top Gainers")
if advancedinfo and advancedinfo_proceed and not button_reset :
    topgainers_symb = pd.DataFrame(data = raw_topwinners[["Symbol"]])
    topgainers = pd.DataFrame(data= raw_topwinners[advancedinfo])
    st.sidebar.dataframe(data= pd.concat([topgainers_symb,topgainers], axis= 1))
    
elif button_reset or not advancedinfo or not advancedinfo_proceed:
    st.sidebar.dataframe(data = raw_topwinners[["Symbol","% Change"]].head(10))



st.sidebar.subheader("Top Losers")
toplosers = st.sidebar.dataframe(data = raw_toplosers[["Symbol","% Change"]].head(10), width = 400, height = 400)

##END OF SIDE BAR ##