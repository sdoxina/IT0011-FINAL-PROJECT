import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
from data_handler import load_products, save_orders
from receipt_generator import generate_receipt
import random
import string

# CustomerApp class to manage the customer's shopping experience
class CustomerApp:
    def __init__(self, root, back_callback):
        self.root = root  # Tkinter root window
        self.root.geometry("850x800")  # Set window size for the app
        self.back_callback = lambda: self.go_back(back_callback)  # Back button callback
        
        self.clear_window()  # Clears any existing content in the window

        # Scrollable Frame Setup
        self.canvas = tk.Canvas(root, bg="#FFC0CB")  # Canvas for scrollable area
        self.scroll_frame = tk.Frame(self.canvas, bg="#FFC0CB")  # Frame to hold the products
        self.scrollbar = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)  # Scrollbar for the canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")  # Pack the scrollbar to the right
        self.canvas.pack(side="left", fill="both", expand=True)  # Pack the canvas to the left
        self.canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")  # Create window inside canvas

        self.scroll_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))  # Update scroll region

        # Set font styles
        self.poppins_font = ("Poppins", 12)
        self.poppins_bold = ("Poppins", 14, "bold")

        # Title Label for the product listing page
        title_label = tk.Label(self.scroll_frame, text="Available Skincare Products", font=("Poppins", 18, "bold"), fg="#4CAF50", bg="#FFC0CB")
        title_label.grid(row=0, column=1, pady=10, sticky="nsew")

        # Headers for the product list
        tk.Label(self.scroll_frame, text="Product", font=self.poppins_bold, bg="#FFC0CB").grid(row=1, column=0, padx=10, sticky="w")
        tk.Label(self.scroll_frame, text="Image", font=self.poppins_bold, bg="#FFC0CB").grid(row=1, column=1, padx=10, sticky="w")
        tk.Label(self.scroll_frame, text="Price", font=self.poppins_bold, bg="#FFC0CB").grid(row=1, column=2, padx=10, sticky="w")
        tk.Label(self.scroll_frame, text="Quantity", font=self.poppins_bold, bg="#FFC0CB").grid(row=1, column=3, padx=10, sticky="w")

        self.products = load_products()  # Load products from data handler
        self.images = {}  # Dictionary to store product images
        self.cart = {}  # Cart dictionary to hold the selected items
        self.checkbuttons = {}  # Checkbuttons for selecting products
        self.quantities = {}  # Dictionary to track quantities for each product

        row_count = 2
        for product in self.products:
            name, price, stock, image_path = product["name"], product["price"], product["stock"], product["image"]
            var = tk.IntVar(value=0)  # Variable to track if the product is selected
            self.checkbuttons[name] = var

            check = tk.Checkbutton(self.scroll_frame, text=name, variable=var, font=self.poppins_font, bg="#FFC0CB", command=lambda p=name: self.toggle_quantity(p))
            check.grid(row=row_count, column=0, padx=10, sticky="w")

            # Price label for each product
            price_label = tk.Label(self.scroll_frame, text=f"PHP {price}", font=self.poppins_font, bg="#FFC0CB")
            price_label.grid(row=row_count, column=2)

            # Quantity label for each product
            qty_label = tk.Label(self.scroll_frame, text="0", font=self.poppins_font, bg="#FFC0CB")
            qty_label.grid(row=row_count, column=3)

            # Minus and Plus buttons to adjust quantity
            minus_button = tk.Button(self.scroll_frame, text="-", font=self.poppins_font, state="disabled", command=lambda p=name, l=qty_label: self.adjust_quantity(p, l, -1))
            minus_button.grid(row=row_count, column=4)

            plus_button = tk.Button(self.scroll_frame, text="+", font=self.poppins_font, state="disabled", command=lambda p=name, l=qty_label: self.adjust_quantity(p, l, 1))
            plus_button.grid(row=row_count, column=5)

            # Store quantity controls
            self.quantities[name] = {"label": qty_label, "minus": minus_button, "plus": plus_button}

            # Try loading the product image
            try:
                image_path = product.get("image", "images/no_image.png")  # Default image if missing
                img = Image.open(image_path)  # Open image
                img = img.resize((80, 80), Image.LANCZOS)  # Resize image
                tk_img = ImageTk.PhotoImage(img)  # Convert to Tkinter-compatible format
                self.images[name] = tk_img  # Store the image to prevent garbage collection

                img_label = tk.Label(self.scroll_frame, image=tk_img, bg="#FFC0CB")  # Create image label
                img_label.grid(row=row_count, column=1, padx=10)

            except Exception as e:
                print(f"Error loading image {image_path}: {e}")  # Print error if image loading fails
                img_label = tk.Label(self.scroll_frame, text="No Image", font=self.poppins_font, bg="#FFC0CB")  # Fallback label
                img_label.grid(row=row_count, column=1, padx=10)

            row_count += 1

        # Button frame to center the Checkout and Back buttons
        button_frame = tk.Frame(self.scroll_frame, bg="#FFC0CB")
        button_frame.grid(row=row_count, column=1, columnspan=3, pady=10, sticky="nsew")

        # Configure columns for proper spacing
        button_frame.grid_columnconfigure(0, weight=1)  # Left side (Back button)
        button_frame.grid_columnconfigure(1, weight=2)  # Spacer in the center
        button_frame.grid_columnconfigure(2, weight=1)  # Right side (Checkout button)

        # Back Button (Left)
        back_button = tk.Button(button_frame, text="Back", font=self.poppins_font, bg="#f44336", fg="white", command=self.back_callback)
        back_button.grid(row=0, column=0, padx=20, sticky="ew")

        # Checkout Button (Right)
        checkout_button = tk.Button(button_frame, text="Checkout", font=self.poppins_font, bg="#4CAF50", fg="white", command=self.checkout)
        checkout_button.grid(row=0, column=2, padx=20, sticky="ew")

    # Toggle quantity for the selected product
    def toggle_quantity(self, product):
        if self.checkbuttons[product].get():
            self.quantities[product]["label"].config(text="1")  # Set initial quantity to 1
            self.quantities[product]["minus"].config(state="normal")  # Enable minus button
            self.quantities[product]["plus"].config(state="normal")  # Enable plus button
        else:
            self.quantities[product]["label"].config(text="0")  # Reset quantity to 0
            self.quantities[product]["minus"].config(state="disabled")  # Disable minus button
            self.quantities[product]["plus"].config(state="disabled")  # Disable plus button

    # Adjust product quantity (either increment or decrement)
    def adjust_quantity(self, product, label, change):
        current = int(label.cget("text"))  # Get the current quantity from the label
        new_qty = max(1, current + change)  # Ensure quantity doesn't go below 1
        label.config(text=str(new_qty))  # Update the quantity label

    # Handle the checkout process
    def checkout(self):
        selected_items = {p: int(self.quantities[p]["label"].cget("text")) for p in self.checkbuttons if self.checkbuttons[p].get()}  # Collect selected items
        if not selected_items:  # If no items are selected, show warning
            messagebox.showwarning("Cart", "No items selected!")
            return
        name = simpledialog.askstring("Name", "Enter your name:")  # Ask for customer name
        if not name:  # If no name is provided, show error
            messagebox.showerror("Error", "Name is required!")
            return

        order_details = {}
        for p, qty in selected_items.items():  # Loop through selected products and create order details
            for product in self.products:
                if product["name"] == p:
                    order_details[p] = {"qty": qty, "price": product["price"]}
                    break

        save_orders(name, selected_items)  # Save the order to data
        receipt_no = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))  # Generate random receipt number
        receipt_file = generate_receipt(name, order_details, receipt_no)  # Generate receipt
        messagebox.showinfo("Order", f"Order placed successfully! Receipt saved as {receipt_file}")  # Show success message

    # Navigate back to the previous screen
    def go_back(self, back_callback):
        self.clear_window()  # Clear the current window
        back_callback()  # Call the back callback function

    # Clear the window of all widgets
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()  # Destroy each widget in the root window
