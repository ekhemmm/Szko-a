import tkinter as tk
window = tk.Tk()

label1 = tk.Label(window, text = "Wybierz swoje ulunione gatunki filmów.", justify = "left" )
label2 = tk.Label(window, text = "Zaznacz wszystkie, które chciałbyś wybrać:", justify = "left")
label1.pack(pady=0, padx=0, anchor="w")
label2.pack(pady=0, padx=0, anchor="w")

def Change():
    textBox.delete(1.0,tk.END)
    if cb1.get() == 1:
        textBox.insert(tk.END, "Lubisz filmy komediowe.\n")
    if cb2.get() == 1:
        textBox.insert(tk.END, "Lubisz filmy romantyczne.\n")
    if cb3.get() == 1:
        textBox.insert(tk.END, "Lubisz filmy dramatyczne.\n")
cb1 = tk.IntVar(value=0)
cb2 = tk.IntVar(value=0)
cb3 = tk.IntVar(value=0)

c1 = tk.Checkbutton(window, text="komedia", variable=cb1, command=Change, justify = "left")
c1.pack(pady=0, padx=0, anchor="w")
c2 = tk.Checkbutton(window, text="romans", variable=cb2, command=Change, justify = "left")
c2.pack(pady=0, padx=0, anchor="w")
c3 = tk.Checkbutton(window, text="dramat", variable=cb3, command=Change, justify = "left")
c3.pack(pady=0, padx=0, anchor="w")

textBox = tk.Text(window, height=5, width=30, padx=5, pady=5, font="Times 18 bold")
textBox.pack()

window.mainloop()