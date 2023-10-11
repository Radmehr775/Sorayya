
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential

df = pd.read_csv("BTC.csv")

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_df = scaler.fit_transform(df["close"].values.reshape(-1, 1))

X_train, y_train = [], []
for x in range(60, len(scaled_df)):
    X_train.append(scaled_df[x-60:x, 0])
    y_train.append(scaled_df[x, 0])
X_train, y_train = np.array(X_train), np.array(y_train)
X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))

model = Sequential()
model.add(LSTM(units=50, return_sequences=True,
          input_shape=(X_train.shape[1], 1)))
model.add(Dropout(0.5))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.5))
model.add(LSTM(units=50))
model.add(Dropout(0.5))
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=100, batch_size=32)

model.save("BTC.model")
