from tkinter import *
import historical_prices as hp
from historical_prices import figure as figure
import sys
import entries
from hyperlink_mng import *
import sec_filings_execution as sfe
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Dimentions of the Overall Window
HEIGHT = 600
WIDTH = 1000

# Overall Window
window = Tk()
canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = Frame(window)
frame.place(x=250, y=500)


tickers = Entry(frame, bd=2)
ticker = tickers.get()
tickers.pack()
ticker_label = Label(frame, text="Ticker")
ticker_label.pack()


years_prices = Entry(frame, bd=2) 
year_prices = years_prices.get()
years_prices.pack()
years_label = Label(frame, text="Years for Hist Price")
years_label.pack()


years_sec = Entry(frame, bd=2)
year_sec = years_sec.get()
years_sec.pack()
years_label = Label(frame, text="Years for Filings")
years_label.pack()



class sec_filings:
    def __init__(self, window):
        self.window = window
        self.button = Button(frame, text="Get SEC Filings", fg="black", command= self.show)
        self.button.pack()

    def show(self):
        sfe.execution(ticker, year_sec)
        fig = Figure(figsize=(3,3))
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.4, rely=0.06)

class price_history:
    def __init__(self, window):
        self.window = window
        self.button = Button(frame, text="Get Hist Prices", fg="black", command=self.get)
        self.button.pack()
    
    def get(self):
        x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        y= np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        fig = Figure(figsize=(3,3))
        a = fig.add_subplot(111)
        a.plot(x, y, color='blue')
        a.invert_yaxis()

        a.set_title ("Estimation Grid", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.4, rely=0.06)


class mclass:
    def __init__(self,  window):
        self.window = window
        # self.box = Entry(window)
        self.button = Button (window, text="check", command=self.plot)
        # self.box.pack ()
        self.button.pack()

    def plot(self):
        x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        y= np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        fig = Figure(figsize=(3,3))
        a = fig.add_subplot(111)
        a.plot(x, y, color='blue')
        a.invert_yaxis()

        a.set_title ("Estimation Grid", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack()
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.4, rely=0.06)

#EXECUTION
start_one = sec_filings(window)
start_two = price_history(window)
start= mclass(window)

window.mainloop()