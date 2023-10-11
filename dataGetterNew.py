import requests
import pandas as pd
import time


def fetch_historical_minute_data(crypto_symbol, limit=1000):
    """
    Fetch historical minute data for a given cryptocurrency from the Binance exchange.

    Parameters:
        crypto_symbol (str): The symbol of the cryptocurrency (e.g., "BTCUSDT" for Bitcoin/USDT).
        limit (int): The maximum number of data points to retrieve per API call (default is 1000).

    Returns:
        pandas.DataFrame: A DataFrame containing historical minute data.
    """
    base_url = 'https://api.binance.com/api/v3/klines'
    all_data = []

    # Get the current timestamp in milliseconds
    current_timestamp = int(time.time() * 1000)

    # Set the start timestamp to 1000 days ago
    start_timestamp = current_timestamp - (10 * 24 * 60 * 60 * 365)
    req = 1
    while start_timestamp < current_timestamp:
        print(req)

        # Fetch historical data for the specified time interval
        params = {
            'symbol': crypto_symbol,
            'interval': '1m',  # 1-minute interval
            'limit': limit,
            'startTime': start_timestamp,
        }
        response = requests.get(base_url, params=params)
        data = response.json()
        req = req + 1

        if not data:
            break

        all_data.extend(data)

        # Get the timestamp of the last data point to continue from the next interval
        last_timestamp = all_data[-1][0]

        # Add a small delay to respect the API rate limits
        time.sleep(1)

        # Update the start timestamp for the next iteration (move forward in time)
        # Add one minute to the last timestamp
        start_timestamp = last_timestamp + 60 * 1000

    df = pd.DataFrame(all_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time',
                                         'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume',
                                         'taker_buy_quote_asset_volume', 'ignore'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    df.to_csv(f"{crypto_symbol}.csv")

    return df


if __name__ == "__main__":
    # Replace "BTCUSDT" with the desired cryptocurrency pair (e.g., "ETHUSDT" for Ethereum/USDT)
    crypto_symbol = "XRPUSDT"
    historical_data = fetch_historical_minute_data(crypto_symbol)

    if historical_data is not None:
        print(historical_data.head())
