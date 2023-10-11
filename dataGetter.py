
import cryptocompare
import plotly.graph_objs as go
from datetime import datetime
from datetime import timedelta
import pandas as pd


def plot_candlestick_chart(symbol, currency, exchange, limit=2000, num=5):
    # Fetch historical data
    rea = []
    data = []
    data.append(cryptocompare.get_historical_price_minute(
        symbol, currency=currency, exchange=exchange, limit=limit))

    for i in range(num):
        datescon = [datetime.fromtimestamp(day['time']) for day in data[i]]

        start_timestamp = int(datetime.strptime(
            str(datescon[0]), '%Y-%m-%d %H:%M:%S').timestamp())
        data.append(cryptocompare.get_historical_price_minute(
            symbol, currency=currency, exchange=exchange, limit=limit, toTs=start_timestamp))
        data[i].remove(data[i][-1])
        rea[:0] = data[i]
    df = pd.DataFrame(rea)

    # Format data for plotting
    dates = [datetime.fromtimestamp(day['time']) for day in rea]
    # ohlcv = go.Candlestick(x=dates,
    #                        open=[day['open'] for day in rea],
    #                        high=[day['high'] for day in rea],
    #                        low=[day['low'] for day in rea],
    #                        close=[day['close'] for day in rea])

    df["time"] = dates
    # df.to_csv("{}.csv".format(symbol))

    return df


# if __name__ == '__main__':
#     symbol = 'BTC'  # specify the cryptocurrency symbol here
#     currency = 'USDT'  # specify the currency to use here
#     exchange = 'kraken'  # specify the exchange to use here
#     plot_candlestick_chart(symbol, currency, exchange)
