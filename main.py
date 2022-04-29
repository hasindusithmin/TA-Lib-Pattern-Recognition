import requests
from pandas import DataFrame
from talib import CDLDOJI
def myfn(cc,tf):
    # cc:currency_cross | tf:timeframe
    url = f'https://forex-codeunity.herokuapp.com/yahoo/history/{cc}?interval={tf}'
    r = requests.get(url)
    return r.json()

candles = myfn(cc='eurusd',tf='5m')
df = DataFrame(candles)

integer = eval("CDLDOJI(df['Open'], df['High'], df['Low'], df['Close'])")
index = list(integer[integer != 0].index)
points = []
for i in index:
    points.append(int(df.iloc[i].Datetime / 1000 + 19800))
print(points)