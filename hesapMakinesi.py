
import tkinter as tk
from tkinter import ttk, messagebox
import math

class HesapMakinesi(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mavi-X16 Hesap Makinesi")
        self.geometry("400x600")
        self.configure(bg="#2c3e50")

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Sonuç ekranı
        result_frame = ttk.Frame(self, style="Result.TFrame")
        result_frame.pack(fill="x", padx=10, pady=20)

        self.result_label = ttk.Label(result_frame, textvariable=self.result_var, anchor="e", font=("Arial", 28), style="Result.TLabel")
        self.result_label.pack(fill="x")

        # Butonlar
        button_frame = ttk.Frame(self, style="Button.TFrame")
        button_frame.pack(fill="both", expand=True)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("√", 5, 1), ("10^x", 5, 2), ("log", 5, 3)
        ]

        for (text, row, col) in buttons:
            button = ttk.Button(button_frame, text=text, command=lambda t=text: self.on_button_click(t), style="Button.TButton")
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        for i in range(6):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)

        # Stiller
        self.style = ttk.Style(self)
        self.style.configure("Button.TButton", font=("Arial", 20), background="white", foreground="black", padding=20)
        self.style.map("Button.TButton", background=[("active", "#e0e0e0")], foreground=[("active", "black")])
        
        self.style.configure("Result.TFrame", background="#2c3e50")
        self.style.configure("Result.TLabel", background="#2c3e50", foreground="white")

    def on_button_click(self, value):
        if value == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Hata", "Geçersiz işlem veya sayı girdiniz!")
                self.result_var.set("")
        elif value == "C":
            self.result_var.set("")
        elif value == "√":
            try:
                result = math.sqrt(float(self.result_var.get()))
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Hata", "Geçersiz sayı girdiniz!")
                self.result_var.set("")
        elif value == "10^x":
            try:
                result = math.pow(10, float(self.result_var.get()))
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Hata", "Geçersiz sayı girdiniz!")
                self.result_var.set("")
        elif value == "log":
            try:
                result = math.log10(float(self.result_var.get()))
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Hata", "Geçersiz sayı girdiniz!")
                self.result_var.set("")
        else:
            self.result_var.set(self.result_var.get() + value)

if __name__ == "__main__":
    app = HesapMakinesi()
    app.mainloop()
