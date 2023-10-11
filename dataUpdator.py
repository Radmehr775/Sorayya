
import pandas as pd
from datetime import datetime
from dataGetter import *

symbol = "BTC"
currency = "USDT"
exchange = "kraken"

try:
    frmt = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    now = now.strftime('%Y-%m-%d %H:%M')+":00"
    df = pd.read_csv(symbol + ".csv")
    last = df['time'].iloc[-1]

    if datetime.strptime(now, frmt) != datetime.strptime(last, frmt):
        diff = int(datetime.timestamp(datetime.strptime(now, frmt))) - \
            int(datetime.timestamp(datetime.strptime(last, frmt)))
        diff = diff / 60

        update = plot_candlestick_chart(symbol, currency,
                                        exchange, limit=int(diff), num=1)
        update.to_csv("{}.csv".format(symbol), mode="a",
                      header=False, index=False)
except:
    print("dust aziz data nagerefti olaq")
    df = plot_candlestick_chart(symbol, currency, exchange)
    df.to_csv("{}.csv".format(symbol), index=False)
finally:
    print(df.describe())
