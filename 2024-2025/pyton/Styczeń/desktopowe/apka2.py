import tkinter as tk

window = tk.Tk()
window.geometry("300x300")
window.resizable(False,False)

Label1 = tk.Label(window, text="Label 1", bg="silver")
Label1.place(x=20, y=20, width=50, height=35)

Label2 = tk.Label(window, text="Label 2", bg="red")
Label2.place(x=70, y=20, width=90, height=35)

window.mainloop()