import datetime
import pandas as pd
#for compatibility between datareader and pandas
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()
df = web.DataReader("TSLA", 'morningstar', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace = True)
df = df.drop("Symbol", axis = 1)
print(df.head())
