import tkinter as tk
window = tk.Tk()

scrollbar = tk.Scrollbar(window)
listbox = tk.Listbox(window, selectmode=tk.MULTIPLE)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.pack(fill=tk.Y)
scrollbar.config(command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)

for i in range(15):
    listbox.insert(tk.END, str(i))

label = tk.Label(window)
label.pack()

def checklist():
    selection = listbox.curselection()
    label.config(text = str(selection))
    label.after(300, checklist)

checklist()

window.mainloop()