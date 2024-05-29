import customtkinter
from PIL import Image
from sarandb import Database

class SearchPatient(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure_settings()
        self.db = Database()
        self.image_ref = None  # To hold reference to the image object
        self.file_path = None  # To hold the file path of the photo

    def configure_settings(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.create_window()

    def create_window(self):
        self.title("Search Patient")
        self.after(0, lambda: self.state('zoomed'))

        # Search Entry
        self.search_entry = customtkinter.CTkEntry(
            self, width=200, corner_radius=10, fg_color="#4895ef", text_color="#000", font=('Arial', 16)
        )
        self.search_entry.place(x=50, y=100)

        # Search Button
        self.search_button = customtkinter.CTkButton(
            self, corner_radius=10, fg_color="#7400b8", text="Search By Name", hover_color="#B29CBE", command=self.search_patient
        )
        self.search_button.place(x=300, y=100)

        # Placeholder for future search by registration
        self.search_frame = customtkinter.CTkButton(self, text="Search by Registration", fg_color="red", state="disabled")
        self.search_frame.place(x=500, y=100)

        # Frame to hold search results
        self.search_results_frame = customtkinter.CTkFrame(self, corner_radius=10, fg_color="#0B8BC7")
        self.search_results_frame.place(x=50, y=200, relwidth=0.9, relheight=0.6)

        # Canvas and scrollbar for search results
        self.search_results_canvas = customtkinter.CTkCanvas(self.search_results_frame, background="#0B8BC7")
        self.search_results_scrollbar = customtkinter.CTkScrollbar(self.search_results_frame, corner_radius=10, bg_color="red", fg_color="#031C27", command=self.search_results_canvas.yview)
        self.search_results_inner_frame = customtkinter.CTkFrame(self.search_results_canvas, width=1200, height=500, corner_radius=10, fg_color="#063D57")

        self.search_results_inner_frame.bind(
            "<Configure>",
            lambda e: self.search_results_canvas.configure(
                scrollregion=self.search_results_canvas.bbox("all")
            )
        )

        self.search_results_canvas.create_window((0, 0), window=self.search_results_inner_frame, anchor="nw")
        self.search_results_canvas.configure(yscrollcommand=self.search_results_scrollbar.set)

        self.search_results_canvas.pack(side="left", fill="both", expand=True)
        self.search_results_scrollbar.pack(side="right", fill="y")

    def search_patient(self):
        search_name = self.search_entry.get()
        patients = self.db.search_patient_by_name(search_name)
        
        for widget in self.search_results_inner_frame.winfo_children():
            widget.destroy()
        
        if patients:
            for patient in patients:
                result = patient[6]
                self.file_path = patient[10]
                
                patient_frame = customtkinter.CTkFrame(self.search_results_inner_frame, corner_radius=10, fg_color="#094664")
                patient_frame.pack(fill="x", padx=10, pady=15)
                patient_label = customtkinter.CTkLabel(
                    patient_frame, 
                    text=f"Registration Number: {patient[1]}\t Name: {patient[2]}, Address: {patient[3]}, "
                         f"Date of Joining: {patient[4]}, Addiction Type: {patient[5]}, Gender: {result}, "
                         f"Duration: {patient[7]}, Room Type: {patient[8]}, Monthly Charge: {patient[9]}"
                )
                patient_label.pack(fill="x", padx=10, pady=15)
                
                pic_button = customtkinter.CTkButton(patient_frame, text="See Photo", command=self.show_photo)
                pic_button.pack(pady=5)
        else:
            no_results_label = customtkinter.CTkLabel(self.search_results_inner_frame, text="No patients found with the given name.")
            no_results_label.pack(fill="x", pady=10)

    def show_photo(self):
        if self.file_path:
            win = customtkinter.CTkToplevel(self)
            win.geometry("200x200")
            win.title("Patient Photo")
            photo = customtkinter.CTkImage(light_image=Image.open(self.file_path), size=(200, 200))
            self.image_ref = photo  # Keep a reference to the image object
            pic_label = customtkinter.CTkLabel(win, image=photo, text="")
            pic_label.image = photo  # Keep a reference to avoid garbage collection
            pic_label.pack()

if __name__ == "__main__":
    s = SearchPatient()
    s.mainloop()
