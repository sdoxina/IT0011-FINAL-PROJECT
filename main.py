import tkinter as tk
from PIL import Image, ImageTk  # Import for PNG support
from customer import CustomerApp
from admin import AdminApp

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blumee - Skincare Management System")
        self.root.geometry("400x400")
        self.root.configure(bg="#FFC0CB")  # Baby pink background

        self.show_main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_window()

        # Load and display the logo
        # try:
        #     logo_image = Image.open('soulspeakFavicon.png')
        #     print(logo_image.format)
        #     print(logo_image.size)
        #     print(logo_image.mode)
        #     logo_image.show()  # Ensure the file is in the same directory
        #     # logo_image = logo_image.resize((200, 100), Image.LANCZOS)  # Resize if needed
        #     # self.logo = ImageTk.PhotoImage(logo_image)  # Keep a reference (avoid garbage collection)
            
        #     logo_label = tk.Label(self.root, image=self.logo, bg="#FFC0CB")
        #     logo_label.pack(pady=20)
        # except Exception as e:
        #     print(f"Error loading logo: {e}")  # Debugging in case of errors

        try:  # Ensure 'pet' dictionary is properly defined
                pil_image = Image.open('soulspeakFavicon.png').resize((100, 100), Image.LANCZOS)
                image = ImageTk.PhotoImage(pil_image)
                logo_label = tk.Label(image=image, bg="#FFFFFF")
                logo_label.image = image  # Keep a reference
                logo_label.pack()
        except Exception as e:
            print(f"Error loading image: {e}")
            error_label = tk.Label(text="Error Displaying Image", font=("Century Gothic", 10), bg="#FFFFFF", fg="#2B2C41")
            error_label.pack()

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
