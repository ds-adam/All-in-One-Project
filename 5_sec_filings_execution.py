import sec_support
import time


# EXECUTION
keyword = input('enter correct ticker to get financial data links: ').strip()
pages_msg = input('enter the pages you want parse (comma separated): ')
pages = list(int(page.strip()) for page in pages_msg.split(','))

ticker = sec_support.search_ticker_by_key(keyword)
data_list = sec_support.parse_web_page_docs(ticker, pages)

# construct unique filename
timesrt = time.strftime("%Y%m%d-%H%M%S")
fname = f"sec_{ticker}_{timesrt}.csv"
final_df = sec_support.save_df_to_csv(data_list, fname)


# checks
print(f"***************************\n\t{final_df.head(5)}")
print(f"\t{final_df.at[99, 'URLs']}\n*******************************")
print(f"find generated file here: \t{fname}")
open(fname,'r')
print("Completed!")

