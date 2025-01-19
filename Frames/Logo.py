from tkinter import *
from Frames.Fail import *
from Frames.Pass import *
from PIL import Image, ImageTk

class Logo_Frame(Frame):
    def __init__(self, parent):
        super().__init__(parent,bg="white",width=270,height=200)
        
        image = Image.open(r'F:\C & C++\Result_Analyser\Logo.jpg')
        image = image.resize((220, 200), Image.LANCZOS)
        photo= ImageTk.PhotoImage(image)
        
        label = Label(self, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.pack()
        self.pack(side=TOP,fill="x",padx=(15,15),pady=10)