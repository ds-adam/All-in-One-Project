import requests
import matplotlib.pyplot as plt
import pandas as pd 
import time


# define the url
ticker = 'GOOG'
url = f"https://api.tdameritrade.com/v1/marketdata/{ticker}/pricehistory"

# this part is the control. Change period (years) 
attributes = {'apikey':'0VUBGJN2ZEGBQWNSWB3AJAGRGULVTHAJ',
            'periodType':'year',
            'period': '5',
            'frequencyType':'daily',
            'frequency':'1',
            'needExtendedHoursData':'false'}

content = requests.get(url = url, params = attributes)

data = content.json()

df = pd.DataFrame(data['candles'])
df['date'] = pd.to_datetime(df['datetime'], unit='ms')

# save the data  in csv format
df.to_csv(f'{ticker}_data.csv')

# plot the data to quickly check
plt.plot(df['date'], df['open'])
plt.xlabel('date')
plt.ylabel('price')
plt.show()
