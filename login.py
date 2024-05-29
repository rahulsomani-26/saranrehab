import customtkinter
import tkinter
from tkinter import messagebox
from PIL import Image
from sarandb import Database
from patientwindow import PatientWindow
from resource_1 import resource_path

class Login(customtkinter.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure_window()
        self.db = Database()

    def configure_window(self):
        customtkinter.set_appearance_mode("dark")
        self.geometry("500x500")
        self.title("Login to Saran")
        try:
            self.iconbitmap(resource_path(r'C:\Users\soman\prefinal_saran\icons\logo.ico'))
        except tkinter.TclError:
            pass
        self.resizable(False, False)
        self.create_window()

    def create_window(self):
        self.img = customtkinter.CTkImage(
            light_image=Image.open(resource_path(r'C:\Users\soman\prefinal_saran\icons\logo.png')),
            size=(200, 200)
        )
        self.img_label = customtkinter.CTkLabel(self, image=self.img, text=" ")
        self.img_label.pack()

        self.username_label = customtkinter.CTkLabel(
            self, text="Username", corner_radius=5, fg_color="#0C0C0C",
            text_color="#1573DF", font=("Arial", 12)
        )
        self.username_label.place(x=10, y=250)
        self.username_entry = customtkinter.CTkEntry(self, placeholder_text="Enter Username", width=200)
        self.username_entry.place(x=150, y=250)
        
        self.password_label = customtkinter.CTkLabel(
            self, text="Password", corner_radius=5, fg_color="#111010",
            text_color="#1573DF", font=("Arial", 12)
        )
        self.password_label.place(x=10, y=300)
        self.password_entry = customtkinter.CTkEntry(self, width=200, placeholder_text="Enter Password", show='*')
        self.password_entry.place(x=150, y=300)

        # Bind Enter key to move focus
        self.username_entry.bind('<Return>', lambda event: self.focus_next_widget(event, self.password_entry))
        self.password_entry.bind('<Return>', lambda event: self.focus_next_widget(event, self.submit_button))

        # Buttons
        self.submit_button = customtkinter.CTkButton(
            self, text="Login", width=200, corner_radius=6, border_width=1,
            border_color="blue", fg_color="#000", command=self.verify_user
        )
        self.submit_button.place(x=10, y=400)

        # Exit Button
        self.exit_button = customtkinter.CTkButton(
            self, text="Exit", width=200, corner_radius=6, border_width=1,
            border_color="blue", fg_color="#000", command=self.quit
        )
        self.exit_button.place(x=250, y=400)

    def focus_next_widget(self, event, next_widget):
        next_widget.focus_set()

    def verify_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if not username or not password:
            messagebox.showerror(title="Error", message="Username and Password cannot be empty.")
            return

        try:
            if self.db.verify_user(username=username, password=password):
                self.open_main_window()
            else:
                messagebox.showerror(title="Error", message="Invalid username or password.")
        except Exception as e:
            messagebox.showerror(title="Error", message=str(e))

    def open_main_window(self):
        print("Working")
        self.destroy()
        # p = PatientWindow()
        # p.mainloop()

    def show_signup(self):
        self.destroy()
        # s = Signup()
        # s.mainloop()

l = Login()
l.mainloop()
