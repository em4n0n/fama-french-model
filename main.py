import pandas as pd
import pandas_datareader.data as web
import statsmodels.api as sm
from datetime import datetime

# Download stock data from YFinance
start = datetime(2020,1,1)
end = datetime(2024,1,1)
tesla_data = web.DataReader('TSLA', 'yahoo', start, end)
