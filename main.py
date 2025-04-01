# Import required modules
import tkinter as tk
from PIL import Image, ImageTk  # Import for PNG support
from customer import CustomerApp  # Import the CustomerApp module
from admin import AdminApp  # Import the AdminApp module
from auth import AdminLoginApp  # Import the login module

# MainApp class to handle the GUI structure
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blumee - Skincare Management System")  # Set the window title
        self.root.geometry("600x600")  # Set window size
        self.root.configure(bg="#FFC0CB")  # Set background color to baby pink

        self.show_main_menu()  # Display the main menu on startup

    # Method to clear any existing widgets from the window
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Method to display the main menu with logo and buttons
    def show_main_menu(self):
        self.clear_window()  # Clear the window before displaying the menu

        # Load and display the logo
        try:
            logo_image = Image.open('./img/blumeelogo1.png')  # Open the logo image file
            self.logo = ImageTk.PhotoImage(logo_image)  # Convert the image to a format suitable for tkinter
            logo_label = tk.Label(self.root, image=self.logo, bg="#FFC0CB")  # Create a label for the logo
            logo_label.pack(pady=20)  # Display the logo label with padding
        except Exception as e:
            print(f"Error loading logo: {e}")  # Print an error message if the logo fails to load

        # Add a welcome label below the logo
        welcome_label = tk.Label(self.root, text="Welcome to Blumee!", font=("Poppins", 20, "bold"), bg="#FFC0CB", fg="#FF69B4")
        welcome_label.pack(pady=10)  # Display the welcome label with padding

        # Button styling dictionary to apply to buttons
        button_style = {"font": ("Poppins", 12), "width": 20, "height": 2, "bg": "#FFFFFF", "fg": "#FF69B4", "bd": 3}

        # Create and pack buttons for customer, admin, and exit options
        tk.Button(self.root, text="Customer", command=self.show_customer, **button_style).pack(pady=10)  # Button for Customer
        tk.Button(self.root, text="Admin", command=self.show_admin, **button_style).pack(pady=10)  # Button for Admin
        tk.Button(self.root, text="Exit", command=self.root.quit, **button_style).pack(pady=10)  # Button to quit the app

    # Method to display the customer section
    def show_customer(self):
        self.clear_window()  # Clear the window before displaying customer section
        CustomerApp(self.root, self.show_main_menu)  # Initialize and show the CustomerApp

    def show_admin(self):
        self.clear_window()  
        # Display the admin login screen first
        AdminLoginApp(self.root, self.show_admin_panel, self.show_main_menu)

    # Method to display the admin section
    def show_admin_panel(self):
        self.clear_window()  # Clear the window before displaying admin section
        AdminApp(self.root, self.show_main_menu)  # Initialize and show the AdminApp

# Run the application if this file is executed directly
if __name__ == "__main__":
    root = tk.Tk()  # Create the main tkinter window
    app = MainApp(root)  # Initialize the MainApp with the root window
    root.mainloop()  # Start the tkinter event loop to keep the window open
