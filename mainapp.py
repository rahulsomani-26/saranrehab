import customtkinter
import tkinter 
from tkinter import messagebox
from PIL import Image
from login import Login
from sarandb import Database
from resource_1 import resource_path




class Signup(customtkinter.CTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.db = Database()

        self.username = customtkinter.StringVar()
        self.password = customtkinter.StringVar()
        self.repeat_password = customtkinter.StringVar()


        self.title("Signup")
        try:
            self.iconbitmap(resource_path(r'C:\Users\soman\prefinal_saran\icons\logo.ico'))
        except tkinter.TclError:
            pass
        self.resizable(False,False)

        # Saran Image to be displayed on Top Centre

        self.img = customtkinter.CTkImage(light_image=Image.open(resource_path(r'C:\Users\soman\prefinal_saran\icons\logo.png')),size=(200,200))
        self.img_label = customtkinter.CTkLabel(self,image=self.img,text=" ")
        self.img_label.pack()

        self.username_label = customtkinter.CTkLabel(self,text="Username",corner_radius=5,fg_color="#0C0C0C",text_color="#1573DF",font=("Arial",12))
        self.username_label.place(x=10,y=250)
        self.username_entry = customtkinter.CTkEntry(self,placeholder_text="Enter Username",width=200)
        self.username_entry.place(x=150,y=250)

        self.password_label = customtkinter.CTkLabel(self,text="Password",corner_radius=5,fg_color="#111010",text_color="#1573DF",font=("Arial",12) )
        self.password_label.place(x=10,y=300)

        self.password_entry = customtkinter.CTkEntry(self,placeholder_text="Enter Password",width=200,show='*')
        self.password_entry.place(x=150,y=300)

        self.showpassword_img = customtkinter.CTkImage(light_image=Image.open(resource_path(r'C:\Users\soman\prefinal_saran\icons\closedeye.png')))
        self.show_password_button =customtkinter.CTkButton(self,image=self.showpassword_img,text="",fg_color="black",width=50,command=self.toggle_password_visibility )
        self.show_password_button.place(x=400,y=300)

        self.repeat_password = customtkinter.CTkLabel(self,text="Repeat Password",corner_radius=5,fg_color="#111010",text_color="#1573DF",font=("Arial",12))
        self.repeat_password.place(x=10,y=350)
    
        self.repeat_password_entry = customtkinter.CTkEntry(self,placeholder_text="Repeat Password",width=200,show='*')
        self.repeat_password_entry.place(x=150,y=350)

        # Submit Button 

        self.submit_button = customtkinter.CTkButton(self,text="SignUP",width=200,corner_radius=6,border_width=1,border_color="blue",fg_color="#000",command=self.store_entry)
        self.submit_button.place(x=10,y=450)


        # Exit Button 

        self.exit_button = customtkinter.CTkButton(self,text="Exit",width=200,corner_radius=6,border_width=1,border_color="blue",fg_color="#000",command=self.quit)
        self.exit_button.place(x=250,y=450)

        self.password_visible = False

        # Already a Member

        self.already_member_label = customtkinter.CTkLabel(self,text="Already a Member ! Login",fg_color="#4873E7",text_color="#000000",font=('Arial',16),corner_radius=10)
        self.already_member_label.place(x=150,y=550)
        self.already_member_label.bind(sequence='<Button-1>',command=self.show_login)

    def store_entry(self):
            # Get Data 
        username = self.username_entry.get()
        password = self.password_entry.get()
        repeat_password = self.repeat_password_entry.get()
        messagebox.askyesno(title="Store Data",message="About to store your data")
        # db = Database() 
        try:
            if password == repeat_password:
                # db.verify_user(username=username,password=password)
                self.db.store_user(username=username,password=password)
            else:
                messagebox.showinfo(title="Password Mismatch",message="Password Does Not Match")
                self.password_entry.configure(bg_color='red')
                self.password_entry.delete(0,customtkinter.END)
                self.repeat_password_entry.delete(0,customtkinter.END)
                self.password_entry.focus()
        except Exception as e:
            messagebox.showerror(title="Error",message=str(e))

    def show_password(self):
        pass 

    def show_login(self,event):
         self.destroy()
         l =Login()
         l.mainloop() 


    def toggle_password_visibility(self):
        # Toggle password visibility
        self.password_visible = not self.password_visible
        show_char = '' if self.password_visible else '*'
        self.password_entry.configure(show=show_char)
        self.repeat_password_entry.configure(show=show_char)
        # self.showpassword_img.configure(light_image=Image.open(r'images/icons/openeye.png'))
        try:
            self.showpassword_img = customtkinter.CTkImage(light_image=Image.open(resource_path(r'C:\Users\soman\prefinal_saran\icons\openeye.png ')))
            self.show_password_button.configure(require_redraw=True,image=self.showpassword_img)
            self.password_visible = not self.password_visible
            # messagebox.askyesno(title="Password",message="Password is visible now")
        except Exception as e:
            messagebox.askyesnocancel(title="Error",message=str(e))

if __name__ == '__main__':
    s = Signup()
    s.geometry("500x600+400+50")
    s.mainloop()

