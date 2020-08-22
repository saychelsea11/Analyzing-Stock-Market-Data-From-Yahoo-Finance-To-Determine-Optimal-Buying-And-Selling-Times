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

fig, ax = plt.subplots(2,3)
ax = ax.flatten()
print (ax)

#Explanation of how the 'ax' container works with plt.subplots
#https://stackoverflow.com/questions/37967786/axes-from-plt-subplots-is-a-numpy-ndarray-object-and-has-no-attribute-plot

ax[0].plot(msft)
ax[0].set_title('Microsoft stock trend on 7-24-20')
ax[0].set_xlabel('Time (min)')
ax[0].set_ylabel('Stock price ($)')
ax[0].axvline(pd.to_datetime('7-24-20 15:00'),color='red',label='11am')
ax[0].axvline(pd.to_datetime('7-24-20 19:00'),color='green',label='3pm')
ax[0].legend(loc='lower center')

#plt.subplot(2,3,2)
ax[1].plot(jd)
ax[1].set_title('JD.com stock trend on 7-24-20')
ax[1].set_xlabel('Time (min)')
ax[1].set_ylabel('Stock price ($)')
ax[1].axvline(pd.to_datetime('7-24-20 15:00'),color='red',label='11am')
ax[1].axvline(pd.to_datetime('7-24-20 19:00'),color='green',label='3pm')
ax[1].legend(loc='lower center')

#plt.subplot(2,3,3)
ax[2].plot(uber)
ax[2].set_title('Uber stock trend on 7-24-20')
ax[2].set_xlabel('Time (min)')
ax[2].set_ylabel('Stock price ($)')
ax[2].axvline(pd.to_datetime('7-24-20 15:00'),color='red',label='11am')
ax[2].axvline(pd.to_datetime('7-24-20 19:00'),color='green',label='3pm')
ax[2].legend(loc='lower center')

#plt.subplot(2,3,4)
ax[3].plot(snap)
ax[3].set_title('Snap stock trend on 7-24-20')
ax[3].set_xlabel('Time (min)')
ax[3].set_ylabel('Stock price ($)')
ax[3].axvline(pd.to_datetime('7-24-20 15:00'),color='red',label='11am')
ax[3].axvline(pd.to_datetime('7-24-20 19:00'),color='green',label='3pm')
ax[3].legend(loc='lower center')

#plt.subplot(2,3,5)
ax[4].plot(nio)
ax[4].set_title('NIO stock trend on 7-24-20')
ax[4].set_xlabel('Time (min)')
ax[4].set_ylabel('Stock price ($)')
ax[4].axvline(pd.to_datetime('7-24-20 15:00'),color='red',label='11am')
ax[4].axvline(pd.to_datetime('7-24-20 19:00'),color='green',label='3pm')
ax[4].legend(loc='lower center')

#plt.subplot(2,3,6)
ax[5].plot(huya)
ax[5].set_title('Huya stock trend on 7-24-20')
ax[5].set_xlabel('Time (min)')
ax[5].set_ylabel('Stock price ($)')
ax[5].axvline(pd.to_datetime('7-24-20 15:00'),color='red',label='11am')
ax[5].axvline(pd.to_datetime('7-24-20 19:00'),color='green',label='3pm')
ax[5].legend(loc='lower center')

#plt.tight_layout(w_pad=0.1)

#handles, labels = ax.get_legend_handles_labels()
#ax.legend(handles, labels, loc='upper center')

plt.show()