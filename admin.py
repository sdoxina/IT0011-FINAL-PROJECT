# Import required modules
import tkinter as tk
from tkinter import messagebox  # To show pop-up messages
from data_handler import load_products, load_orders  # Import functions to load products and orders data
from manage_products import ManageProductsApp  # Import the ManageProductsApp module
from report import generate_report  # Import the function to generate the sales report

# AdminApp class to handle the admin panel functionality
class AdminApp:  
    def __init__(self, root, back_callback):
        self.root = root  # Reference to the root window
        self.back_callback = lambda: self.go_back(back_callback)  # Callback function for going back
        self.root.geometry("600x600")  # Set the window size
        self.root.configure(bg="#FFC0CB")  # Set background color to pink
        self.clear_window()  # Clear any existing widgets in the window
        self.show_admin_menu()  # Display the admin menu

    # Method to show the admin menu with options
    def show_admin_menu(self):
        self.clear_window()  # Clear the window before displaying the menu
        
        # Title label for Admin Panel
        tk.Label(self.root, text="Admin Panel", font=("Poppins", 16, "bold"), pady=10, bg="#FFC0CB", fg="black").pack(fill='x', pady=10)
        
        # Buttons for different admin options
        tk.Button(self.root, text="View Orders", font=("Poppins", 12), bg="white", fg="black", command=self.view_orders, highlightthickness=0).pack(pady=5)
        tk.Button(self.root, text="Manage Products", font=("Poppins", 12), bg="white", fg="black", command=self.manage_products, highlightthickness=0).pack(pady=5)
        tk.Button(self.root, text="Generate Report", font=("Poppins", 12), bg="white", fg="black", command=self.generate_report, highlightthickness=0).pack(pady=5)
        tk.Button(self.root, text="Back", font=("Poppins", 12), bg="white", fg="black", command=self.back_callback, highlightthickness=0).pack(pady=10)

    # Method to view orders made by customers
    def view_orders(self):
        orders = load_orders()  # Load the orders data
        if not orders:
            messagebox.showinfo("Orders", "No orders yet!")  # Show info if there are no orders
            return

        self.clear_window()  # Clear the window to display orders
        
        # Label to show the title of the section
        tk.Label(self.root, text="Customer Orders", font=("Poppins", 18, "bold"), pady=10, bg="#FFC0CB", fg="black").pack()

        # Scrollable frame setup for displaying orders
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

        # Table Headers for customer, product, and quantity
        tk.Label(scrollable_frame, text="Customer", font=("Poppins", 12, "bold"), padx=20, bg="#FFC0CB", fg="black").grid(row=0, column=0)
        tk.Label(scrollable_frame, text="Product", font=("Poppins", 12, "bold"), padx=20, bg="#FFC0CB", fg="black").grid(row=0, column=1)
        tk.Label(scrollable_frame, text="Quantity", font=("Poppins", 12, "bold"), padx=20, bg="#FFC0CB", fg="black").grid(row=0, column=2)

        # Display each order in the scrollable frame
        row_count = 1
        for customer, items in orders.items():
            tk.Label(scrollable_frame, text=customer, font=("Poppins", 11, "bold"), padx=20, bg="#FFC0CB", fg="black").grid(row=row_count, column=0, sticky="w")
            for product, qty in items.items():
                tk.Label(scrollable_frame, text=product, font=("Poppins", 11), padx=20, bg="#FFC0CB", fg="black").grid(row=row_count, column=1)
                tk.Label(scrollable_frame, text=str(qty), font=("Poppins", 11), padx=20, bg="#FFC0CB", fg="black").grid(row=row_count, column=2)
                row_count += 1
            row_count += 1

        # Back button to return to the admin menu
        tk.Button(self.root, text="Back", font=("Poppins", 12), bg="white", fg="black", command=self.show_admin_menu, highlightthickness=0).pack(pady=10)

    # Method to generate the sales report
    def generate_report(self):
        orders = load_orders()  # Load orders data
        products = load_products()  # Load products data

        if not orders:
            messagebox.showinfo("Report", "No orders yet!")  # Show info if there are no orders
            return

        report_data = generate_report(orders, products)  # Generate the sales report

        self.clear_window()  # Clear the window to display the report

        # Display report title and summary information
        tk.Label(self.root, text=f"Daily Sales Report - {report_data['date']}", 
                font=("Poppins", 16, "bold"), pady=10, bg="#FFC0CB", fg="black").pack()

        tk.Label(self.root, text=f"Total Orders: {report_data['total_orders']}", 
                font=("Poppins", 12), bg="#FFC0CB", fg="black").pack()
        
        tk.Label(self.root, text=f"Total Revenue: PHP {report_data['total_revenue']:.2f}", 
                font=("Poppins", 12), bg="#FFC0CB", fg="black").pack()

        # Frame for the product breakdown table
        table_frame = tk.Frame(self.root, bg="#FFC0CB")
        table_frame.pack(pady=10)

        # Column Headers for the product breakdown table
        tk.Label(table_frame, text="Product Name", font=("Poppins", 12, "bold"), 
                bg="#FFC0CB", fg="black", padx=10).grid(row=0, column=0)
        tk.Label(table_frame, text="Quantity Sold", font=("Poppins", 12, "bold"), 
                bg="#FFC0CB", fg="black", padx=10).grid(row=0, column=1)
        tk.Label(table_frame, text="Total Sales (PHP)", font=("Poppins", 12, "bold"), 
                bg="#FFC0CB", fg="black", padx=10).grid(row=0, column=2)

        # Display each product's sales data in the table
        for idx, (product, details) in enumerate(report_data["product_sales"].items(), start=1):
            tk.Label(table_frame, text=product, font=("Poppins", 12), bg="#FFC0CB", fg="black").grid(row=idx, column=0, padx=10)
            tk.Label(table_frame, text=details["quantity_sold"], font=("Poppins", 12), bg="#FFC0CB", fg="black").grid(row=idx, column=1, padx=10)
            tk.Label(table_frame, text=f"PHP {details['total_sales']:.2f}", font=("Poppins", 12), bg="#FFC0CB", fg="black").grid(row=idx, column=2, padx=10)

        # Back button to return to the admin menu
        tk.Button(self.root, text="Back", font=("Poppins", 12), bg="white", 
                fg="black", command=self.show_admin_menu, highlightthickness=0).pack(pady=10)

    # Method to manage products in the system
    def manage_products(self):
        self.root.configure(bg="#FFC0CB")  # Ensure background color consistency
        ManageProductsApp(self.root, self.show_admin_menu)  # Open the ManageProductsApp window

    # Method to go back to the previous screen
    def go_back(self, back_callback):
        self.clear_window()  # Clear the window before going back
        back_callback()  # Call the provided back callback

    # Method to clear any existing widgets from the window
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()  # Destroy each widget in the window to clear the content
