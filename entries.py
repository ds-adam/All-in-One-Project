from tkinter import *


def ticker_entry(master, bind_function):
    # Ticker Box
    window = master
    label_ticker = Label(window, text='Ticker:')
    label_ticker.place(x=10, y=20)

    ticker = Entry(window, bg='white', width=30, fg='grey')
    ticker.insert(0, "Example: AZMN")
    shadow_ticker_text = bind_function 
    ticker.bind("<FocusIn>", shadow_ticker_text)
    ticker.place(x=10, y=40)
    return ticker




def period_entry(master, bind_function):
    # Period Box
    window = master
    label_period = Label(window, text='Period:')
    label_period.place(x=10, y=60)

    period = Entry(window, bg='white', width=30, fg='grey')
    period.insert(0, "Example: 3")
    shadow_period_text = bind_function
    period.bind("<FocusIn>", shadow_period_text)
    period.place(x=10, y=80)
    return period