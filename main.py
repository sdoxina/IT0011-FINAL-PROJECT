import tkinter as tk
from PIL import Image, ImageTk  # Import for PNG support
from customer import CustomerApp
from admin import AdminApp

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blumee - Skincare Management System")
        self.root.geometry("600x600")
        self.root.configure(bg="#FFC0CB")  # Baby pink background

        self.show_main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_window()

        # Load and display the logo
        try:
            logo_image = Image.open('./img/blumeelogo1.png')
            self.logo = ImageTk.PhotoImage(logo_image)  # Keep a reference (avoid garbage collection)
            logo_label = tk.Label(self.root, image=self.logo, bg="#FFC0CB")
            logo_label.pack(pady=20)
        except Exception as e:
            print(f"Error loading logo: {e}")  # Debugging in case of errors

        # Add a welcome label below the logo
        welcome_label = tk.Label(self.root, text="Welcome to Blumee!", font=("Poppins", 20, "bold"), bg="#FFC0CB", fg="#FF69B4")
        welcome_label.pack(pady=10)

        # Button styling
        button_style = {"font": ("Poppins", 12), "width": 20, "height": 2, "bg": "#FFFFFF", "fg": "#FF69B4", "bd": 3}

        tk.Button(self.root, text="Customer", command=self.show_customer, **button_style).pack(pady=10)
        tk.Button(self.root, text="Admin", command=self.show_admin, **button_style).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, **button_style).pack(pady=10)

    def show_customer(self):
        self.clear_window()
        CustomerApp(self.root, self.show_main_menu)

    def show_admin(self):
        self.clear_window()
        AdminApp(self.root, self.show_main_menu)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
