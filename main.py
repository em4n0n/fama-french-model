import yfinance as yf
import pandas_datareader.data as web
import statsmodels.api as sm
import pandas as pd
import datetime

# Define the date range
start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2024, 10, 1)

# Fetch Tesla stock data using yfinance
stock_data = yf.download('TSLA', start=start, end=end)

# Fetch Fama-French factors data
ff_data = web.DataReader('F-F_Research_Data_Factors_daily', 'famafrench', start, end)[0]

# Convert Tesla stock 'Adj Close' to returns
stock_data['Returns'] = stock_data['Adj Close'].pct_change()

# Align the Tesla returns and Fama-French factors by date
combined_data = pd.merge(stock_data['Returns'], ff_data, left_index=True, right_index=True)

# Drop rows with missing data
combined_data = combined_data.dropna()

# Prepare dependent and independent variables
y = combined_data['Returns']  # Tesla returns as the dependent variable
X = combined_data[['Mkt-RF', 'SMB', 'HML']]  # Fama-French factors as independent variables

# Add a constant to the model (for the intercept term)
X = sm.add_constant(X)

# Build the Ordinary Least Squares (OLS) model
model = sm.OLS(y, X).fit()

# Print the model summary
print(model.summary())