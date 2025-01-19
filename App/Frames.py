import tkinter as tk
from Frames.Staticstics import *
from Frames.Find_Result import *
from Frames.List_Prn import *
from Frames.Pass_Fail import *
from Frames.Top5_List import *

from tkinter import ttk

class Display_Frames:
    def __init__(self, display_content_frame):
        self.frame1 = tk.Frame(display_content_frame)
        List_Prn(self.frame1)
        self.frame1.grid(row=0, column=0, sticky="nsew")
        
        

        self.frame2 = Statictisc(display_content_frame)
        self.frame2.grid(row=0, column=0, sticky="nsew")
        
        
        self.frame3 = Frame_Find_Result(display_content_frame)
        self.frame3.grid(row=0, column=0, sticky="nsew")
        
        
        self.frame4 = Pass_Fail(display_content_frame)
       
        
        
        self.frame5 = tk.Frame(display_content_frame, bg="white")
        label5 = tk.Label(self.frame5, text="Thank You from Atomic Tos",bg='white',font=("Times New Roman", 20,"bold"))
        label5.pack(padx=20, pady=20)
        self.frame5.grid(row=0, column=0, sticky="nsew")
        
        
        self.frame6 = Top5_List(display_content_frame)
       
        

        display_content_frame.grid_rowconfigure(0, weight=1)
        display_content_frame.grid_columnconfigure(0, weight=1)

    def show_frame(self, frame):
        # Raise the selected frame to the top
        frame.tkraise()
        
    def Test(self, event):
        print("clicked")

 
        