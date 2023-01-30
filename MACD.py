import pandas as pd
import numpy as np
import talib

# Load data into a pandas DataFrame
data = pd.read_csv("stock_data.csv")

# Calculate the Moving Average Convergence Divergence (MACD)
macd, signal, hist = talib.MACD(data['Close'].values, fastperiod=12, slowperiod=26, signalperiod=9)

# Create a column in the DataFrame to store the signal
data['Signal'] = signal

# Set up a strategy to buy when the MACD crosses above the signal line
# and sell when it crosses below

# Initialize the positions
positions = np.zeros(len(data))

for i in range(1, len(data)):
    if macd[i] > signal[i] and macd[i-1] <= signal[i-1]:
        positions[i] = 1
    elif macd[i] < signal[i] and macd[i-1] >= signal[i-1]:
        positions[i] = -1

# Calculate the returns based on the positions
returns = np.diff(data['Close'].values) * positions[:-1]

# Print the final returns
print("Final returns:", returns[-1])
