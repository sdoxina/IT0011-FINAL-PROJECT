import tkinter as tk
from tkinter import messagebox
from data_handler import load_products, load_orders
from manage_products import ManageProductsApp
from report import generate_report

class AdminApp:  
    def __init__(self, root, back_callback):
        self.root = root
        self.back_callback = lambda: self.go_back(back_callback)
        self.root.geometry("600x600")
        self.root.configure(bg="#FFC0CB")  # Set background color
        self.clear_window()
        self.show_admin_menu()

    def show_admin_menu(self):
        self.clear_window()
        
        # Title
        tk.Label(self.root, text="Admin Panel", font=("Poppins", 16, "bold"), pady=10, bg="#FFC0CB", fg="black").pack(fill='x', pady=10)
        
        # Buttons
        tk.Button(self.root, text="View Orders", font=("Poppins", 12), bg="white", fg="black", command=self.view_orders, highlightthickness=0).pack(pady=5)
        tk.Button(self.root, text="Manage Products", font=("Poppins", 12), bg="white", fg="black", command=self.manage_products, highlightthickness=0).pack(pady=5)
        tk.Button(self.root, text="Generate Report", font=("Poppins", 12), bg="white", fg="black", command=self.generate_report, highlightthickness=0).pack(pady=5)
        tk.Button(self.root, text="Back", font=("Poppins", 12), bg="white", fg="black", command=self.back_callback, highlightthickness=0).pack(pady=10)

    def view_orders(self):
        orders = load_orders()
        if not orders:
            messagebox.showinfo("Orders", "No orders yet!")
            return

        self.clear_window()
        
        tk.Label(self.root, text="Customer Orders", font=("Poppins", 18, "bold"), pady=10, bg="#FFC0CB", fg="black").pack()

        # Scrollable frame setup
        container = tk.Frame(self.root, bg="#FFC0CB")
        container.pack(fill="both", expand=True, padx=10, pady=5)

        canvas = tk.Canvas(container, bg="#FFC0CB", highlightthickness=0)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview, bd=0, highlightthickness=0)
        scrollable_frame = tk.Frame(canvas, bg="#FFC0CB")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Table Headers
        tk.Label(scrollable_frame, text="Customer", font=("Poppins", 12, "bold"), padx=20, bg="#FFC0CB", fg="black").grid(row=0, column=0)
        tk.Label(scrollable_frame, text="Product", font=("Poppins", 12, "bold"), padx=20, bg="#FFC0CB", fg="black").grid(row=0, column=1)
        tk.Label(scrollable_frame, text="Quantity", font=("Poppins", 12, "bold"), padx=20, bg="#FFC0CB", fg="black").grid(row=0, column=2)

        row_count = 1
        for customer, items in orders.items():
            tk.Label(scrollable_frame, text=customer, font=("Poppins", 11, "bold"), padx=20, bg="#FFC0CB", fg="black").grid(row=row_count, column=0, sticky="w")
            for product, qty in items.items():
                tk.Label(scrollable_frame, text=product, font=("Poppins", 11), padx=20, bg="#FFC0CB", fg="black").grid(row=row_count, column=1)
                tk.Label(scrollable_frame, text=str(qty), font=("Poppins", 11), padx=20, bg="#FFC0CB", fg="black").grid(row=row_count, column=2)
                row_count += 1
            row_count += 1

        tk.Button(self.root, text="Back", font=("Poppins", 12), bg="white", fg="black", command=self.show_admin_menu, highlightthickness=0).pack(pady=10)

    def generate_report(self):
        orders = load_orders()
        products = load_products()

        if not orders:
            messagebox.showinfo("Report", "No orders yet!")
            return

        report_data = generate_report(orders, products)

        self.clear_window()
        
        tk.Label(self.root, text=f"Daily Sales Report - {report_data['date']}", font=("Poppins", 16, "bold"), pady=10, bg="#FFC0CB", fg="black").pack()

        tk.Label(self.root, text=f"Total Orders: {report_data['total_orders']}", font=("Poppins", 12), bg="#FFC0CB", fg="black").pack()
        tk.Label(self.root, text=f"Total Revenue: PHP {report_data['total_revenue']:.2f}", font=("Poppins", 12), bg="#FFC0CB", fg="black").pack()

        tk.Button(self.root, text="Back", font=("Poppins", 12), bg="white", fg="black", command=self.show_admin_menu, highlightthickness=0).pack(pady=10)

    def manage_products(self):
        self.root.configure(bg="#FFC0CB")  # Ensure background color consistency
        ManageProductsApp(self.root, self.show_admin_menu)

    def go_back(self, back_callback):
        self.clear_window()
        back_callback()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()