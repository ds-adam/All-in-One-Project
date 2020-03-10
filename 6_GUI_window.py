from tkinter import *
import historical_prices as hp
from historical_prices import figure as figure
import sys
import sec_filings_execution as sfe
import entries

# Dimentions of the Overall Window
HEIGHT = 600
WIDTH = 600

# Functions to display a grey aid text in 'ticker box'
def shadow_ticker_text(txt):
    def handle_focus_in(txt):
        ticker.delete(0, END)
        ticker.config(fg='black')
    handle_focus_in(txt)

    def handle_focus_out(txt):
        ticker.delete(0, END)
        ticker.config(fg='black')
    handle_focus_out(txt)

    def handle_enter(txt):
        ticker.delete(0, END)
        ticker.config(fg='black')
    handle_enter(txt)

def shadow_period_text(txt):
    def handle_focus_in(txt):
        period.delete(0, END)
        period.config(fg='black')
    handle_focus_in(txt)

    def handle_focus_out(txt):
        period.delete(0, END)
        period.config(fg='black')
    handle_focus_out(txt)

    def handle_enter(txt):
        period.delete(0, END)
        period.config(fg='black')
    handle_enter(txt)

def shadow_pages_text(txt):
    def handle_focus_in(txt):
        pages_cs.delete(0, END)
        pages_cs.config(fg='black')
    handle_focus_in(txt)

    def handle_focus_out(txt):
        pages_cs.delete(0, END)
        pages_cs.config(fg='black')
    handle_focus_out(txt)

    def handle_enter(txt):
        pages_cs.delete(0, END)
        pages_cs.config(fg='black')
    handle_enter(txt)

# Overall Window
window = Tk()
canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()


# Ticker Box
label_ticker = Label(window, text='Ticker:')
label_ticker.place(x=10, y=20)

ticker = Entry(window, bg='white', width=30, fg='grey')
ticker.insert(0, "Example: AZMN")
ticker.bind("<FocusIn>", shadow_ticker_text)
ticker.place(x=10, y=40)


# Period Box
label_period = Label(window, text='Period:')
label_period.place(x=10, y=60)

period = Entry(window, bg='white', width=30, fg='grey')
period.insert(0, "Example: 3")
period.bind("<FocusIn>", shadow_period_text)
period.place(x=10, y=80)



# Button for Graph
button = Button(window, text='Get Hist. Prices', command=lambda: hp.ticker_graph(ticker.get(), period.get()))
button.place(x=110, y=140)

# Pages Box
label_pages = Label(window, text='Pages:')
label_pages.place(x=10, y=100)

pages_cs = Entry(window, bg='white', width=30, fg='grey')
# pages = pages_cs.get()
pages_cs.insert(0, "Example: 1, 2, 3")
pages_cs.bind("<FocusIn>", shadow_pages_text)
pages_cs.place(x=10, y=120)

# Button for SEC Filings
button = Button(window, text='Get SEC Filings', command=lambda: sfe.execution(entries.ticker_entry.ticker.get(), entries.ticker_entry.period.get()))
button.place(x=10, y=140)

canvas = hp.FigureCanvasTkAgg(figure, master=window)
canvas.draw()
canvas.get_tk_widget().place(relx=0.4, rely=0.06)

sec = Text(window) 
sec.place(relx=0.4, rely=0.60)

class PrintToT1(object): 
    def write(self, s): 
        sec.insert(END, s)

    def flush(self):
        pass 

sys.stdout = PrintToT1() 
# print ('Hello, world!') 
result = sfe.execution('fb', '1,2,3')
print(result)

window.mainloop()


