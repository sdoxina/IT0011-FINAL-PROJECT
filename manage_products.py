import tkinter as tk
from tkinter import messagebox
from data_handler import load_products, save_products

class ManageProductsApp:
    def __init__(self, root, back_callback):
        self.root = root
        self.root.geometry("630x800")
        self.root.configure(bg="#FFC0CB")  # Ensures background consistency
        self.back_callback = back_callback
        self.clear_window()
        self.show_product_management()

    def show_product_management(self):
        self.clear_window()
        frame = tk.Frame(self.root, bg="#FFC0CB")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="Manage Products", font=("Poppins", 20, "bold"), bg="#FFC0CB").grid(row=0, column=1, pady=10)
        
        tk.Label(frame, text="Name", font=("Poppins", 12, "bold"), bg="#FFC0CB").grid(row=1, column=0, padx=10)
        tk.Label(frame, text="Price", font=("Poppins", 12, "bold"), bg="#FFC0CB").grid(row=1, column=1, padx=10)
        tk.Label(frame, text="Stock", font=("Poppins", 12, "bold"), bg="#FFC0CB").grid(row=1, column=2, padx=10)
        
        self.products = load_products()
        self.product_widgets = {}
        
        row_count = 2
        for product in self.products:
            self.display_product(frame, product, row_count)
            row_count += 1
        
        self.add_product_button = tk.Button(frame, text="Add Product", command=lambda: self.add_product(frame, row_count), font=("Poppins", 12))
        self.add_product_button.grid(row=row_count, column=1, pady=10)
        
        tk.Button(frame, text="Back", command=self.back_callback, font=("Poppins", 12)).grid(row=row_count + 1, column=1, pady=10)

    def add_product(self, frame, row_count):
        # Create new entry fields for product name, price, and stock
        self.product_name_entry = tk.Entry(frame, font=("Poppins", 12), highlightthickness=0, relief="flat", bg="#FFC0CB")
        self.product_price_entry = tk.Entry(frame, font=("Poppins", 12), highlightthickness=0, relief="flat", bg="#FFC0CB")
        self.product_stock_entry = tk.Entry(frame, font=("Poppins", 12), highlightthickness=0, relief="flat", bg="#FFC0CB")
        
        self.product_name_entry.grid(row=row_count, column=0, padx=10)
        self.product_price_entry.grid(row=row_count, column=1)
        self.product_stock_entry.grid(row=row_count, column=2)
        
        self.save_new_product_button = tk.Button(frame, text="Save", command=lambda: self.save_new_product(frame, row_count), font=("Poppins", 12))
        self.save_new_product_button.grid(row=row_count, column=3, padx=10)
        self.cancel_new_product_button = tk.Button(frame, text="Cancel", command=lambda: self.cancel_new_product(frame, row_count), font=("Poppins", 12))
        self.cancel_new_product_button.grid(row=row_count, column=4, padx=10)

    def save_new_product(self, frame, row_count):
        # Get values from the entry fields
        name = self.product_name_entry.get()
        price = self.product_price_entry.get()
        stock = self.product_stock_entry.get()
        
        if not name or not price or not stock:
            messagebox.showerror("Error", "Please fill in all fields!")
            return
        
        # Add the new product to the list
        new_product = {"name": name, "price": price, "stock": stock}
        self.products.append(new_product)
        
        # Save the products list
        save_products(self.products)

        # Update the display and buttons
        self.show_product_management()

    def cancel_new_product(self, frame, row_count):
        # Clear the entry fields and buttons for adding new product
        self.product_name_entry.grid_forget()
        self.product_price_entry.grid_forget()
        self.product_stock_entry.grid_forget()
        self.save_new_product_button.grid_forget()
        self.cancel_new_product_button.grid_forget()

    def display_product(self, frame, product, row):
        name, price, stock = product["name"], product["price"], product["stock"]

        name_label = tk.Label(frame, text=name, font=("Poppins", 12), bg="#FFC0CB")
        price_label = tk.Label(frame, text=f"PHP {price}", font=("Poppins", 12), bg="#FFC0CB")
        stock_label = tk.Label(frame, text=str(stock), font=("Poppins", 12), bg="#FFC0CB")

        name_label.grid(row=row, column=0, padx=10)
        price_label.grid(row=row, column=1)
        stock_label.grid(row=row, column=2)

        price_entry = tk.Entry(frame, width=15, font=("Poppins", 12), highlightthickness=0, relief="flat", bg="#FFC0CB")
        price_entry.insert(0, str(price))
        stock_entry = tk.Entry(frame, width=15, font=("Poppins", 12), highlightthickness=0, relief="flat", bg="#FFC0CB")
        stock_entry.insert(0, str(stock))

        price_entry.grid(row=row, column=1)
        stock_entry.grid(row=row, column=2)

        price_entry.grid_remove()
        stock_entry.grid_remove()
        
        edit_btn = tk.Button(frame, text="Edit", command=lambda: self.toggle_edit(product, price_entry, stock_entry, price_label, stock_label, edit_btn, save_btn, cancel_btn), font=("Poppins", 12))
        save_btn = tk.Button(frame, text="Save", command=lambda: self.save_changes(product, price_entry, stock_entry, price_label, stock_label, edit_btn, save_btn, cancel_btn), font=("Poppins", 12))
        cancel_btn = tk.Button(frame, text="Cancel", command=lambda: self.cancel_edit(product, price_entry, stock_entry, price_label, stock_label, edit_btn, save_btn, cancel_btn), font=("Poppins", 12))
        del_btn = tk.Button(frame, text="Delete", command=lambda: self.delete_product(product), font=("Poppins", 12))

        edit_btn.grid(row=row, column=3, padx=5)
        save_btn.grid(row=row, column=4, padx=5)
        cancel_btn.grid(row=row, column=5, padx=5)
        del_btn.grid(row=row, column=6, padx=5)

        save_btn.grid_remove()
        cancel_btn.grid_remove()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def delete_product(self, product):
        self.products.remove(product)
        save_products(self.products)
        self.show_product_management()

    def save_changes(self, product, price_entry, stock_entry, price_label, stock_label, edit_btn, save_btn, cancel_btn):
        price = price_entry.get()
        stock = stock_entry.get()
        
        product["price"] = price
        product["stock"] = stock
        
        save_products(self.products)
        
        price_label.config(text=f"PHP {price}")
        stock_label.config(text=stock)
        
        self.toggle_edit(product, price_entry, stock_entry, price_label, stock_label, edit_btn, save_btn, cancel_btn)

    def cancel_edit(self, product, price_entry, stock_entry, price_label, stock_label, edit_btn, save_btn, cancel_btn):
        price_entry.grid_remove()
        stock_entry.grid_remove()
        save_btn.grid_remove()
        cancel_btn.grid_remove()
        
        price_label.config(text=f"PHP {product['price']}")
        stock_label.config(text=str(product['stock']))
        
        edit_btn.grid()
