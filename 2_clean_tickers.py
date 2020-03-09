import pandas as pd
import numpy as np
import time

# Read the file
df = pd.read_csv('raw_finviz_data.csv')

# Clean market cap column and turn them into integers
df['Market Cap'] = df['Market Cap'].str.replace('.','')
df['Market Cap'] = df['Market Cap'].str.replace('M','000000')
df['Market Cap'] = df['Market Cap'].str.replace('B','000000000')
df['Market Cap'] = df['Market Cap'].str.replace('-','')

# Replace empty cells with NaN
df['Market Cap'].replace('', np.nan, inplace=True)
df.dropna(subset=['Market Cap'], inplace=True)


# Drop duplicate entries
df.drop_duplicates(subset=['Company'], keep='first', inplace=True)

# Save the file into csv file with a timestamp
timestr = time.strftime("%Y%m%d-%H%M%S")

df.to_csv(f'cleaned_finviz_data_{timestr}.csv')