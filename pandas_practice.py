import pandas as pd 
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame 
import matplotlib.pyplot as plt
from matplotlib import style

# Adjusting the size of matplotlib
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))
mpl.__version__



start = datetime.datetime(2020,1,1)
end = datetime.datetime(2020,7,21)
 


# extract weekly data from stock, source, start date, end date
df = web.DataReader("BUX.CN", 'yahoo', start, end)
print(df)


#rolling mean (moving average) to determine trend
    # cut down noise in price chart and moving average could be resistance

close_px = df['Adj Close']
#windows = 100 : 100 days of stock closing price and take the average
# for each of the windows moving average 
mavg = close_px.rolling(window=100).mean()
print(mavg)




# Adjusting the style of matplotlib
style.use('ggplot')

#plt.plot(close_px)
#plt.show()

#plt.plot(mavg)
#plt.show()



#return deviation: det risk and return
# expected return measures mean of prob distribution of investment returns
# expected return of portolio = weight of each asset * expected return + values for each investment
# rt = pt1 - pt0 / pt0  = pt1/pt0 - 1 

rets = close_px/close_px.shift(1) -1 
plt.plot(rets)
plt.ylabel('Return Deviation')
plt.xlabel('Date')
plt.show()



#analyze competitors stocks