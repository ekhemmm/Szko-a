import tkinter as tk
window = tk.Tk()

def sprawdz():
    if entry.get() == "sekret":
        textBox.insert(tk.END, "Cos tan cos tam odkryles sekret dozyj 99 lat i zyj dalej wariacie grypsujesz???:DDD" )

label = tk.Label(window, text = "Wprowadź hasło do sekretu długowieczności")
label.grid(row=0, column=0, columnspan=2)

tk.Label(window, text="Hasło:\t").grid(row=1, column=0)
entry = tk.Entry(window)
entry.grid(row=1, column=1)
entry.insert(0, "")

button = tk.Button(window, text = "Sprawdz", command=sprawdz)
button.grid(row=2, column=0)

textBox = tk.Text(window, height=5, width=30, padx=5, pady=5, font="Times 18 bold")
textBox.grid(row=3, column=0, columnspan=2)

window.mainloop()