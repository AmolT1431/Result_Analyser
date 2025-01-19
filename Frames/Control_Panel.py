import tkinter as tk
from tkinter import *
from tkinter import ttk
from DialogBox.Folder_Select import*


class Control_Panel(tk.Frame):
    def __init__(self, parent, labels):
        super().__init__(parent, bg="white")
        self.label, self.label2, self.label3 = labels

        # Create buttons with custom colors
        button1 = tk.Button(self, text="Load PRN List", font=('Times New Roman', 15, 'bold'), 
                            bg='#FF7722', fg='black', activebackground='green', activeforeground='black', 
                            command=lambda: select_file(self.label))
        button2 = tk.Button(self, text="Download Result", font=('Times New Roman', 15, 'bold'), 
                            bg='#FF7722', fg='black', activebackground='green', activeforeground='black', 
                            command=lambda: Result_download(self.label2))
        button3 = tk.Button(self, text="Process DATA", font=('Times New Roman', 15, 'bold'), 
                            bg='#FF7722', fg='black', activebackground='green', activeforeground='black', 
                            command=lambda: Process_Data(self.label3))

        # Pack the buttons
        button1.pack(fill='x', pady=(200, 15), padx=(10, 10))
        button2.pack(fill='x', pady=(0, 15), padx=(10, 10))
        button3.pack(fill='x', pady=(0, 15), padx=(10, 10))

        self.pack(expand=True, fill="both", padx=10, pady=10)
        
    def button_clicked(self, button_number):
        print(f"Button {button_number} clicked")
 