import os
from alpha_vantage.timeseries import TimeSeries

# get the api key from environment variable
apikey = os.getenv('ALPHAVANTAGE_API_KEY')

#initialize the TimeSeries class
ts = TimeSeries(key=apikey)

# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')

#print metadata and data
print (meta_data)
print (data)



