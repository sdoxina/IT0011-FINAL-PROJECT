import tkinter as tk
from tkinter import messagebox
from data_handler import load_products, save_products, load_orders

class AdminApp:
    def __init__(self, root, back_callback):
        self.root = root
        self.back_callback = back_callback

        tk.Label(root, text="Admin Panel", font=("Arial", 14)).grid(row=0, column=1, pady=10)

        tk.Button(root, text="View Orders", command=self.view_orders).grid(row=1, column=1, pady=5)
        tk.Button(root, text="Manage Products", command=self.manage_products).grid(row=2, column=1, pady=5)
        tk.Button(root, text="Back", command=self.back_callback).grid(row=3, column=1, pady=10)

    def view_orders(self):
        orders = load_orders()
        orders_str = "\n".join([f"{product}: {qty}" for product, qty in orders])
        messagebox.showinfo("Orders", orders_str if orders_str else "No orders yet!")

    def manage_products(self):
        self.manage_win = tk.Toplevel(self.root)
        self.manage_win.title("Manage Products")
        self.manage_win.geometry("500x300")

        self.products = load_products()
        row_count = 0

        for product, price in self.products:
            tk.Label(self.manage_win, text=f"{product} - ${price}").grid(row=row_count, column=0, padx=10)
            tk.Button(self.manage_win, text="Delete", command=lambda p=product: self.delete_product(p)).grid(row=row_count, column=1)
            row_count += 1

        tk.Label(self.manage_win, text="New Product:").grid(row=row_count, column=0)
        self.new_product = tk.Entry(self.manage_win)
        self.new_product.grid(row=row_count, column=1)

        tk.Label(self.manage_win, text="Price:").grid(row=row_count + 1, column=0)
        self.new_price = tk.Entry(self.manage_win)
        self.new_price.grid(row=row_count + 1, column=1)

        tk.Button(self.manage_win, text="Add Product", command=self.add_product).grid(row=row_count + 2, column=1, pady=10)

    def delete_product(self, product):
        self.products = [p for p in self.products if p[0] != product]
        save_products(self.products)
        messagebox.showinfo("Success", f"{product} deleted.")
        self.manage_win.destroy()
        self.manage_products()

    def add_product(self):
        product = self.new_product.get()
        try:
            price = float(self.new_price.get())
            self.products.append((product, price))
            save_products(self.products)
            messagebox.showinfo("Success", f"{product} added.")
            self.manage_win.destroy()
            self.manage_products()
        except ValueError:
            messagebox.showerror("Error", "Invalid price!")
