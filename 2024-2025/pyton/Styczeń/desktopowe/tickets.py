import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

class TicketsReservationSystem():
    def __init__(self, root):
        self.root = root
        self.root.title("System rezerwacji biletów")
        self.root.geometry("800x400")
        self.data_file = "reservations.json"
        self.tree = ttk.Treeview(root, columns=("Imię", "Nazwisko", "Numer telefonu", "Liczba biletów"), show='headings')
        self.tree.heading("Imię", text="Imię")
        self.tree.heading("Nazwisko", text="Nazwisko")
        self.tree.heading("Numer telefonu", text="Numer telefonu")
        self.tree.heading("Liczba biletów", text="Liczba biletów")
        self.tree.pack(pady=20, fill=tk.BOTH, expand=True)
        self.load_data()
        self.add_button = tk.Button(root, text="Dodaj rezerwację", command=self.add_reservation)
        self.add_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.delete_button = tk.Button(root, text="Usuń rezerwację", command=self.delete_reservation)
        self.delete_button.pack(side=tk.LEFT, padx=10, pady=10)

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                reservations = json.load(f)
                for reservation in reservations:
                    self.tree.insert('', tk.END, values=(reservation['first_name'], reservation['last_name'], reservation['phone'], reservation['tickets']))

    def save_data(self, reservations):
        with open(self.data_file, 'w') as f:
            json.dump(reservations, f)

    def add_reservation(self):
        def save_new_reservation():
            first_name = first_name_entry.get()
            last_name = last_name_entry.get()
            phone = phone_entry.get()
            tickets = tickets_entry.get()

            if not first_name or not last_name or not phone or not tickets:
                messagebox.showerror("Błąd", "Wszystkie pola są wymagane!")
                return

            new_reservation = {"first_name": first_name, "last_name": last_name, "phone": phone, "tickets": tickets}

            self.tree.insert('', tk.END, values=(first_name, last_name, phone, tickets))
            reservations = []
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as f:
                    reservations = json.load(f)
            reservations.append(new_reservation)
            self.save_data(reservations)
            add_window.destroy()

        add_window = tk.Toplevel(self.root)
        add_window.title("Dodaj rezerwację")
        add_window.geometry("300x250")
        tk.Label(add_window, text="Imię").pack(pady=5)
        first_name_entry = tk.Entry(add_window)
        first_name_entry.pack()
        tk.Label(add_window, text="Nazwisko").pack(pady=5)
        last_name_entry = tk.Entry(add_window)
        last_name_entry.pack()
        tk.Label(add_window, text='Numer telefonu').pack(pady=5)
        phone_entry = tk.Entry(add_window)
        phone_entry.pack()
        tk.Label(add_window, text="Liczba biletów").pack(pady=5)
        tickets_entry = tk.Entry(add_window)
        tickets_entry.pack()
        tk.Button(add_window, text="Zapisz", command=save_new_reservation).pack(pady=10)

    def delete_reservation(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Błąd", "Nie wybrano rezerwacji do usunięcia")
            return
        item = self.tree.item(selected_item)
        values = item['values']
        self.tree.delete(selected_item)
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                reservations = json.load(f)
            updated_reservations = [res for res in reservations if res['first_name'] != values[0] or res['last_name'] != values[1]]
            self.save_data(updated_reservations)

def main():
    root = tk.Tk()
    app = TicketsReservationSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()