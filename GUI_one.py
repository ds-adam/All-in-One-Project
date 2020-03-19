from tkinter import *
import historical_prices as hp
# from historical_prices import figure as figure
import sys
import entries
from hyperlink_mng import *
import sec_filings_execution as sfe
from historical_prices import figure as figure
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from hyperlink_mng import *
import fund_data_each as fde

# Dimentions of the Overall Window
HEIGHT = 600
WIDTH = 1000

# Overall Window
window = Tk()
canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

# frame = Frame(window)
# frame.place(x=10,y=160)

#Inputs 
ticker_one = StringVar()
year_prices_one = StringVar()
year_sec_one = StringVar()

name_text = fde.get_name(ticker_one.get())
name_label = Label(window, text=name_text)
name_label.place(x=5, y=300)

#Input classes
class tickers:
    def __init__(self, window):
        self.tickers = Entry(window, bd=2, textvariable=ticker_one)
        self.tickers.place(x=10,y=30)
        self.ticker_label = Label(window, text="Ticker")
        self.ticker_label.place(x=10,y=5)

class years_prices:
    def __init__(self, window):
        self.years_prices = Entry(window, bd=2, textvariable=year_prices_one) 
        self.years_prices.place(x=10,y=80)
        self.years_label = Label(window, text="Years for Hist Price")
        self.years_label.place(x=10,y=55)

class years_sec:
    def __init__(self, window):
        self.years_sec = Entry(window, bd=2, textvariable=year_sec_one)
        self.years_sec.place(x=10,y=130)
        self.years_label = Label(window, text="Years for Filings")
        self.years_label.place(x=10,y=105)


#Button classes
class sec_filings:
    def __init__(self, window):
        self.window = window
        self.button = Button(window, text="Get SEC Filings", fg="black", command= self.show)
        self.button.place(x=10,y=160)

    def show(self):
        # a separate space to show 'DataFramed' SEC Filings 
        sec = Text(window) 
        hyperlink = HyperlinkManager(sec)
        sec.place(relx=0.5, rely=0.5)
        
        class PrintToT1(object):
            def write(self, s):
                sec.insert(END, s)
            def flush(self):
                pass 

        sys.stdout = PrintToT1()
        result = sfe.execution(ticker_one.get(), year_sec_one.get())
        print(result)

class price_history:
    def __init__(self, window):
        self.window = window
        self.button = Button(window, text="Get Hist Prices", fg="black", command=self.get)
        self.button.place(x=10,y=200)
    
    def get(self):
        
        graph = hp.ticker_graph(ticker_one.get(), year_prices_one.get())
        canvas = hp.FigureCanvasTkAgg(figure, master=window)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.5, rely=0.03)

class fund_data:
    def __init__(self, window):
        self.window = window
        self.button = Button(window, text="Get Fundamental Data", fg="black", command= self.get)
        self.button.place(x=10,y=240)

    def get(self):
        sec = Text(window, width=30, height=25) 
        hyperlink = HyperlinkManager(sec)
        sec.place(relx=0.2, rely=0.1)
        
        class PrintToT1(object):
            def write(self, s):
                sec.insert(END, s)
            def flush(self):
                pass 

        sys.stdout = PrintToT1()
        result = fde.get_fund_data(ticker_one.get())
        print(result)


#EXECUTION
tickers(window)
years_prices(window)
years_sec(window)
sec_filings(window)
price_history(window)
fund_data(window)

window.mainloop()