# Title 

Analyzing-Stock-Market-Data-From-Yahoo-Finance-To-Determine-Optimal-Buying-And-Selling-Times

# Goal

To find the best buying and selling times during a trading day

# Hypothesis

- We already know that the highest trading activity occurs between the opening time of 9:30am and 11:00am on any given trading day. 
- From a qualitative viewpoint, I expect stocks to move in the opposite direction of the what the trend was during the opening 1.5hrs of trading. I expect the change in trend to go on till around 3pm before slightly reversing once more till the closing time of 4pm. 
- If we can prove that this theory is in fact somewhat accurate, crucial trading decisions can be made more reliably. 

# Data

- The data was collected using the *yfinance* library in Python created by Ran Aroussi. 
-- https://aroussi.com/post/python-yahoo-finance
- Data was extracted with an interval of 1min spanning 30 days for the following tickers
  - MSFT
  - JD
  - NIO
  - HUYA
  - ELF
  - UBER
  - SNAP

