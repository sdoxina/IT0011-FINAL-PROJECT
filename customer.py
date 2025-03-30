import tkinter as tk
from tkinter import messagebox, simpledialog
from data_handler import load_products, save_orders

class CustomerApp:
    def __init__(self, root, back_callback):
        self.root = root
        self.back_callback = lambda: self.go_back(back_callback)

        self.clear_window()

        tk.Label(root, text="Available Skincare Products", font=("Arial", 14)).grid(row=0, column=1, pady=10)

        # Add table headers
        tk.Label(root, text="Product", font=("Arial", 12, "bold")).grid(row=1, column=0, padx=10)
        tk.Label(root, text="Price", font=("Arial", 12, "bold")).grid(row=1, column=1, padx=10)
        tk.Label(root, text="Quantity", font=("Arial", 12, "bold")).grid(row=1, column=2, padx=10)

        self.products = load_products()
        self.cart = {}
        self.checkbuttons = {}
        self.quantities = {}

        row_count = 2
        for product in self.products:
            name, price, stock = product["name"], product["price"], product["stock"]
            var = tk.IntVar(value=0)
            self.checkbuttons[name] = var

            # Checkbox for product selection
            check = tk.Checkbutton(root, text=name, variable=var, command=lambda p=name: self.toggle_quantity(p))
            check.grid(row=row_count, column=0, padx=10, sticky="w")

            # Label for price
            price_label = tk.Label(root, text=f"PHP {price}")
            price_label.grid(row=row_count, column=1)

            # Label for quantity
            qty_label = tk.Label(root, text="0")  # Default quantity is 0
            qty_label.grid(row=row_count, column=2)

            # Minus (-) and Plus (+) buttons
            minus_button = tk.Button(root, text="-", state="disabled", command=lambda p=name, l=qty_label: self.adjust_quantity(p, l, -1))
            minus_button.grid(row=row_count, column=3)

            plus_button = tk.Button(root, text="+", state="disabled", command=lambda p=name, l=qty_label: self.adjust_quantity(p, l, 1))
            plus_button.grid(row=row_count, column=4)

            self.quantities[name] = {"label": qty_label, "minus": minus_button, "plus": plus_button}

            row_count += 1


        # Checkout & Back Buttons
        tk.Button(root, text="Checkout", command=self.checkout).grid(row=row_count, column=1, pady=10)
        tk.Button(root, text="Back", command=self.back_callback).grid(row=row_count + 1, column=1, pady=10)

    def toggle_quantity(self, product):
        """Enable/disable quantity and buttons when checkbox is toggled."""
        if self.checkbuttons[product].get():
            self.quantities[product]["label"].config(text="1")  # Set quantity to 1
            self.quantities[product]["minus"].config(state="normal")  # Enable buttons
            self.quantities[product]["plus"].config(state="normal")
        else:
            self.quantities[product]["label"].config(text="0")  # Reset to 0
            self.quantities[product]["minus"].config(state="disabled")  # Disable buttons
            self.quantities[product]["plus"].config(state="disabled")

    def adjust_quantity(self, product, label, change):
        """Increase or decrease quantity, ensuring it never goes below 1 when selected."""
        current = int(label.cget("text"))
        new_qty = max(1, current + change)  # Minimum quantity is 1 if selected
        label.config(text=str(new_qty))

    def checkout(self):
        selected_items = {p: int(self.quantities[p]["label"].cget("text")) for p in self.checkbuttons if self.checkbuttons[p].get()}
        
        if not selected_items:
            messagebox.showwarning("Cart", "No items selected!")
            return
        
        name = simpledialog.askstring("Name", "Enter your name:")
        if not name:
            messagebox.showerror("Error", "Name is required!")
            return

        save_orders(name, selected_items)
        messagebox.showinfo("Order", "Order placed successfully!")

    def go_back(self, back_callback):
        self.clear_window()
        back_callback()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
