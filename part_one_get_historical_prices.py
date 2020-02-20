import requests
import matplotlib.pyplot as plt
import pandas as pd 
import time
from bs4 import BeautifulSoup 

# define the url
ticker_raw = input(f'Please enter ticker symbol: ')
period = int(input(f'Please enter # of years: '))

ticker = ticker_raw.strip().upper()
# period = period_raw.strip()

url_for_price = f"https://api.tdameritrade.com/v1/marketdata/{ticker}/pricehistory"

# this part is the control. Change period (years) 
attributes = {'apikey':'0VUBGJN2ZEGBQWNSWB3AJAGRGULVTHAJ',
            'periodType':'year',
            'period': f'{period}',
            'frequencyType':'daily',
            'frequency':'1',
            'needExtendedHoursData':'false'}

content = requests.get(url = url_for_price, params = attributes)

# get the full company name
url_for_name = f"https://finviz.com/quote.ashx?t={ticker}&ty=c&p=d&b=1"
response = requests.get(url_for_name).text
soup = BeautifulSoup(response, 'lxml')
#Clean the company name
company_title = soup.title.text.split('.')[0]
company_title = company_title.split(' ')[1:]
company_title = ' '.join(company_title)


data = content.json()

df = pd.DataFrame(data['candles'])
df['date'] = pd.to_datetime(df['datetime'], unit='ms')

# save the data  in csv format
# timestr = time.strftime("%Y%m%d-%H%M%S")
# df.to_csv(f'{ticker}_data_{timestr}.csv')

# plot the data to quickly check
plt.plot(df['date'], df['open'])
plt.title(f'{company_title} - {period} years.')
plt.xlabel('date')
plt.ylabel('price')
plt.show()
