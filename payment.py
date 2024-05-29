import qrcode
import customtkinter
from tkinter import messagebox
from PIL import Image, ImageTk
from resource_1 import resource_path

class PaymentGateway(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        customtkinter.set_appearance_mode("dark")
        self.configure_window()
        self.phonepay_url = ""
        self.qr_photo = None

    def configure_window(self):
        self.geometry("800x600")
        self.title("Payment")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        self.upi_id_label = customtkinter.CTkLabel(self, text="Enter UPI ID", corner_radius=5, fg_color="blue")
        self.upi_id_label.grid(row=0, column=0, padx=20, pady=20, sticky="e")

        self.upi_id_entry = customtkinter.CTkEntry(self, placeholder_text="Enter Your UPI ID", width=200, corner_radius=5, font=('Arial', 16))
        self.upi_id_entry.grid(row=0, column=1, padx=20, pady=20, sticky="w")

        self.amount_label = customtkinter.CTkLabel(self, text="Amount", corner_radius=5, fg_color="blue",width=100)
        self.amount_label.place(x=270,y=100)

        self.amount_entry = customtkinter.CTkEntry(self, placeholder_text="Enter Amount", width=250, corner_radius=5, font=('Arial', 16))
        self.amount_entry.place()


        # Pay Button
        self.submit_btn = customtkinter.CTkButton(self, text="Pay", corner_radius=6, fg_color="#1E56D8", font=('Arial', 16), command=self.pay)
        self.submit_btn.grid(row=1, column=0, padx=20, pady=20, sticky="e")

        # Cancel Button
        self.cancel_btn = customtkinter.CTkButton(self, text="Cancel", corner_radius=6, fg_color="#1E56D8", font=('Arial', 16), command=self.quit)
        self.cancel_btn.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # QR Code canvas
        self.qrcode_canvas = customtkinter.CTkCanvas(self, width=400, height=400, background='#202021')
        self.qrcode_canvas.grid(row=2, column=0, columnspan=2, padx=50, pady=20, sticky="nesw")

    def pay(self):
        self.phonepay_url = f'upi://pay?pa={self.upi_id_entry.get()}&pn=Recipient%20Name'
        self.create_qr_code()

    def create_qr_code(self):
        qr_image = qrcode.make(self.phonepay_url)
        self.qr_photo = ImageTk.PhotoImage(qr_image)
        self.qrcode_canvas.create_image(200, 200, image=self.qr_photo)
        self.qrcode_canvas.image = self.qr_photo


if __name__ == "__main__":
    p = PaymentGateway()
    p.mainloop()
