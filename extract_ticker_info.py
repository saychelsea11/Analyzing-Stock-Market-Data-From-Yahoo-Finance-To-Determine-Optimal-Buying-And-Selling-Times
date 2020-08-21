import pandas as pd
import yfinance as yf

tickers = ['MSFT','JD','SNAP','NIO','ELF','HUYA','UBER']
count = 0
for i in tickers:
	ticker_list = []
	ticker_list.append(i)
	current_ticker = yf.Ticker(i)
	data1 = current_ticker.history(start='2020-07-24',end='2020-07-31',interval='1m')
	data2 = current_ticker.history(start='2020-08-01',end='2020-08-07',interval='1m')
	data3 = current_ticker.history(start='2020-08-08',end='2020-08-15',interval='1m')
	count = count + 1
	print (i)
	if count==1:
		data1 = (data1).append(data2).append(data3)
		data1['Ticker'] = ticker_list*len(data1)
		df = data1
	else:
		data1 = (data1).append(data2).append(data3)
		data1['Ticker'] = ticker_list*len(data1)
		df = df.append(data1)
	
df.to_csv('my_tickers_last_30_days.csv')
	