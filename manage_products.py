import tkinter as tk
from tkinter import messagebox
from data_handler import load_products, save_products

class ManageProductsApp:
    def __init__(self, root, back_callback):
        self.root = root
        self.back_callback = back_callback
        self.clear_window()
        self.show_product_management()

    def show_product_management(self):
        """Display all products and allow inline editing when Edit is clicked."""
        self.clear_window()
        tk.Label(self.root, text="Manage Products", font=("Arial", 14, "bold")).grid(row=0, column=1, pady=10)

        tk.Label(self.root, text="Name", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10)
        tk.Label(self.root, text="Price", font=("Arial", 12, "bold")).grid(row=1, column=1, padx=10)
        tk.Label(self.root, text="Stock", font=("Arial", 12, "bold")).grid(row=1, column=2, padx=10)

        self.products = load_products()
        self.product_widgets = {}  

        row_count = 2
        for product in self.products:
            self.display_product(product, row_count)
            row_count += 1

        tk.Button(self.root, text="Add Product", command=lambda: self.add_product(row_count)).grid(row=row_count, column=1, pady=10)
        tk.Button(self.root, text="Back", command=self.back_callback).grid(row=row_count + 1, column=1, pady=10)

    def display_product(self, product, row):
        """Displays a product row with labels, entry fields, and buttons."""
        name, price, stock = product["name"], product["price"], product["stock"]

        # Labels
        name_label = tk.Label(self.root, text=name)
        price_label = tk.Label(self.root, text=f"PHP {price}")
        stock_label = tk.Label(self.root, text=str(stock))

        name_label.grid(row=row, column=0, padx=10)
        price_label.grid(row=row, column=1)
        stock_label.grid(row=row, column=2)

        # Entry fields (hidden initially)
        price_entry = tk.Entry(self.root, width=10)
        price_entry.insert(0, str(price))
        stock_entry = tk.Entry(self.root, width=10)
        stock_entry.insert(0, str(stock))

        price_entry.grid(row=row, column=1)
        stock_entry.grid(row=row, column=2)

        price_entry.grid_remove()
        stock_entry.grid_remove()

        # Buttons
        edit_btn = tk.Button(self.root, text="Edit", command=lambda: self.toggle_edit(product, price_entry, stock_entry, price_label, stock_label, edit_btn, save_btn, cancel_btn))
        save_btn = tk.Button(self.root, text="Save", command=lambda: self.save_changes(product, price_entry, stock_entry, price_label, stock_label, edit_btn, save_btn, cancel_btn))
        cancel_btn = tk.Button(self.root, text="Cancel", command=lambda: self.cancel_edit(product, price_entry, stock_entry, price_label, stock_label, edit_btn, save_btn, cancel_btn))
        del_btn = tk.Button(self.root, text="Delete", command=lambda: self.delete_product(product))

        edit_btn.grid(row=row, column=3, padx=5)
        save_btn.grid(row=row, column=4, padx=5)
        cancel_btn.grid(row=row, column=5, padx=5)
        del_btn.grid(row=row, column=6, padx=5)

        save_btn.grid_remove()
        cancel_btn.grid_remove()

        # Store widgets
        self.product_widgets[product["name"]] = {
            "price_entry": price_entry,
            "stock_entry": stock_entry,
            "price_label": price_label,
            "stock_label": stock_label,
            "edit_button": edit_btn,
            "save_button": save_btn,
            "cancel_button": cancel_btn
        }

    def toggle_edit(self, product, price_entry, stock_entry, price_label, stock_label, edit_button, save_button, cancel_button):
        """Toggle between view mode and edit mode."""
        price_label.grid_remove()
        stock_label.grid_remove()
        price_entry.grid()
        stock_entry.grid()

        edit_button.grid_remove()
        save_button.grid()
        cancel_button.grid()

    def save_changes(self, product, price_entry, stock_entry, price_label, stock_label, edit_button, save_button, cancel_button):
        try:
            new_price = float(price_entry.get())
            new_stock = int(stock_entry.get())

            product["price"] = new_price
            product["stock"] = new_stock
            save_products(self.products)

            # Ensure correct formatting and remove unwanted characters
            price_label.config(text=f"PHP {new_price:.2f}")  # Enforce two decimal places
            stock_label.config(text=str(new_stock))

            # Reset UI elements
            price_entry.grid_remove()
            stock_entry.grid_remove()
            save_button.grid_remove()
            cancel_button.grid_remove()

            price_label.grid()
            stock_label.grid()
            edit_button.grid()

            messagebox.showinfo("Success", f"Updated {product['name']} successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

    def cancel_edit(self, product, price_entry, stock_entry, price_label, stock_label, edit_button, save_button, cancel_button):
        """Cancel edit and restore previous values."""
        price_entry.delete(0, tk.END)
        stock_entry.delete(0, tk.END)

        price_entry.insert(0, str(product["price"]))
        stock_entry.insert(0, str(product["stock"]))

        price_entry.grid_remove()
        stock_entry.grid_remove()
        save_button.grid_remove()
        cancel_button.grid_remove()

        price_label.grid()
        stock_label.grid()
        edit_button.grid()

    def add_product(self, row):
        """Add a new product and allow immediate editing."""
        new_product = {"name": "New Product", "price": 0.0, "stock": 0}
        self.products.append(new_product)

        # Entry fields for new product
        name_entry = tk.Entry(self.root, width=15)
        price_entry = tk.Entry(self.root, width=10)
        stock_entry = tk.Entry(self.root, width=10)

        name_entry.insert(0, "New Product")
        price_entry.insert(0, "0.0")
        stock_entry.insert(0, "0")

        name_entry.grid(row=row, column=0, padx=10)
        price_entry.grid(row=row, column=1)
        stock_entry.grid(row=row, column=2)

        # Save and Cancel buttons
        save_btn = tk.Button(self.root, text="Save", command=lambda: self.save_new_product(name_entry, price_entry, stock_entry, save_btn, cancel_btn, row))
        cancel_btn = tk.Button(self.root, text="Cancel", command=lambda: self.cancel_new_product(name_entry, price_entry, stock_entry, save_btn, cancel_btn))

        save_btn.grid(row=row, column=3, padx=5)
        cancel_btn.grid(row=row, column=4, padx=5)

    def save_new_product(self, name_entry, price_entry, stock_entry, save_btn, cancel_btn, row):
        """Save a new product from entry fields."""
        name = name_entry.get().strip()
        try:
            price = float(price_entry.get())
            stock = int(stock_entry.get())

            if not name:
                raise ValueError("Product name cannot be empty.")

            new_product = {"name": name, "price": price, "stock": stock}
            self.products[-1] = new_product  # Update the last added product
            save_products(self.products)

            # Destroy entry fields and buttons to prevent UI glitches
            name_entry.destroy()
            price_entry.destroy()
            stock_entry.destroy()
            save_btn.destroy()
            cancel_btn.destroy()

            # Display as a regular product row
            self.display_product(new_product, row)

            messagebox.showinfo("Success", f"Added {name} successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

    def cancel_new_product(self, name_entry, price_entry, stock_entry, save_btn, cancel_btn):
        """Cancel adding a new product and remove the entry fields."""
        self.products.pop()  # Remove the last added placeholder product
        name_entry.grid_remove()
        price_entry.grid_remove()
        stock_entry.grid_remove()
        save_btn.grid_remove()
        cancel_btn.grid_remove()

    def delete_product(self, product):
        """Delete a product from the list."""
        confirm = messagebox.askyesno("Delete Product", f"Are you sure you want to delete {product['name']}?")
        if confirm:
            self.products.remove(product)
            save_products(self.products)
            self.show_product_management()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
