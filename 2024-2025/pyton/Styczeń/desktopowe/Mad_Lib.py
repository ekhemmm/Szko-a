import tkinter as tk
window = tk.Tk()

def showStory():
    imie = entry1.get()
    rzecz = entry2.get()
    czas = entry3.get()
    
    przymiotniki = ""
    if cb1.get():
        przymiotniki += "naglące, "
    if cb2.get():
        przymiotniki += "radosne, "
    if cb3.get():
        przymiotniki += "elektryzujące, "

    cialo = ""
    if radioValue.get() == 1:
        cialo = "pępek"
    elif radioValue.get() == 2:
        cialo = "duży palec u \nnogi"
    elif radioValue.get() == 3:
        cialo = "rdzeń \nprzedłużony"

    textBox.delete(1.0,tk.END)
    textBox.insert(tk.END,f"Sławny badacz i odkrywca {imie} o mało co nie zrezygnował z życiowej misji \nposzukiwania zaginionego miasta, które zamieszkiwały {rzecz}, "  
                   f"gdy pewnego \ndnia Komputery znalazły {imie}. Silne, {przymiotniki}osobliwe uczucie \nowładnęło badaczem. " 
                   f"Po tak długim czasie poszukiwanie wreszcie się \nzakończyło. "
                   f"W oku {imie} pojawiła się łza, która spadla na jego {cialo}. A wtedy {rzecz} szybko pożarły {imie}. Jaki morał płynie z tego \nopowiadania? "  
                   f"Pomyśl, zanim zaczniesz coś {czas}.")

l = tk.Label(window, text="Wprowadź informacje do twojego opowiadania").grid(row=0, column=0, sticky="w")
l1 = tk.Label(window, text="Osoba: ").grid(row=1, column=0, columnspan=2, sticky="w")
l2 = tk.Label(window, text="Rzeczownik w liczbie mnogiej: ").grid(row=2, column=0, columnspan=2, sticky="w")
l3= tk.Label(window, text="Czasownik: ").grid(row=3, column=0, columnspan=2, sticky="w")
l4 = tk.Label(window, text="Przymiotnik(i): ").grid(row=4, column=0, columnspan=2, sticky="w")
l5 = tk.Label(window, text="Część ciała: ").grid(row=5, column=0, columnspan=2, sticky="w")

entry1 = tk.Entry(window)
entry1.grid(row=1, column=1, sticky="w")
entry2 = tk.Entry(window)
entry2.grid(row=2, column=1, sticky="w")
entry3 = tk.Entry(window)
entry3.grid(row=3, column=1, sticky="w")

cb1 = tk.IntVar(value=0)
cb2 = tk.IntVar(value=0)
cb3 = tk.IntVar(value=0)

c1 = tk.Checkbutton(window, text="naglące", variable=cb1)
c1.grid(row=4, column=1, sticky="w")
c2 = tk.Checkbutton(window, text="radosne", variable=cb2)
c2.grid(row=4, column=2, sticky="w")
c3 = tk.Checkbutton(window, text="elektryzujące", variable=cb3)
c3.grid(row=4, column=3, sticky="w")

radioValue = tk.IntVar()

r1 = tk.Radiobutton(window, text="pępek", variable=radioValue, value=1)
r1.grid(row=5, column=1, sticky="w")
r2 = tk.Radiobutton(window, text="duży palec u nogi", variable=radioValue, value=2)
r2.grid(row=5, column=2, sticky="w")
r3 = tk.Radiobutton(window, text="rdzeń przedłuzony", variable=radioValue, value=3)
r3.grid(row=5, column=3, sticky="w")

tk.Button(window, text="Kliknij aby wyświetlić opowiadanie", command=showStory).grid(row=6, column=0, sticky="w")

textBox = tk.Text(window, height=15, wrap="word")
textBox.grid(row=7, column=0, columnspan=4)

window.mainloop()