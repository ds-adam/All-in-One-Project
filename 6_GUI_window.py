from tkinter import *
import historical_prices as hp

# Dimentions of the Overall Window
HEIGHT = 600
WIDTH = 600

# Functions to display a grey aid text in 'ticker box'
def handle_focus_in(_):
    ticker.delete(0, END)
    ticker.config(fg='black')

def handle_focus_out(_):
    # ticker.delete(0, END)
    ticker.config(fg='black')

def handle_enter(txt):
    # ticker.delete(0, END)
    ticker.config(fg='black')

# Overall Window
window = Tk()
canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

# Ticker Box
label_ticker = Label(window, text='Ticker:')
label_ticker.pack()

ticker = Entry(window, bg='white', width=30, fg='grey')
ticker.insert(0, "Example: AZMN")
ticker.bind("<FocusIn>", handle_focus_in)
ticker.bind("<FocusOut>", handle_focus_out)
ticker.bind("<Return>", handle_enter)
ticker.pack()

# Period Box
label_period = Label(window, text='Period:')
label_period.pack()

period = Entry(window, bg='white', width=30, fg='grey')
period.insert(0, "Example: 3")
period.bind("<FocusIn>", handle_focus_in)
period.bind("<FocusOut>", handle_focus_out)
period.bind("<Return>", handle_enter)
period.pack()

button = Button(window, text='Get graph', command=lambda: hp.ticker_graph(ticker.get(), period.get()))
button.pack()

window.mainloop()


