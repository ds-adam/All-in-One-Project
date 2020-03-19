import requests
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg') 
import pandas as pd 
import time
from bs4 import BeautifulSoup 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import sys
sys.path.insert(0, r'C:\Users\19293\Desktop\DS File\All-in-One-Project\Keys')
from keys import client_id

# define the url
# ticker_raw = input(f'Please enter ticker symbol: ')
# period = int(input(f'Please enter # of years: '))

figure = Figure(figsize=(7,3), dpi=100)

def ticker_graph(ticker, period):
    ticker = ticker.strip().upper()
    period = period
    # period = period.strip()
    
    url_for_price = f"https://api.tdameritrade.com/v1/marketdata/{ticker}/pricehistory"

    # this part is the control. Change period (years) 
    attributes = {'apikey': client_id,
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
    graphs = figure.add_subplot(111).plot(df['date'], df['open'])

    # graphs.set_text(f'{company_title} - {period} years.')
    # graphs.set_xlabel('date')
    # graphs.set_ylabel('price')
    # # plt.show()

# ticker_graph('FB', 5)