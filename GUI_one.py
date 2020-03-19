from tkinter import *
import historical_prices as hp
# from historical_prices import figure as figure
import sys
import entries
from hyperlink_mng import *
import sec_filings_execution as sfe
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from hyperlink_mng import *


# Dimentions of the Overall Window
HEIGHT = 600
WIDTH = 1000

# Overall Window
window = Tk()
canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = Frame(window)
frame.place(x=10,y=160)

#Inputs 
ticker_one = StringVar()
year_prices_one = StringVar()
year_sec_one = StringVar()

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
        self.button = Button(frame, text="Get SEC Filings", fg="black", command= self.show)
        self.button.pack(side=RIGHT)

    def show(self):
        # a separate space to show 'DataFramed' SEC Filings 
        sec = Text(window) 
        hyperlink = HyperlinkManager(sec)
        sec.place(relx=0.2, rely=0.1)
        
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
        self.button = Button(frame, text="Get Hist Prices", fg="black", command=self.get)
        self.button.pack()
    
    def get(self):
        hp.ticker_graph(ticker_one.get(), year_prices_one.get())
        
        figure = Figure(figsize=(3,2), dpi=100)
        a = figure.add_subplot(111)
        a.plot([1,2,3,4,5],[1,2,3,4,5])

        canvas = hp.FigureCanvasTkAgg(figure, master=window)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.4, rely=0.06)

        # a = fig.add_subplot(111)
        # a.plot(x, y, color='blue')
        # a.invert_yaxis()

        # a.set_title ("Estimation Grid", fontsize=16)
        # a.set_ylabel("Y", fontsize=14)
        # a.set_xlabel("X", fontsize=14)




# class mclass:
#     def __init__(self,  window):
#         self.window = window
#         # self.box = Entry(window)
#         self.button = Button (window, text="check", command=self.plot)
#         # self.box.pack ()
#         self.button.pack()

#     def plot(self):
#         x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#         y= np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#         fig = Figure(figsize=(3,3))
#         a = fig.add_subplot(111)
#         a.plot(x, y, color='blue')
#         a.invert_yaxis()

#         a.set_title ("Estimation Grid", fontsize=16)
#         a.set_ylabel("Y", fontsize=14)
#         a.set_xlabel("X", fontsize=14)

#         canvas = FigureCanvasTkAgg(fig, master=self.window)
#         canvas.get_tk_widget().pack()
#         canvas.draw()
#         canvas.get_tk_widget().place(relx=0.4, rely=0.06)

# sec = Text(window) 
# hyperlink = HyperlinkManager(sec)
# sec.place(relx=0.4, rely=0.60)

# class PrintToT1(object):
#     def write(self, s):
#          sec.insert(END, s)
#     def flush(self):
#         pass 

# sys.stdout = PrintToT1()
# print('Hello, world!')


#EXECUTION
tickers(window)
years_prices(window)
years_sec(window)
sec_filings(window)
price_history(window)


window.mainloop()