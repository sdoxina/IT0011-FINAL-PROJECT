import tkinter as tk
from tkinter import messagebox
from data_handler import load_products, save_products

class ManageProductsApp:
    def __init__(self, root, back_callback):
        self.root = root
<<<<<<< HEAD
        self.root.geometry("630x700")
        self.root.configure(bg="#FFC0CB")  # Ensures background consistency
=======
        self.root.geometry("580x720")  # Set window size wider
>>>>>>> ca57288e821232d411fcc7927306cac513df58c8
        self.back_callback = back_callback
        self.clear_window()
        self.show_product_management()

    def show_product_management(self):
        self.clear_window()
        tk.Label(self.root, text="Manage Products", font=("Poppins", 14, "bold")).grid(row=0, column=1, pady=10)

        tk.Label(self.root, text="Name", font=("Poppins", 12, "bold")).grid(row=1, column=0, padx=10)
        tk.Label(self.root, text="Price", font=("Poppins", 12, "bold")).grid(row=1, column=1, padx=10)
        tk.Label(self.root, text="Stock", font=("Poppins", 12, "bold")).grid(row=1, column=2, padx=10)

        self.products = load_products()
        self.product_widgets = {}  

        row_count = 2
        for product in self.products:
            self.display_product(product, row_count)
            row_count += 1

<<<<<<< HEAD
    def add_product(self, frame, row_count):
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
        name = self.product_name_entry.get()
        price = self.product_price_entry.get()
        stock = self.product_stock_entry.get()
        
        if not name or not price or not stock:
            messagebox.showerror("Error", "Please fill in all fields!")
            return
        
        new_product = {"name": name, "price": price, "stock": stock}
        self.products.append(new_product)
        save_products(self.products)
        self.show_product_management()

    def cancel_new_product(self, frame, row_count):
        self.product_name_entry.grid_forget()
        self.product_price_entry.grid_forget()
        self.product_stock_entry.grid_forget()
        self.save_new_product_button.grid_forget()
        self.cancel_new_product_button.grid_forget()

    def display_product(self, frame, product, row):
=======
        tk.Button(self.root, text="Add Product", command=lambda: self.add_product(row_count), font=("Poppins", 12)).grid(row=row_count, column=1, pady=10)
        tk.Button(self.root, text="Back", command=self.back_callback, font=("Poppins", 12)).grid(row=row_count + 1, column=1, pady=10)

    def display_product(self, product, row):
>>>>>>> ca57288e821232d411fcc7927306cac513df58c8
        name, price, stock = product["name"], product["price"], product["stock"]

        # Labels
        name_label = tk.Label(self.root, text=name, font=("Poppins", 12))
        price_label = tk.Label(self.root, text=f"PHP {price}", font=("Poppins", 12))
        stock_label = tk.Label(self.root, text=str(stock), font=("Poppins", 12))

        name_label.grid(row=row, column=0, padx=10)
        price_label.grid(row=row, column=1)
        stock_label.grid(row=row, column=2)

<<<<<<< HEAD
        # Create editable entries for name, price, and stock
        name_entry = tk.Entry(frame, font=("Poppins", 12), highlightthickness=0, relief="flat", bg="#FFC0CB")
        name_entry.insert(0, name)
        price_entry = tk.Entry(frame, width=15, font=("Poppins", 12), highlightthickness=0, relief="flat", bg="#FFC0CB")
=======
        # Entry fields
        name_entry = tk.Entry(self.root, width=15, font=("Poppins", 12))
        price_entry = tk.Entry(self.root, width=15, font=("Poppins", 12))
        stock_entry = tk.Entry(self.root, width=15, font=("Poppins", 12))

        name_entry.insert(0, name)
>>>>>>> ca57288e821232d411fcc7927306cac513df58c8
        price_entry.insert(0, str(price))
        stock_entry.insert(0, str(stock))

<<<<<<< HEAD
        name_entry.grid(row=row, column=0)
=======
        name_entry.grid(row=row, column=0, padx=10)
>>>>>>> ca57288e821232d411fcc7927306cac513df58c8
        price_entry.grid(row=row, column=1)
        stock_entry.grid(row=row, column=2)

        name_entry.grid_remove()
        price_entry.grid_remove()
        stock_entry.grid_remove()

<<<<<<< HEAD
        edit_btn = tk.Button(frame, text="Edit", command=lambda: self.toggle_edit(product, name_entry, price_entry, stock_entry, name_label, price_label, stock_label, edit_btn, save_btn, cancel_btn), font=("Poppins", 12))
        save_btn = tk.Button(frame, text="Save", command=lambda: self.save_changes(product, name_entry, price_entry, stock_entry, name_label, price_label, stock_label, edit_btn, save_btn, cancel_btn), font=("Poppins", 12))
        cancel_btn = tk.Button(frame, text="Cancel", command=lambda: self.cancel_edit(product, name_entry, price_entry, stock_entry, name_label, price_label, stock_label, edit_btn, save_btn, cancel_btn), font=("Poppins", 12))
        del_btn = tk.Button(frame, text="Delete", command=lambda: self.delete_product(product), font=("Poppins", 12))
=======
        # Buttons
        edit_btn = tk.Button(self.root, text="Edit", command=lambda: self.toggle_edit(
            product, name_entry, price_entry, stock_entry, 
            name_label, price_label, stock_label, edit_btn, save_btn, cancel_btn
        ), font=("Poppins", 12))
        
        save_btn = tk.Button(self.root, text="Save", command=lambda: self.save_changes(
            product, name_entry, price_entry, stock_entry, 
            name_label, price_label, stock_label, edit_btn, save_btn, cancel_btn
        ), font=("Poppins", 12))
        
        cancel_btn = tk.Button(self.root, text="Cancel", command=lambda: self.cancel_edit(
            product, name_entry, price_entry, stock_entry, 
            name_label, price_label, stock_label, edit_btn, save_btn, cancel_btn
        ), font=("Poppins", 12))

        
        del_btn = tk.Button(self.root, text="Delete", command=lambda: self.delete_product(product), font=("Poppins", 12))
>>>>>>> ca57288e821232d411fcc7927306cac513df58c8

        edit_btn.grid(row=row, column=3, padx=5)
        save_btn.grid(row=row, column=4, padx=5)
        cancel_btn.grid(row=row, column=5, padx=5)
        del_btn.grid(row=row, column=6, padx=5)

        save_btn.grid_remove()
        cancel_btn.grid_remove()

<<<<<<< HEAD
    def toggle_edit(self, product, name_entry, price_entry, stock_entry, name_label, price_label, stock_label, edit_btn, save_btn, cancel_btn):
        # Make name, price, and stock entries visible
        name_label.grid_remove()
        price_label.grid_remove()
        stock_label.grid_remove()

        name_entry.grid(row=name_label.grid_info()['row'], column=name_label.grid_info()['column'])
        price_entry.grid(row=price_label.grid_info()['row'], column=price_label.grid_info()['column'])
        stock_entry.grid(row=stock_label.grid_info()['row'], column=stock_label.grid_info()['column'])

        # Show save and cancel buttons, hide edit button
        edit_btn.grid_forget()
        save_btn.grid(row=name_entry.grid_info()['row'], column=name_entry.grid_info()['column'] + 1)
        cancel_btn.grid(row=name_entry.grid_info()['row'], column=name_entry.grid_info()['column'] + 2)

    def save_changes(self, product, name_entry, price_entry, stock_entry, name_label, price_label, stock_label, edit_btn, save_btn, cancel_btn):
        name = name_entry.get()
        price = price_entry.get()
        stock = stock_entry.get()

        if not name or not price or not stock:
            messagebox.showerror("Error", "Please fill in all fields!")
            return
        
        product["name"] = name
        product["price"] = price
        product["stock"] = stock
        
        save_products(self.products)
        
        name_label.config(text=name)
        price_label.config(text=f"PHP {price}")
        stock_label.config(text=stock)
        
        self.toggle_edit(product, name_entry, price_entry, stock_entry, name_label, price_label, stock_label, edit_btn, save_btn, cancel_btn)

    def cancel_edit(self, product, name_entry, price_entry, stock_entry, name_label, price_label, stock_label, edit_btn, save_btn, cancel_btn):
        name_entry.grid_remove()
        price_entry.grid_remove()
        stock_entry.grid_remove()
        save_btn.grid_remove()
        cancel_btn.grid_remove()
        
        name_label.config(text=product['name'])
        price_label.config(text=f"PHP {product['price']}")
        stock_label.config(text=str(product['stock']))
        
        edit_btn.grid()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def delete_product(self, product):
        self.products.remove(product)
        save_products(self.products)
        self.show_product_management()
=======
        # Store widgets
        self.product_widgets[product["name"]] = {
            "name_entry": name_entry,
            "price_entry": price_entry,
            "stock_entry": stock_entry,
            "name_label": name_label,
            "price_label": price_label,
            "stock_label": stock_label,
            "edit_button": edit_btn,
            "save_button": save_btn,
            "cancel_button": cancel_btn
        }

    def toggle_edit(self, product, name_entry, price_entry, stock_entry, 
                name_label, price_label, stock_label, edit_button, save_button, cancel_button):
        name_label.grid_remove()
        price_label.grid_remove()
        stock_label.grid_remove()

        name_entry.grid()
        price_entry.grid()
        stock_entry.grid()

        edit_button.grid_remove()
        save_button.grid()
        cancel_button.grid()


    def save_changes(self, product, name_entry, price_entry, stock_entry, 
                 name_label, price_label, stock_label, edit_button, save_button, cancel_button):
        try:
            new_name = name_entry.get().strip()
            new_price = float(price_entry.get())
            new_stock = int(stock_entry.get())

            if not new_name:
                raise ValueError("Product name cannot be empty.")

            # Update product details
            product["name"] = new_name
            product["price"] = new_price
            product["stock"] = new_stock
            save_products(self.products)

            # Update label text
            name_label.config(text=new_name)
            price_label.config(text=f"PHP {new_price:.2f}")
            stock_label.config(text=str(new_stock))

            # Hide entry fields
            name_entry.grid_remove()
            price_entry.grid_remove()
            stock_entry.grid_remove()
            save_button.grid_remove()
            cancel_button.grid_remove()

            # Show labels and edit button again
            name_label.grid()
            price_label.grid()
            stock_label.grid()
            edit_button.grid()

            messagebox.showinfo("Success", f"Updated {new_name} successfully!")

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid name, price, and stock quantity.")

    def cancel_edit(self, product, name_entry, price_entry, stock_entry, 
                name_label, price_label, stock_label, edit_button, save_button, cancel_button):
        name_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        stock_entry.delete(0, tk.END)

        name_entry.insert(0, product["name"])
        price_entry.insert(0, str(product["price"]))
        stock_entry.insert(0, str(product["stock"]))

        # Hide entry fields
        name_entry.grid_remove()
        price_entry.grid_remove()
        stock_entry.grid_remove()
        save_button.grid_remove()
        cancel_button.grid_remove()

        # Show labels again
        name_label.grid()
        price_label.grid()
        stock_label.grid()
        edit_button.grid()


    def add_product(self, row):
        new_product = {"name": "New Product", "price": 0.0, "stock": 0}
        self.products.append(new_product)

        # Entry fields for new product
        name_entry = tk.Entry(self.root, width=15, font=("Poppins", 12), highlightthickness=0, bd=0)
        price_entry = tk.Entry(self.root, width=15, font=("Poppins", 12), highlightthickness=0, bd=0)
        stock_entry = tk.Entry(self.root, width=15, font=("Poppins", 12), highlightthickness=0, bd=0)

        name_entry.insert(0, "New Product")
        price_entry.insert(0, "0.0")
        stock_entry.insert(0, "0")

        name_entry.grid(row=row, column=0, padx=10)
        price_entry.grid(row=row, column=1)
        stock_entry.grid(row=row, column=2)

        # Save and Cancel buttons
        save_btn = tk.Button(self.root, text="Save", command=lambda: self.save_new_product(name_entry, price_entry, stock_entry, save_btn, cancel_btn, row), font=("Poppins", 12))
        cancel_btn = tk.Button(self.root, text="Cancel", command=lambda: self.cancel_new_product(name_entry, price_entry, stock_entry, save_btn, cancel_btn), font=("Poppins", 12))

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
        self.products.pop()  # Remove the last added placeholder product
        name_entry.grid_remove()
        price_entry.grid_remove()
        stock_entry.grid_remove()
        save_btn.grid_remove()
        cancel_btn.grid_remove()

    def delete_product(self, product):
        confirm = messagebox.askyesno("Delete Product", f"Are you sure you want to delete {product['name']}?")
        if confirm:
            self.products.remove(product)
            save_products(self.products)
            self.show_product_management()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
>>>>>>> ca57288e821232d411fcc7927306cac513df58c8
