import tkinter as tk
from customer import CustomerApp
from admin import AdminApp

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Skincare Management System")
        self.root.geometry("600x400")
        
        self.show_main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_window()

        tk.Label(self.root, text="Welcome to Skincare Store", font=("Arial", 14)).grid(row=0, column=1, pady=20)

        tk.Button(self.root, text="Customer", command=self.show_customer, width=20, height=2).grid(row=1, column=1, pady=10)
        tk.Button(self.root, text="Admin", command=self.show_admin, width=20, height=2).grid(row=2, column=1, pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=20, height=2).grid(row=3, column=1, pady=10)

    def show_customer(self):
        self.clear_window()
        CustomerApp(self.root, self.show_main_menu)

    def show_admin(self):
        self.clear_window()
        AdminApp(self.root, self.show_main_menu)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
