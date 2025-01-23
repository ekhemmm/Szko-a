import tkinter as tk
window = tk.Tk()

label1 = tk.Label(window, text = "Wybierz swoje ulubione gatunki filmów.", justify = "left" )
label2 = tk.Label(window, text = "Zaznacz wszystkie, które chciałbyś wybrać:", justify = "left")
label1.pack(pady=0, padx=0, anchor="w")
label2.pack(pady=0, padx=0, anchor="w")

def radioClicked():
    if radioValue.get() == 1:
        textBox.delete(1.0,tk.END)
        textBox.insert(tk.END, "Twoim ulubionym gatunkiem filmu jest komedia.")
    
    elif radioValue.get() == 2:
        textBox.delete(1.0,tk.END)
        textBox.insert(tk.END, "Twoim ulubionym gatunkiem filmu jest romans.")
    
    elif radioValue.get() == 3:
        textBox.delete(1.0,tk.END)
        textBox.insert(tk.END, "Twoim ulubionym gatunkiem filmu jest dramat.")

radioValue = tk.IntVar()

c1 = tk.Radiobutton(window, text="komedia", variable=radioValue, command=radioClicked, value=1, justify = "left")
c1.pack(pady=0, padx=0, anchor="w")
c2 = tk.Radiobutton(window, text="romans", variable=radioValue, command=radioClicked, value=2, justify = "left")
c2.pack(pady=0, padx=0, anchor="w")
c3 = tk.Radiobutton(window, text="dramat", variable=radioValue, command=radioClicked, value=3, justify = "left")
c3.pack(pady=0, padx=0, anchor="w")

textBox = tk.Text(window, height=5, width=30, padx=5, pady=5, font="Times 18 bold")
textBox.pack()

window.mainloop()