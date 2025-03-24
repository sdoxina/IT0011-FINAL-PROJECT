import tkinter as tk
from tkinter import messagebox
from data_handler import load_products, save_orders

class CustomerApp:
    def __init__(self, root, back_callback):
        self.root = root
        self.back_callback = back_callback

        tk.Label(root, text="Available Skincare Products", font=("Arial", 14)).grid(row=0, column=1)

        self.products = load_products()
        self.cart = {}

        row_count = 1
        for product, price in self.products:
            tk.Label(root, text=f"{product} - ${price}", font=("Arial", 12)).grid(row=row_count, column=0, padx=10)
            quantity = tk.Entry(root, width=5)
            quantity.grid(row=row_count, column=1)
            tk.Button(root, text="Add to Cart", command=lambda p=product, q=quantity: self.add_to_cart(p, q)).grid(row=row_count, column=2)
            row_count += 1

        tk.Button(root, text="Checkout", command=self.checkout).grid(row=row_count, column=1, pady=10)
        tk.Button(root, text="Back", command=self.back_callback).grid(row=row_count + 1, column=1, pady=10)

    def add_to_cart(self, product, quantity_entry):
        try:
            qty = int(quantity_entry.get())
            if qty > 0:
                self.cart[product] = qty
                messagebox.showinfo("Cart", f"Added {qty} {product}(s) to cart.")
        except ValueError:
            messagebox.showerror("Error", "Enter a valid quantity!")

    def checkout(self):
        if not self.cart:
            messagebox.showwarning("Cart", "Cart is empty!")
            return

        save_orders(self.cart)
        messagebox.showinfo("Order", "Order placed successfully!")
        self.cart.clear()
