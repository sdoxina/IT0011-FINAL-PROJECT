import tkinter as tk
from tkinter import messagebox
from data_handler import load_products, load_orders
from manage_products import ManageProductsApp
from report import generate_report

class AdminApp:  
    def __init__(self, root, back_callback):
        self.root = root
        self.back_callback = lambda: self.go_back(back_callback)
        self.root.geometry("400x400")
        self.clear_window()
        self.show_admin_menu()

    def show_admin_menu(self):
        self.clear_window()
        
        # Title
        tk.Label(self.root, text="Admin Panel", font=("Poppins", 16, "bold"), pady=10, bg="#FFC0CB").pack(fill='x', pady=10)
        
        # Buttons
        tk.Button(self.root, text="View Orders", font=("Poppins", 12), command=self.view_orders).pack(pady=5)
        tk.Button(self.root, text="Manage Products", font=("Poppins", 12), command=self.manage_products).pack(pady=5)
        tk.Button(self.root, text="Generate Report", font=("Poppins", 12), command=self.generate_report).pack(pady=5)
        tk.Button(self.root, text="Back", font=("Poppins", 12), command=self.back_callback).pack(pady=10)

    def view_orders(self):
        orders = load_orders()
        if not orders:
            messagebox.showinfo("Orders", "No orders yet!")
            return

        self.clear_window()
        
        tk.Label(self.root, text="Customer Orders", font=("Poppins", 16, "bold"), pady=10).pack()

        # Table Headers
        frame = tk.Frame(self.root)
        frame.pack()
        
        tk.Label(frame, text="Customer", font=("Poppins", 12, "bold"), padx=20).grid(row=0, column=0)
        tk.Label(frame, text="Product", font=("Poppins", 12, "bold"), padx=20).grid(row=0, column=1)
        tk.Label(frame, text="Quantity", font=("Poppins", 12, "bold"), padx=20).grid(row=0, column=2)

        row_count = 1
        for customer, items in orders.items():
            tk.Label(frame, text=customer, font=("Poppins", 11, "bold"), padx=20).grid(row=row_count, column=0, sticky="w")
            for product, qty in items.items():
                tk.Label(frame, text=product, font=("Poppins", 11), padx=20).grid(row=row_count, column=1)
                tk.Label(frame, text=str(qty), font=("Poppins", 11), padx=20).grid(row=row_count, column=2)
                row_count += 1
            row_count += 1

        tk.Button(self.root, text="Back", font=("Poppins", 12), command=self.show_admin_menu).pack(pady=10)

    def generate_report(self):
        orders = load_orders()
        products = load_products()

        if not orders:
            messagebox.showinfo("Report", "No orders yet!")
            return

        report_data = generate_report(orders, products)

        self.clear_window()
        
        tk.Label(self.root, text=f"Daily Sales Report - {report_data['date']}", font=("Poppins", 16, "bold"), pady=10).pack()

        tk.Label(self.root, text=f"Total Orders: {report_data['total_orders']}", font=("Poppins", 12)).pack()
        tk.Label(self.root, text=f"Total Revenue: PHP {report_data['total_revenue']:.2f}", font=("Poppins", 12)).pack()

        frame = tk.Frame(self.root)
        frame.pack()
        
        tk.Label(frame, text="Product", font=("Poppins", 12, "bold"), padx=20).grid(row=0, column=0)
        tk.Label(frame, text="Quantity Sold", font=("Poppins", 12, "bold"), padx=20).grid(row=0, column=1)

        row_count = 1
        for product, qty in report_data['product_sales'].items():
            tk.Label(frame, text=product, font=("Poppins", 11), padx=20).grid(row=row_count, column=0)
            tk.Label(frame, text=str(qty), font=("Poppins", 11), padx=20).grid(row=row_count, column=1)
            row_count += 1

        tk.Button(self.root, text="Back", font=("Poppins", 12), command=self.show_admin_menu).pack(pady=10)

    def manage_products(self):
        ManageProductsApp(self.root, self.show_admin_menu)

    def go_back(self, back_callback):
        self.clear_window()
        back_callback()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
