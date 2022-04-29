
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import uvicorn
from fns import myfn

# valid data
valid_func = ['cdl2crows', 'cdl3blackcrows', 'cdl3inside', 'cdl3linestrike', 'cdl3outside', 'cdl3starsinsouth', 'cdl3whitesoldiers', 'cdlabandonedbaby', 'cdladvanceblock', 'cdlbelthold', 'cdlbreakaway', 'cdlclosingmarubozu', 'cdlconcealbabyswall', 'cdlcounterattack', 'cdldarkcloudcover', 'cdldoji', 'cdldojistar', 'cdldragonflydoji', 'cdlengulfing', 'cdleveningdojistar', 'cdleveningstar', 'cdlgapsidesidewhite', 'cdlgravestonedoji', 'cdlhammer', 'cdlhangingman', 'cdlharami', 'cdlharamicross', 'cdlhighwave', 'cdlhikkake', 'cdlhikkakemod', 'cdlhomingpigeon', 'cdlidentical3crows', 'cdlinneck', 'cdlinvertedhammer', 'cdlkicking', 'cdlkickingbylength', 'cdlladderbottom', 'cdllongleggeddoji', 'cdllongline', 'cdlmarubozu', 'cdlmatchinglow', 'cdlmathold', 'cdlmorningdojistar', 'cdlmorningstar', 'cdlonneck', 'cdlpiercing', 'cdlrickshawman', 'cdlrisefall3methods', 'cdlseparatinglines', 'cdlshootingstar', 'cdlshortline', 'cdlspinningtop', 'cdlstalledpattern', 'cdlsticksandwich', 'cdltakuri', 'cdltasukigap', 'cdlthrusting', 'cdltristar', 'cdlunique3river', 'cdlupsidegap2crows', 'cdlxsidegap3methods']
valid_cross = ['eurusd', 'usdjpy', 'gbpusd', 'audusd', 'nzdusd', 'eurjpy', 'gbpjpy', 'eurgbp', 'eurcad', 'eursek', 'eurchf', 'eurhuf', 'eurjpy', 'usdcny', 'usdhkd', 'usdsgd', 'usdinr', 'usdmxn', 'usdphp', 'usdidr', 'usdthb', 'usdmyr', 'usdzar', 'usdrub']
valid_frame = ['5m','15m','30m','60m','1h']

# create app
app = FastAPI()

@app.get('/')
def root():
    return RedirectResponse('/docs')

@app.get('/point/{cross}/{frame}/{func}')
async def point(cross:str,frame:str,func:str):
    if cross not in valid_cross:
        raise HTTPException(status_code=403,detail="Incorrect currency cross")
    if frame not in valid_frame:
        raise HTTPException(status_code=403,detail="Incorrect timeframe")
    if func not in valid_func:
        raise HTTPException(status_code=403,detail="Incorrect function")
    return myfn(cc=cross, tf=frame, fn=func.upper())







