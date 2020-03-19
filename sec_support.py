# import libraries
import requests
import urllib
import pandas as pd
from bs4 import BeautifulSoup
import csv
import numpy as np
import time


# cik_number = '0000886206'
# 10k_url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik_number}&type=10-k&dateb=&owner=exclude&count=100"
# 10q_url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik_number}&type=10-q&dateb=&owner=exclude&count=100"



def parse_web_page_docs(ticker, pages):
    # pages = [0, 1, 2, 3, 4, 5] 
    # needs some polishing since it might cause an error when the company under consideration 
    # does not have an sec webpage corresponding to one of the above numbers (most likely last ones). 
    
    #lists that store individual items scrapped from the base_url 
    filings = []
    urls = []
    filing_dates = []

    # final list that stores individual lists and later will be turned into pd.DataFrame
    final_data_list = []
    
    # loop through each page and scrape the necessary information. 
    for page in pages:
        
        base_url = f"https://www.sec.gov/cgi-bin/browse-edgar?CIK={ticker}&Find=Search&owner=exclude&start={page}00&count=100"
        response = requests.get(base_url)
        soup = BeautifulSoup(response.content, 'lxml')

        content_table = soup.find('table', class_='tableFile2')
        
        
        # a normal page in the SEC webpage is organized using various tags and their attributes.
        # The ones we need are 'tr' - row and 'td' - standard cell. 
        # print(content_table)
        for row in content_table.find_all('tr'):

            if (len(row.find_all('td')) != 0):

                # Filings section of the table
                for filing_items in row.find('td', {'nowrap':True, 'id': False, 'class': False, 'a': False}):
                    filing_item = [ele.strip() for ele in row.find('td', {'nowrap': True, 'id': False, 'class': False, 'a': False})]
                    filings.append(filing_item[0])

                # Format section of the table
                for format_items in row.find_all('a', {'id': 'documentsbutton'}):
                    format_item = format_items.get('href')  #This part took forever
                    sec_url = "https://www.sec.gov/"
                    doc_url = format_item[1:]
                    document_url = sec_url+ doc_url
                    urls.append(document_url)

                # Filing Date section of the table
                for filing_date_items in row.find('td', {'nowrap':False, 'class': False}):
                    filing_date_item = [ele.strip() for ele in row.find('td', {'nowrap':False, 'class': False})]
                    filing_dates.append(filing_date_item[0])
                    
        # join three lists that we created at the beginning into one - 'final_data_list' - as a dictionary.
        for filing, format_1, filing_date in zip(filings, urls, filing_dates):
            final_data_list.append({'Filings': filing, 'URLs': format_1, 'Filing Date': filing_date})
    return final_data_list
    # print(final_data_list)

def save_df_to_csv(list, filename):
    # create a pandas DataFrame from the scraped data. 
    df = pd.DataFrame(list)
    print('data frame saved..')

    # create a dynamic file-name and store the information.
    df.to_csv(filename)
    print('file is generated')
    return df

def search_ticker_by_key(keyword):
    # logic
    ticker=keyword
    return ticker

parse_web_page_docs('fb','1,2,3')