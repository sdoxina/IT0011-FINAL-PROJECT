import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
from data_handler import load_products, save_orders
from receipt_generator import generate_receipt
import random
import string

class CustomerApp:
    def __init__(self, root, back_callback):
        self.root = root
        self.root.geometry("730x770")  # Set window size wider
        self.back_callback = lambda: self.go_back(back_callback)

        self.clear_window()

        # Set font
        self.poppins_font = ("Poppins", 12)
        self.poppins_bold = ("Poppins", 14, "bold")
        
        # Title Label
        tk.Label(root, text="Available Skincare Products", font=("Poppins", 18, "bold"), fg="#4CAF50", bg="#FFC0CB").grid(row=0, column=1, pady=10)

        # Headers
        tk.Label(root, text="Product", font=self.poppins_bold, bg="#FFC0CB").grid(row=1, column=0, padx=10)
        tk.Label(root, text="Image", font=self.poppins_bold, bg="#FFC0CB").grid(row=1, column=1, padx=10)
        tk.Label(root, text="Price", font=self.poppins_bold, bg="#FFC0CB").grid(row=1, column=2, padx=10)
        tk.Label(root, text="Quantity", font=self.poppins_bold, bg="#FFC0CB").grid(row=1, column=3, padx=10)

        self.products = load_products()
        self.images = {}
        self.cart = {}
        self.checkbuttons = {}
        self.quantities = {}

        row_count = 2
        for product in self.products:
            name, price, stock, image_path = product["name"], product["price"], product["stock"], product["image"]
            var = tk.IntVar(value=0)
            self.checkbuttons[name] = var

            check = tk.Checkbutton(root, text=name, variable=var, font=self.poppins_font, bg="#FFC0CB", command=lambda p=name: self.toggle_quantity(p))
            check.grid(row=row_count, column=0, padx=10, sticky="w")

            price_label = tk.Label(root, text=f"PHP {price}", font=self.poppins_font, bg="#FFC0CB")
            price_label.grid(row=row_count, column=2)

            qty_label = tk.Label(root, text="0", font=self.poppins_font, bg="#FFC0CB")
            qty_label.grid(row=row_count, column=3)

            minus_button = tk.Button(root, text="-", font=self.poppins_font, state="disabled", command=lambda p=name, l=qty_label: self.adjust_quantity(p, l, -1))
            minus_button.grid(row=row_count, column=4)

            plus_button = tk.Button(root, text="+", font=self.poppins_font, state="disabled", command=lambda p=name, l=qty_label: self.adjust_quantity(p, l, 1))
            plus_button.grid(row=row_count, column=5)

            self.quantities[name] = {"label": qty_label, "minus": minus_button, "plus": plus_button}

            try:
                image_path = product.get("image", "images/no_image.png")  # Use default if missing
                img = Image.open(image_path)
                img = img.resize((80, 80), Image.LANCZOS)
                tk_img = ImageTk.PhotoImage(img)
                self.images[name] = tk_img  # Prevent garbage collection

                img_label = tk.Label(root, image=tk_img, bg="#FFC0CB")
                img_label.grid(row=row_count, column=1, padx=10)

            except Exception as e:
                print(f"Error loading image {image_path}: {e}")
                img_label = tk.Label(root, text="No Image", font=self.poppins_font, bg="#FFC0CB")
                img_label.grid(row=row_count, column=1, padx=10)


            row_count += 1

        # Buttons
        tk.Button(root, text="Checkout", font=self.poppins_font, bg="#4CAF50", fg="white", command=self.checkout).grid(row=row_count, column=1, pady=10)
        tk.Button(root, text="Back", font=self.poppins_font, bg="#f44336", fg="white", command=self.back_callback).grid(row=row_count + 1, column=1, pady=10)

    def toggle_quantity(self, product):
        if self.checkbuttons[product].get():
            self.quantities[product]["label"].config(text="1")
            self.quantities[product]["minus"].config(state="normal")
            self.quantities[product]["plus"].config(state="normal")
        else:
            self.quantities[product]["label"].config(text="0")
            self.quantities[product]["minus"].config(state="disabled")
            self.quantities[product]["plus"].config(state="disabled")

    def adjust_quantity(self, product, label, change):
        current = int(label.cget("text"))
        new_qty = max(1, current + change)
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

        order_details = {}
        for p, qty in selected_items.items():
            for product in self.products:
                if product["name"] == p:
                    order_details[p] = {"qty": qty, "price": product["price"]}
                    break

        save_orders(name, selected_items)
        
        receipt_no = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        receipt_file = generate_receipt(name, order_details, receipt_no)
        messagebox.showinfo("Order", f"Order placed successfully! Receipt saved as {receipt_file}")

    def go_back(self, back_callback):
        self.clear_window()
        back_callback()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
