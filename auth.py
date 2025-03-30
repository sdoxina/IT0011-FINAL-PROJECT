import tkinter as tk
from tkinter import messagebox

class AdminAuth:
    def __init__(self, root, success_callback):
        self.root = root
        self.success_callback = success_callback

        tk.Label(root, text="Admin Login", font=("Arial", 14)).grid(row=0, column=1, pady=10)
        tk.Label(root, text="Username:").grid(row=1, column=0, padx=10)
        tk.Label(root, text="Password:").grid(row=2, column=0, padx=10)

        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=1, column=1)

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=2, column=1)

        tk.Button(root, text="Login", command=self.authenticate).grid(row=3, column=1, pady=10)
        tk.Button(root, text="Back", command=self.success_callback).grid(row=4, column=1, pady=10)

    def authenticate(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin123":
            messagebox.showinfo("Login Success", "Welcome, Admin!")
            self.success_callback()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials!")
