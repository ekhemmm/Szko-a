import tkinter as tk
window = tk.Tk()

def add(symbol):
    textBox.config(state = tk.NORMAL)
    textBox.insert(tk.END, symbol)
    textBox.config(state = tk.DISABLED)

def DoIT(expression=""):
    expression = textBox.get("1.0", tk.END).strip()
    try:
        result = eval(expression)
        delete()
        add(result)
    except Exception as e:
        delete()
        add("Error")

def delete():
    textBox.config(state = tk.NORMAL)
    textBox.delete("1.0", tk.END)
    textBox.config(state = tk.DISABLED)

textBox = tk.Text(window, height = 1, width = 20)
textBox.grid(row = 0, column = 0, columnspan = 4)

seven = tk.Button(window, text = "7", height = 2, width = 5, command=lambda: add("7"))
seven.grid(row = 1, column = 0, sticky = "W")

eight = tk.Button(window, text = "8", height = 2, width = 5, command=lambda: add("8"))
eight.grid(row = 1, column = 1, sticky = "W")

nine = tk.Button(window, text = "9", height = 2, width = 5, command=lambda: add("9"))
nine.grid(row = 1, column = 2, sticky = "W")

plus = tk.Button(window, text = "+", height = 2, width = 5, command=lambda: add("+"))
plus.grid(row = 1, column = 3, sticky = "W")

four = tk.Button(window, text = "4", height = 2, width = 5, command=lambda: add("4"))
four.grid(row = 2, column = 0, sticky = "W")

five = tk.Button(window, text = "5", height = 2, width = 5, command=lambda: add("5"))
five.grid(row = 2, column = 1, sticky = "W")

six = tk.Button(window, text = "6", height = 2, width = 5, command=lambda: add("6"))
six.grid(row = 2, column = 2, sticky = "W")

minus = tk.Button(window, text = "-", height = 2, width = 5, command=lambda: add("-"))
minus.grid(row = 2, column = 3, sticky = "W")

one = tk.Button(window, text = "1", height = 2, width = 5, command=lambda: add("1"))
one.grid(row = 3, column = 0, sticky = "W")

two = tk.Button(window, text = "2", height = 2, width = 5, command=lambda: add("2"))
two.grid(row = 3, column = 1, sticky = "W")

three = tk.Button(window, text = "3", height = 2, width = 5, command=lambda: add("3"))
three.grid(row = 3, column = 2, sticky = "W")

times = tk.Button(window, text = "*", height = 2, width = 5, command=lambda: add("*"))
times.grid(row = 3, column = 3, sticky = "W")

zero = tk.Button(window, text = "0", height = 2, width = 5, command=lambda: add("0"))
zero.grid(row = 4, column = 0, sticky = "W")

clear = tk.Button(window, text = "Clear", height = 2, width = 5, command=delete)
clear.grid(row = 4, column = 1, sticky = "W")

equal = tk.Button(window, text = "=", height = 2, width = 5, command=DoIT)
equal.grid(row = 4, column = 2, sticky = "W")

divide = tk.Button(window, text = "/", height = 2, width = 5, command=lambda: add("/"))
divide.grid(row = 4, column = 3, sticky = "W")

window.mainloop()