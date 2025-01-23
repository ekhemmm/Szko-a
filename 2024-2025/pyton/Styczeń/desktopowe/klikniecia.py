import tkinter as tk
window = tk.Tk()
n = 0

def buttonValuePlus():
    global n
    n += 1
    label.config(text = "Liczba kliknięć: " + str(n))

def buttonValueMinus():
    global n
    n -= 1
    label.config(text = "Liczba kliknięć: " + str(n))

label = tk.Label(window, text="Liczba kliknięć: 0")
label.pack()

butplus = tk.Button(window, text = "Dodaj", command=buttonValuePlus)
butplus.pack()

butminus = tk.Button(window, text = "Odejmij", command=buttonValueMinus)
butminus.pack()

window.mainloop()