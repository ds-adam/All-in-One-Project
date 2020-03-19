from tkinter import *
import historical_prices as hp
from historical_prices import figure as figure
import sys
import entries
from hyperlink_mng import *

import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Dimentions of the Overall Window
HEIGHT = 600
WIDTH = 600

# Overall Window
window = Tk()
canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = Frame(window)
frame.place(x=250, y=500)


# price_button = Button(frame, text="Get Hist Prices", fg="black")
# price_button.pack(side=RIGHT)

# price_entry = Entry(frame, bd =5)
# price_entry.pack(side = RIGHT)
# price_entry.insert(0, "Enter # of years")


# sec_button = Button(frame, text="Get SEC Filings", fg="black")
# sec_button.pack(side=RIGHT)

# sec_entry = Entry(frame, bd =5)
# sec_entry.pack(side = RIGHT)
# sec_entry.insert(0, "Enter ticker symbol")

class sec_filings:
    def __init__(self, window):
        self.window = window
        self.button = Button(frame, text="Get SEC Filings", fg="black")
        self.button.pack(side=RIGHT)
        self.entry = Entry(frame, bd =5)
        self.entry.pack(side = RIGHT)
        self.entry.insert(0, "Enter # of years")



class price_history:
    def __init__(self, window):
        self.window = window
        self.button = Button(frame, text="Get Hist Prices", fg="black", command=self.get)
        self.button.pack(side=RIGHT)
        self.entry = Entry(frame, bd =5)
        self.entry.pack(side = RIGHT)
        self.entry.insert(0, "Enter # of years")
    
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
        canvas.get_tk_widget().pack()
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