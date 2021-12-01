from tkinter import *
from time import *

window = Tk()
window.title("Clock")

def update_clock():
    hours = strftime("%I")
    munites = strftime("%M")
    secound = strftime("%S")
    am_or_pm = strftime("%p")
    time_text = hours + ":" + munites + ":" + secound + "  " + am_or_pm
    lab.config(text = time_text)
    lab.after(1000, update_clock)



lab = Label(window, text="00:00:00",
            font="Digital-7 100",
            background="#123456",
            foreground="#00ff00")
lab.pack()

update_clock()

window.mainloop()
