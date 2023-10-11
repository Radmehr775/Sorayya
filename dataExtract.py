
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("Bitstamp_AAVEBTC_1h.csv")

# x = [i for i in df["date"]]
# xAxis = []
# for data in range(len(x)):
#     cleanD = x[data].split(" ")
#     xAxis.append(cleanD[0])

# yAxis = [i for i in df["close"]]
# xAxis = xAxis[::-1]

# for j in range(len(yAxis)):
#     yAxis[j] = float(yAxis[j])
# plt.plot(xAxis, yAxis, color='black')
# plt.show()

from dataGetter import *
import pandas as pd

df = plot_candlestick_chart("BTC", "USDT", "kraken", 183, 1)
df.to_csv("bitcoin.csv", index=False)
