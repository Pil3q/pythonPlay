class Trade:
    def __init__(self, instrument, price, quantity, date, reference):
        self.instrument = instrument
        self.price = price
        self.quantity = quantity
        self.date = date
        self.reference = reference
        self.marketVal = price * quantity

import csv

with open('sampletrades.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    trades = []
    for row in readCSV:
        trades.append(Trade(row[0], float(row[1]), float(row[2]), row[3], row[4]))

#this will give us market value of trade
print trades[0].marketVal
#total market val for instrument
instrumentName = 'option'
instruments = [trade for trade in trades if trade.instrument == instrumentName]
marketValues = [trade.marketVal for trade in instruments]
#maybe closing price * number of instruments on the market(where from?)
total = sum(marketValues)
print total
# average price for the day
filteredByDate = [trade for trade in instruments if trade.date[0:10] == '2017/10/10']
prices = [trade.price for trade in filteredByDate]
averagePrice = sum(prices)/len(prices)
print averagePrice
#closing price of the day
tradeTimes = [int(trade.date[11:13] + trade.date[14:16]) for trade in filteredByDate]
closingTime = max(tradeTimes)
closingTrade = [trade for trade in filteredByDate if int(trade.date[11:13] + trade.date[14:16]) == closingTime]
closingPrice = closingTrade[0].price
print closingPrice
#constituent trades??
reference = 'XZ126'
byReference = [trade for trade in trades if trade.reference == reference]
print byReference
#for each day traded value
date = '2017/10/11'
forEachDay = [trade for trade in trades if trade.date[0:10] == date]
tradedValues = [trade.marketVal for trade in forEachDay]
totalForDay = sum(tradedValues)
print totalForDay
#closing price for the day (from all trades)
closingTimesForDay = [int(trade.date[11:13] + trade.date[14:16]) for trade in forEachDay]
closingTimeForDay = max(closingTimesForDay)
closingTradeForDay = [trade for trade in forEachDay if int(trade.date[11:13] + trade.date[14:16]) == closingTimeForDay]
closingPriceForDay = closingTradeForDay[0].price
print closingPriceForDay
# closing position?
print closingTradeForDay
