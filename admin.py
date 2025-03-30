import tkinter as tk
from tkinter import messagebox
from data_handler import load_products, save_products, load_orders
from manage_products import ManageProductsApp

class AdminApp:
    def __init__(self, root, back_callback):
        self.root = root
        self.back_callback = lambda: self.go_back(back_callback)

        self.clear_window()
        self.show_admin_menu()

    def show_admin_menu(self):
        self.clear_window()
        tk.Label(self.root, text="Admin Panel", font=("Arial", 14)).grid(row=0, column=1, pady=10)

        tk.Button(self.root, text="View Orders", command=self.view_orders).grid(row=1, column=1, pady=5)
        tk.Button(self.root, text="Manage Products", command=self.manage_products).grid(row=2, column=1, pady=5)
        tk.Button(self.root, text="Generate Report", command=self.generate_report).grid(row=3, column=1, pady=5)
        tk.Button(self.root, text="Back", command=self.back_callback).grid(row=4, column=1, pady=10)

    def view_orders(self):
        orders = load_orders()  # Now returns a dictionary
        if not orders:
            messagebox.showinfo("Orders", "No orders yet!")
            return

        self.clear_window()
        tk.Label(self.root, text="Customer Orders", font=("Arial", 14, "bold")).grid(row=0, column=1, pady=10)

        # Table Headers
        tk.Label(self.root, text="Customer", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.root, text="Product", font=("Arial", 12, "bold")).grid(row=1, column=1, padx=10, pady=5)
        tk.Label(self.root, text="Quantity", font=("Arial", 12, "bold")).grid(row=1, column=2, padx=10, pady=5)

        row_count = 2
        for customer, items in orders.items():
            tk.Label(self.root, text=customer, font=("Arial", 11, "bold")).grid(row=row_count, column=0, padx=10, pady=2, sticky="w")
            for product, qty in items.items():
                tk.Label(self.root, text=product).grid(row=row_count, column=1, padx=10, pady=2)
                tk.Label(self.root, text=str(qty)).grid(row=row_count, column=2, padx=10, pady=2)
                row_count += 1
            row_count += 1  # Space between customers

        tk.Button(self.root, text="Back", command=self.show_admin_menu).grid(row=row_count, column=1, pady=10)

    def generate_report(self):
        orders = load_orders()
        
        total_orders = sum(len(items) for items in orders.values())  # Count total purchased items
        total_sales = sum(qty for items in orders.values() for qty in items.values())  # Sum all quantities

        messagebox.showinfo("Report", f"Total Orders: {total_orders}\nTotal Sales: {total_sales}")


    def manage_products(self):
        ManageProductsApp(self.root, self.show_admin_menu)

    def go_back(self, back_callback):
        self.clear_window()
        back_callback()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()