import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('my_tickers_last_30_days.csv')
df['Datetime'] = df['Datetime'].map(pd.to_datetime)
df.index = df['Datetime']

df_7_24 = df.loc['2020-07-24',:]

msft = df_7_24[df_7_24['Ticker']=='MSFT']['Open'].resample('T').mean()
jd = df_7_24[df_7_24['Ticker']=='JD']['Open'].resample('T').mean()
uber = df_7_24[df_7_24['Ticker']=='UBER']['Open'].resample('T').mean()
snap = df_7_24[df_7_24['Ticker']=='SNAP']['Open'].resample('T').mean()
nio = df_7_24[df_7_24['Ticker']=='NIO']['Open'].resample('T').mean()
huya = df_7_24[df_7_24['Ticker']=='HUYA']['Open'].resample('T').mean()

plt.subplot(2,3,1)
plt.plot(msft)

plt.subplot(2,3,2)
plt.plot(jd)

plt.subplot(2,3,3)
plt.plot(uber)

plt.subplot(2,3,4)
plt.plot(snap)

plt.subplot(2,3,5)
plt.plot(nio)

plt.subplot(2,3,6)
plt.plot(huya)

plt.show()