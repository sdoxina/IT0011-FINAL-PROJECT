import tkinter as tk
from tkinter import messagebox
from data_handler import load_products, load_orders
from manage_products import ManageProductsApp
from report import generate_report
from datetime import datetime

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
        orders = load_orders()
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
            row_count += 1

        tk.Button(self.root, text="Back", command=self.show_admin_menu).grid(row=row_count, column=1, pady=10)

    def generate_report(self):
        orders = load_orders()
        products = load_products()

        if not orders:
            messagebox.showinfo("Report", "No orders yet!")
            return

        report_data = generate_report(orders, products)

        self.clear_window()
        tk.Label(self.root, text=f"Daily Sales Report - {report_data['date']}", font=("Arial", 14, "bold")).grid(row=0, column=1, pady=10)

        tk.Label(self.root, text=f"Total Orders: {report_data['total_orders']}", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5)
        tk.Label(self.root, text=f"Total Revenue: PHP {report_data['total_revenue']:.2f}", font=("Arial", 12)).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Product", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=10, pady=5)
        tk.Label(self.root, text="Quantity Sold", font=("Arial", 12, "bold")).grid(row=2, column=1, padx=10, pady=5)

        row_count = 3
        for product, qty in report_data['product_sales'].items():
            tk.Label(self.root, text=product).grid(row=row_count, column=0, padx=10, pady=2)
            tk.Label(self.root, text=str(qty)).grid(row=row_count, column=1, padx=10, pady=2)
            row_count += 1

        tk.Button(self.root, text="Back", command=self.show_admin_menu).grid(row=row_count, column=1, pady=10)

    def manage_products(self):
        ManageProductsApp(self.root, self.show_admin_menu)

    def go_back(self, back_callback):
        self.clear_window()
        back_callback()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
