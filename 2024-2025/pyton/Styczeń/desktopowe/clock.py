import tkinter as tk
from time import strftime
window = tk.Tk()

window.title("Digital clock")

def time():
    string = strftime('%H:%M:%S')
    digital_clock.config(text=string)
    digital_clock.after(1000, time)

digital_clock = tk.Label(window, font=("arial", 150), foreground="white",background = "black")

digital_clock.pack(anchor='center')
time()

window.mainloop()