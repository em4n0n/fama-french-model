import pandas as pd
import pandas_datareader.data as web
import statsmodels.api as sm
from datetime import datetime

# Download stock data from YFinance
start = datetime(2020,1,1)
end = datetime(2024,1,1)
tesla_data = web.DataReader('TSLA', 'yahoo', start, end)

# Download Fama-French 3 factors from Kennth French's data library
ff_data = web.DataReader('F-F_Research_Data_Factors_daily', 'famafrench', start, end)[0]

# Calculate stock daily returns
tesla_data['Return'] = tesla_data['Adj Close'].pct_change()

# Merge Tesla returns with Fama-French data
data = pd.merge(tesla_data['Return'], ff_data, left_index=True, right_index=True)

# Calculate excess return (Tesla return minus risk-free rate)
data['Excess Return'] = data['Return'] - data['RF']

# Perform the regression
X = data[['Mkt-RF', 'SMB', 'HML']] # Fama-French factors
y = data['Excess Return'] # Stock's excess return

X = sm.add_constant(x) # Add a constant (alpha) to the model


