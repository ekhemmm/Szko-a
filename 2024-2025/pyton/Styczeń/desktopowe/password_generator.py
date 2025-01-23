import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
 
 
class PasswordGeneratorApp:
    def __init__(self, master):
        master.title("Password generator")
        master.geometry("500x350")
        master.resizable(False,False)
        self.main_frame = ttk.Frame(master, padding="20 20 20 20")
        self.main_frame.pack(fill="both", expand=True)
        self.options_frame = ttk.LabelFrame(self.main_frame, text="character Options", padding="10 10 10 10")
        self.options_frame.pack(fill="x", expand=True, pady=10)
        self.include_letters = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)
        self.letters_check = ttk.Checkbutton(self.options_frame, text="Letters (A-Z, a-z)", variable=self.include_letters)
        self.letters_check.grid(row=0, column=0, sticky="w", pady=5)
        self.digits_check = ttk.Checkbutton(self.options_frame, text="Digits (0-9)", variable=self.include_digits)
        self.digits_check.grid(row=1, column=0, sticky="w", pady=5)
        self.special_check = ttk.Checkbutton(self.options_frame, text="Special Characters (!@#$...)", variable=self.include_special)
        self.special_check.grid(row=2, column=0, sticky="w", pady=5)
        self.length_frame = ttk.Frame(self.main_frame)
        self.length_frame.pack(fill="x", expand=True, pady=10)
        self.length_label = ttk.Label(self.length_frame, text="Password Length:")
        self.length_label.pack(side="left", padx=(0, 10))
        self.length_var = tk.IntVar(value=12)
        self.length_spinbox = ttk.Spinbox(self.length_frame, from_=4, to=64, textvariable=self.length_var, width=5)
        self.length_spinbox.pack(side='left')
        self.generate_button = ttk.Button(self.main_frame, text="Generate password", command=self.generate_password)
        self.generate_button.pack(pady=10)
        self.password_frame = ttk.Frame(self.main_frame)
        self.password_frame.pack(fill="x", expand=True, pady=10)
        self.password_label = ttk.Label(self.password_frame, text="Generated password: ")
        self.password_label.pack(side="left", padx=(0, 10))
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(self.password_frame, textvariable=self.password_var, width=30, state="readonly")
        self.password_entry.pack(side="left")
 
    def generate_password(self):
        print("Hasło")
 
 
def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()