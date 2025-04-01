import tkinter as tk
from tkinter import messagebox

# Function to check admin credentials
def validate_admin(username, password):
    # Replace with real validation logic
    valid_username = "admin"
    valid_password = "admin123"
    
    if username == valid_username and password == valid_password:
        return True
    return False

# AdminLoginApp to handle login
class AdminLoginApp:
    def __init__(self, root, on_success_callback, back_callback):
        self.root = root
        self.on_success_callback = on_success_callback  # Callback to proceed to AdminApp
        self.back_callback = back_callback  # Callback for the back button
        
        self.root.title("Admin Login")
        self.root.geometry("400x400")
        self.root.configure(bg="#FFC0CB")
        
        self.show_login_form()
    
    def show_login_form(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title label
        tk.Label(self.root, text="Admin Login", font=("Poppins", 16, "bold"), bg="#FFC0CB").pack(pady=20)

        # Username entry
        tk.Label(self.root, text="Username", font=("Poppins", 12), bg="#FFC0CB").pack(pady=5)
        self.username_entry = tk.Entry(self.root, font=("Poppins", 12))
        self.username_entry.pack(pady=5)

        # Password entry
        tk.Label(self.root, text="Password", font=("Poppins", 12), bg="#FFC0CB").pack(pady=5)
        self.password_entry = tk.Entry(self.root, font=("Poppins", 12), show="*")
        self.password_entry.pack(pady=5)

        # Login button
        login_button = tk.Button(self.root, text="Login", font=("Poppins", 12), command=self.login, bg="#FFFFFF", fg="#FF69B4")
        login_button.pack(pady=20)

        # Back button
        back_button = tk.Button(self.root, text="Back", font=("Poppins", 12), command=self.back_callback, bg="#f44336", fg="white")
        back_button.pack(pady=10)  # Adds a padding between buttons

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if validate_admin(username, password):
            self.on_success_callback()  # Proceed to AdminApp if login is successful
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
