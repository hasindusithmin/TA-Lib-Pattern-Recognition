import requests
from pandas import DataFrame
from talib import *

def myfn(cc,tf,fn):
    # cc:currency_cross | tf:timeframe
    url = f'https://forex-codeunity.herokuapp.com/yahoo/history/{cc}?interval={tf}'
    r = requests.get(url)
    df = DataFrame(r.json())
    integer = eval(f"{fn}(df['Open'], df['High'], df['Low'], df['Close'])")
    index = list(integer[integer != 0].index)
    points = []
    for i in index:
        points.append(int(df.iloc[i].Datetime / 1000 + 19800))
    return points




