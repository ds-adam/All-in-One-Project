import time
import string
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from bs4 import BeautifulSoup
import requests

def get_name(ticker):
	url = f"https://finviz.com/quote.ashx?t={ticker}&ty=c&p=d&b=1"

	response = requests.get(url).text
	soup = BeautifulSoup(response, 'lxml')

	#Clean the company name
	company_title = soup.title.text.split('.')[0]
	company_title = company_title.split(' ')[1:]
	company_title = ' '.join(company_title)
	print(f'\n{company_title}')


def get_fund_data(ticker):
	url = f"https://finviz.com/quote.ashx?t={ticker}&ty=c&p=d&b=1"

	response = requests.get(url).text
	soup = BeautifulSoup(response, 'lxml')

	keys_list = []
	values_list = []

	for key in soup.find_all('td', class_='snapshot-td2-cp'):
		key = key.text
		keys_list.append(key)

	for value in soup.find_all('td', class_='snapshot-td2'):
		value = value.text
		values_list.append(value)

	dic_one = dict(zip(keys_list, values_list))

	#Clean the company name
	company_title = soup.title.text.split('.')[0]
	company_title = company_title.split(' ')[1:]
	company_title = ' '.join(company_title)

	# This is a nested dictionary that contains company name as 
	# its first key and dic_one as its value. This might be a 
	# better way to store the data (company name and its data 
	# sould be connected.)

	# DataFrame of raw data scraped from finviz, company webpage
	df_raw = pd.DataFrame(dic_one.items(), index=None, columns=['Attribute', 'Value'])

	# List of items we need
	check_list = ['Index', 'Market Cap', 'P/E', 'Insider Own', 'Income', 'Inst Own', 'Sales', 'P/S', 'P/B', 'ROA', 'ROE', '52W Range','P/FCF', 'EPS past 5Y', 'ROI', 'Sales past 5Y', 'Gross Margin', 'Oper. Margin', 'Debt/Eq', 'Profit Margin', 'Payout','Price']

	# Cleaned DataFrame 
	df_clean = df_raw[df_raw['Attribute'].isin(check_list)].reset_index(drop='true')

	# df_clean = df_raw[df_raw['Attribute'].isin(check_list)].set_index('Attribute', inplace=True)


	# make relevant-attributes tables 
	table_one = df_clean.iloc[[0, 3, 6, 4]]
	table_two = df_clean.iloc[[1, 7, 12, 8]]
	table_three = df_clean.iloc[[13, 15, 2, 5]]
	table_four = df_clean.iloc[[9, 10, 14]]
	table_five = df_clean.iloc[[16, 17, 19, 20]]
	table_six = df_clean.iloc[[18, 21, 11]]

	# display those tables without any column names and index
	print(table_one.to_string(index = False, header=False))
	print(table_two.to_string(index = False, header=False))
	print(table_three.to_string(index = False, header=False))
	print(table_four.to_string(index = False, header=False))
	print(table_five.to_string(index = False, header=False))
	print(table_six.to_string(index = False, header=False))

	# df_clean.name = f'{company_title}'
	# timestr = time.strftime("%Y%m%d-%H%M%S")
	# df_clean.to_csv(f'{df.name}_snapshot_finviz_{timestr}.csv')

