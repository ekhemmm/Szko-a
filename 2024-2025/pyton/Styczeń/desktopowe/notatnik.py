import tkinter as tk
from tkinter import filedialog, messagebox
import os


class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Notatnik")
        self.root.geometry("800x600")

        self.text_area = tk.Text(self.root, wrap=tk.WORD, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        self.scrollbar = tk.Scrollbar(self.text_area)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=self.scrollbar.set)

        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Otwórz", command=self.open_file)
        self.file_menu.add_command(label="Zapisz", command=self.save_file)
        self.file_menu.add_command(label="Zapisz jako", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Zamknij", command=self.close_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Wyjdź", command=self.root.quit)
        self.menu_bar.add_cascade(label="Plik", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)
        
        self.operations_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.operations_menu.add_command(label="Oblicz słowa", command=self.words)
        self.menu_bar.add_cascade(label="Pokaż słowa", command=self.operations_menu)
        



        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.file_path = None

    def open_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension='txt',
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
            title="Otwórz plik"
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding="utf-8") as file:
                    content = file.read()
                    self.text_area.delete('1.0', tk.END)
                    self.text_area.insert(tk.END, content)
                    self.root.title(f"Notatnik - {os.path.basename(file_path)}")
                    self.file_path = file_path
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się otworzyć pliku:\n{e}")

    def close_file(self):
        self.text_area.delete(1.0, tk.END)
        self.root.title("Notatnik")
        self.file_path = None

    def save_file(self):
        if self.file_path:
            try:
                with open(self.file_path, 'w', encoding="utf-8") as file:
                    content = self.text_area.get(1.0, tk.END)
                    file.write(content)
                messagebox.showinfo("Zapisano", "Plik został zapisany pomyślnie")
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się zapisać pliku:\n{e}")
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension='txt',
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")],
            title="Zapisz jako"
        )
        if file_path:
            try:
                with open(file_path, 'w', encoding="utf-8") as file:
                    content = self.text_area.get(1.0, tk.END)
                    file.write(content)
                    self.root.title(f"Notatnik - {os.path.basename(file_path)}")
                    self.file_path = file_path
                messagebox.showinfo("Zapisano", "Plik został zapisany pomyślnie")
            except Exception as e:
                messagebox.showerror("Błąd", f"Nie udało się zapisać pliku:\n{e}")

    def on_closing(self):
        if messagebox.askokcancel("Wyjdź", "Czy na pewno chcesz zakończyć?"):
            self.root.destroy()

    def words():
        print("ddd")


if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
