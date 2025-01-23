import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class TicketsReservationSystem():
    def __init__(self, root):
        self.root = root 
        self.root.title = ("Systen rezerwacji biletów")
        self.root.geometry("800x400")
        self.data_file = "reservations.json"
        self.tree = ttk.Treeview(root,
                                 columns=("Imię", "Nazwisko", "Numer telefonu", "Liczba biletów"),
                                 show='headings')
        self.tree.heading("Imię", text="Imię")
        self.tree.heading("Nazwisko", text="Nazwisko")
        self.tree.heading("Numer telefonu", text="Numer telefonu")
        self.tree.heading("Liczba biletów", text="Liczba biletów")
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)
        self.load_data()
        self.add_button = tk.Button(root, text="Dodaj rezerwację")
        self.add_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.delete_button = tk.Button(root, text="Usuń rezerwację")
        self.delete_button.pack(side=tk.LEFT, padx=10, pady=10)
    
    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                reservations = json.load(f)
                for reservation in reservations:
                    self.tree.insert('', tk.END, values=(reservation['first_name'], reservation['lest_name'], reservation['phone'], reservation['tickets']))
    
    def save_data(self, reservations):
        with open(self.data_file, 'w') as f:
            json.dump(reservations, f)
    
    def main():
        root = tk.Tk()
        app = TicketsReservationSystem(root)
        root.mainloop()
    
    if __name__ == "__main__":
        main()