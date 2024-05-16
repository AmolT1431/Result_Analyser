from tkinter import *
from App.Center import *
from App.Frames import *
from Frames.Buttons import*
from Frames.Option_Frame import*
 

class Option_Frame(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent,bg="lightgray",width=0,height=100)
        
        
        for i in range(3):
            self.columnconfigure(i, weight=2)  # Allow columns to expand equally
        for j in range(2):
            self.rowconfigure(j, weight=2)  # Allow rows to expand 
            

    def add_buttons(self,Display_label,myframe):
            
        button1 = tk.Frame(self, bg="white", width=200, height=75)
        button1.grid(row=0, column=0, padx=5, pady=10)  # Reduced padding
        button1.bind("<Button-1>", lambda event: b1_click(Display_label,myframe))
        label_text = "Prn List"
        label = tk.Label(button1, text=label_text,bg="white",font=("Times New Roman", 20,"bold"))
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)




        button2 = tk.Frame(self, bg="white", width=200, height=75)
        button2.grid(row=1, column=0, padx=5, pady=15)  # Reduced padding
        button2.bind("<Button-1>", lambda event: b2_click(Display_label,myframe))
        label_text = "Staticstic"
        label = tk.Label(button2, text=label_text,bg="white",font=("Times New Roman", 20,"bold"))
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)





        button3 = tk.Frame(self, bg="white",  width=200, height=75)
        button3.grid(row=0, column=1, padx=5, pady=5)  # Reduced padding
        button3.bind("<Button-1>", lambda event: b3_click(Display_label,myframe))
        label_text = "Find Result"
        label = tk.Label(button3, text=label_text,bg="white",font=("Times New Roman", 20,"bold"))
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        




        button4 = tk.Frame(self, bg="white",  width=200, height=75)
        button4.grid(row=1, column=1, padx=5, pady=5)  # Reduced padding
        button4.bind("<Button-1>", lambda event: b4_click(Display_label,myframe))
        label_text = "Pass & Fail"
        label = tk.Label(button4, text=label_text,bg="white",font=("Times New Roman", 20,"bold"))
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        





        button5 = tk.Frame(self, bg="white",  width=200, height=75)
        button5.grid(row=0, column=2, padx=5, pady=5)  # Reduced padding
        button5.bind("<Button-1>", lambda event: b5_click(Display_label,myframe))
        label_text = "Sort List"
        label = tk.Label(button5, text=label_text,bg="white",font=("Times New Roman", 20,"bold"))
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        



        button6 = tk.Frame(self, bg="white", width=200, height=75)
        button6.grid(row=1, column=2, padx=5, pady=5)  # Reduced padding
        button6.bind("<Button-1>", lambda event: b6_click(Display_label,myframe))
        label_text = "Top 5"
        label = tk.Label(button6, text=label_text,bg="white",font=("Times New Roman", 20,"bold"))
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

