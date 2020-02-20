import time
import pandas as pd 
from bs4 import BeautifulSoup
import requests

# get intitial company list and raw data from finviz
raw_url = "https://finviz.com/screener.ashx?v=111&r=01"

url_list = []
dfs = []

# loop through every page and scrape all essenstial information
for i in range(387):
    i = 1 + i*20
    basic_url = f"https://finviz.com/screener.ashx?v=111&r={i}"
    url_list.append(basic_url)

for url in url_list:
    tables = pd.read_html(url, header=0, index_col=0)
    df = pd.DataFrame(tables[14])
    dfs.append(df)

# join all the data into one large pandas DataFrame
all_data = pd.concat(dfs)

# Save the file into csv file with a timestamp
timestr = time.strftime("%Y%m%d-%H%M%S")
all_data.to_csv(f'raw_finviz_data_{timestr}.csv')