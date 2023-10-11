
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import load_model

df = pd.read_csv("BTC.csv")

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_df = scaler.fit_transform(df["close"].values.reshape(-1, 1))

model = load_model("BTC.model")

tdf = pd.read_csv("bitcoin.csv")
price = tdf["close"].values

totalDf = pd.concat((df["close"], tdf["close"]), axis=0)
model_inputs = totalDf[len(totalDf) - len(tdf) - 60:].values
model_inputs = model_inputs.reshape(-1, 1)
model_inputs = scaler.fit_transform(model_inputs)

x_test = []

for x in range(60, len(model_inputs)):
    x_test.append(model_inputs[x-60:x, 0])

x_test = np.array(x_test)
print(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

predicted_prices = model.predict(x_test)
predicted_prices = scaler.inverse_transform(predicted_prices)

plt.plot(price, color="black", label="actual prices")
plt.plot(predicted_prices, color="blue", label="predicted prices")
plt.legend(loc="upper left")
plt.show()


real_data = [model_inputs[len(model_inputs)+1 - 60:len(model_inputs)+1, 0]]
real_data = np.array(real_data)
real_data = np.reshape(
    real_data, (real_data.shape[0], real_data.shape[1], 1))

prediction = model.predict(real_data)
prediction = scaler.inverse_transform(prediction)

print(prediction)
