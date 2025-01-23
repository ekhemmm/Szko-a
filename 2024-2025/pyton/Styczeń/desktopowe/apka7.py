import tkinter as tk
window = tk.Tk()

def radioClicked():
    print("Radio value: ", radioValue.get())

radioValue = tk.IntVar()
r1 = tk.Radiobutton(window, text="Option 1", variable=radioValue, value=1, command=radioClicked)
r2 = tk.Radiobutton(window, text="Option 2", variable=radioValue, value=2, command=radioClicked)
r3 = tk.Radiobutton(window, text="Option 3", variable=radioValue, value=3, command=radioClicked)

r1.pack()
r2.pack()
r3.pack()

window.mainloop()