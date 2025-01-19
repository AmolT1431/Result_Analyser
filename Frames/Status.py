from tkinter import *
from App.Center import *
from App.Frames import *
from Frames.Buttons import*
from Frames.Option_Frame import*
from PIL import Image, ImageTk
 
class Status_Frame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white", width=200, height=200)
       
        # Load and resize the image
        image = Image.open(r'F:\C & C++\Result_Analyser\alert.png')
        image = image.resize((31, 30), Image.LANCZOS)
        icon = ImageTk.PhotoImage(image)
       
        # Create the first label
        self.label = tk.Label(self, text="PRN List Not Selected", bg="white",font=("Times New Roman", 12,"bold"),image=icon, compound='right', height=3, padx=10, pady=10)
        self.label.image = icon  # Keep a reference to avoid garbage collection
        self.label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
        
        # Create the second label
        self.label2 = tk.Label(self, text="Result Not Downloaded",  bg="white",font=("Times New Roman", 12,"bold"),image=icon, compound='right', height=3, padx=10, pady=10)
        self.label2.image = icon  # Keep a reference to avoid garbage collection
        self.label2.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        
        self.label3 = tk.Label(self, text="Data not processed",  bg="white",font=("Times New Roman", 12,"bold"),image=icon, compound='right', height=3, padx=10, pady=10)
        self.label3.image = icon  # Keep a reference to avoid garbage collection
        self.label3.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        
        
        # Pack the frame
        self.pack(side=tk.LEFT, fill="both", expand=True, pady=(10, 10), padx=(10, 10))
