import tkinter as tk
from tkinter import *

class Control_Panel(Frame):
    def __init__(self, parent):
        super().__init__(parent,bg="white")
        
        button1 = tk.Button(self,height=2, text="Button 1", command=lambda: self.button_clicked(1))
        button2 = tk.Button(self,height=2, text="Button 2", command=lambda: self.button_clicked(2))
        button3 = tk.Button(self,height=2, text="Button 3", command=lambda: self.button_clicked(3))
        button4 = tk.Button(self,height=2, text="Button 4", command=lambda: self.button_clicked(4))

        button1.pack(fill='x',pady=(150,15),padx=(10,10))
        button2.pack(fill='x',pady=(0,15),padx=(10,10))
        button3.pack(fill='x',pady=(0,15),padx=(10,10))
        button4.pack(fill='x',pady=(0,15),padx=(10,10))
        
        self.pack(expand=True, fill="both",padx=10,pady=10)
        
    def button_clicked(self, button_number):
        print(f"Button {button_number} clicked")
 