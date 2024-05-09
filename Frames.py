import tkinter as tk

class Display_Frames:
    def __init__(self, display_content_frame):
        self.frame1 = tk.Frame(display_content_frame, bg="red")
        label1 = tk.Label(self.frame1, text="Frame 1")
        label1.pack(padx=20, pady=20)
        self.frame1.grid(row=0, column=0, sticky="nsew")

        self.frame2 = tk.Frame(display_content_frame, bg="blue")
        label2 = tk.Label(self.frame2, text="Frame 2")
        label2.pack(padx=20, pady=20)
        self.frame2.grid(row=0, column=0, sticky="nsew")
        
        self.frame3 = tk.Frame(display_content_frame, bg="yellow")
        label3 = tk.Label(self.frame3, text="Frame 3")
        label3.pack(padx=20, pady=20)
        self.frame3.grid(row=0, column=0, sticky="nsew")
        
        
        self.frame4 = tk.Frame(display_content_frame, bg="pink")
        label4 = tk.Label(self.frame4, text="Frame 4")
        label4.pack(padx=20, pady=20)
        self.frame4.grid(row=0, column=0, sticky="nsew")
        
        
        self.frame5 = tk.Frame(display_content_frame, bg="black")
        label5 = tk.Label(self.frame5, text="Frame 5")
        label5.pack(padx=20, pady=20)
        self.frame5.grid(row=0, column=0, sticky="nsew")
        
        
        self.frame6 = tk.Frame(display_content_frame, bg="blue")
        label6 = tk.Label(self.frame6, text="Frame 6")
        label6.pack(padx=20, pady=20)
        self.frame6.grid(row=0, column=0, sticky="nsew")
        

        display_content_frame.grid_rowconfigure(0, weight=1)
        display_content_frame.grid_columnconfigure(0, weight=1)

    def show_frame(self, frame):
        # Raise the selected frame to the top
        frame.tkraise()
        
    def Test(self, event):
        print("clicked")

 
