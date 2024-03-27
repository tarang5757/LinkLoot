import customtkinter as ctk
from main import JobScraper




class DashboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Link Loot')
        self.geometry('400x250')
        self.resizable(False, False)
        #self.iconphoto()
        self.iconbitmap('job.ico')




        #Layout
        self.grid_columnconfigure(1, weight=1)

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # job title
        ctk.CTkLabel(self, text="Job Title:").grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        self.job_title_entry = ctk.CTkEntry(self, placeholder_text="Please Enter Job Title")
        self.job_title_entry.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="ew")

        # job location
        ctk.CTkLabel(self, text="Location:").grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.location_entry = ctk.CTkEntry(self, placeholder_text="Please Enter The Location")
        self.location_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")



        #fileName
        ctk.CTkLabel(self, text="File Name:").grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.file_entry = ctk.CTkEntry(self, placeholder_text="Enter file Name To Save It to.")
        self.file_entry.grid(row=2, column=1, padx=20, pady=10, sticky="ew")


        # Login button
        search_button = ctk.CTkButton(self, text="search", fg_color="#9B2335",text_color="#FFFFFF", font=("Arial", 14), command=self.search,)
        search_button.grid(row=3, column=1, padx=20, pady=(0, 20), sticky="e")

        

        self.grid_rowconfigure(3, weight=1)  #this makes the rows above expand to fill space, pushing the label to the bottom
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        author_label = ctk.CTkLabel(self, text="Created By Tarang", font=("Roboto", 14, "bold"), text_color="#ffbf00")
        author_label.grid(row=3, column=0, columnspan=2, sticky="s")  

        
        author_label.grid(padx=20, pady=(0, 10))




    def search(self):
        # Placeholder for login action
        jobTitle = self.job_title_entry.get()
        jobLocation = self.location_entry.get()
        fileName = self.file_entry.get()
        #instance of object
        scraper = JobScraper(jobTitle, jobLocation)
        #call the run method
        scraper.run(fileName)

        #close gui after executing the instuction
        self.destroy()

       




if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()
