
from tkinter import *
from Frames.Fail import *
from Frames.Pass import *

class Pass_Fail(Frame):
    def __init__(self, parent):
        super().__init__(parent,bg="yellow")
        
        passframe=Pass(self)
        
        failframe=Fail(self)
         
        self.grid(row=0, column=0, sticky="nsew")