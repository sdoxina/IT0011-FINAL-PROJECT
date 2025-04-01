import tkinter as tk
from tkinter import messagebox

# Function to check admin credentials
def validate_admin(username, password):
    # Replace with real validation logic
    valid_username = "admin"  # Hardcoded valid username
    valid_password = "admin123"  # Hardcoded valid password
    
    # Check if the entered username and password match the valid ones
    if username == valid_username and password == valid_password:
        return True  # Return True if credentials are correct
    return False  # Return False if credentials are incorrect

# AdminLoginApp to handle login
class AdminLoginApp:
    def __init__(self, root, on_success_callback, back_callback):
        self.root = root  # Tkinter root window
        self.on_success_callback = on_success_callback  # Callback to proceed to AdminApp on success
        self.back_callback = back_callback  # Callback for the back button
        
        self.root.title("Admin Login")  # Set the window title
        self.root.geometry("400x400")  # Set the window size
        self.root.configure(bg="#FFC0CB")  # Set background color of the window
        
        self.show_login_form()  # Display the login form when the app is initialized
    
    def show_login_form(self):
        # Clear the window by destroying any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Title label for the login form
        tk.Label(self.root, text="Admin Login", font=("Poppins", 16, "bold"), bg="#FFC0CB").pack(pady=20)

        # Username entry field with label
        tk.Label(self.root, text="Username", font=("Poppins", 12), bg="#FFC0CB").pack(pady=5)
        self.username_entry = tk.Entry(self.root, font=("Poppins", 12))  # Entry widget for username
        self.username_entry.pack(pady=5)

        # Password entry field with label
        tk.Label(self.root, text="Password", font=("Poppins", 12), bg="#FFC0CB").pack(pady=5)
        self.password_entry = tk.Entry(self.root, font=("Poppins", 12), show="*")  # Entry widget for password (hidden input)
        self.password_entry.pack(pady=5)

        # Login button that triggers the login function when clicked
        login_button = tk.Button(self.root, text="Login", font=("Poppins", 12), command=self.login, bg="#FFFFFF", fg="#FF69B4")
        login_button.pack(pady=20)

        # Back button that calls the back callback when clicked
        back_button = tk.Button(self.root, text="Back", font=("Poppins", 12), command=self.back_callback, bg="#f44336", fg="white")
        back_button.pack(pady=10)  # Adds padding between buttons

    def login(self):
        # Get username and password input from the user
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the entered credentials are valid
        if validate_admin(username, password):
            self.on_success_callback()  # Call the success callback if credentials are correct
        else:
            # Show error message if credentials are incorrect
            messagebox.showerror("Login Failed", "Invalid username or password.")
