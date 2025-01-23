import tkinter as tk
window = tk.Tk()

def menuItemSelected():
    print("Menu item selected")
def menuItemCloseSelected():
    quit()

rootmenu = tk.Menu()
filemenu = tk.Menu()

filemenu.add_command(label="New", command=menuItemSelected)
filemenu.add_command(label="Open", command=menuItemSelected)
filemenu.add_command(label="Save", command=menuItemSelected)
filemenu.add_command(label="Save as", command=menuItemSelected)
filemenu.add_separator()
filemenu.add_command(label="Close", command=menuItemCloseSelected)

editmenu = tk.Menu()
editmenu.add_command(label="Cut", command=menuItemSelected)
editmenu.add_command(label="Copy", command=menuItemSelected)
editmenu.add_command(label="Paste", command=menuItemSelected)
editmenu.add_command(label="Config", command=menuItemSelected)
rootmenu.add_cascade(label="File", menu=filemenu)
rootmenu.add_cascade(label="Edit", menu=editmenu)

window.config(menu=rootmenu)



window.mainloop()