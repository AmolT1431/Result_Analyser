from tkinter import *
from Center import *
from Frames import *
from Buttons import*
 


App = Tk()
App.title("Test")
App.geometry('1050x700')
# App.maxsize('1050','700')
App.minsize('850','350')
App.resizable(width=TRUE,height=True)
 

App.update_idletasks()
 
Center.center_window(App,App.winfo_width(),App.winfo_height())

# Create the main frame
main_frame = Frame(App, bg="black", width=1000, height=700)
main_frame.pack(fill=BOTH, expand=True)

#######################################################################
control_frame=Frame(main_frame,bg="lightgray",width=0,height=0)
control_frame.pack(side=RIGHT,fill="both",expand=False)

Logo_frame=Frame(control_frame,bg="white",width=300,height=200)
Logo_frame.pack(side=TOP,fill="x",padx=(15,15),pady=10)

########################################################################

########################################################################
content_frame=Frame(main_frame,bg="black",width=600,height=0)
content_frame.pack(side=LEFT,fill="both",padx=(0,10),expand=TRUE)

option_frame=Frame(content_frame,bg="lightgray",width=0,height=150)
option_frame.pack(side=TOP,fill="both",expand=FALSE,pady=(0,10))

display_frame=Frame(content_frame,bg="white",width=0,height=750)
display_frame.pack(side=BOTTOM,fill="both",expand=True)

display_content_frame = Frame(display_frame, bg="blue", width=600, height=550)
display_content_frame.pack(side=BOTTOM, fill="both", expand=True)

Display_label = Label(display_frame, text="Display", bg="white",font=("Times New Roman", 20,"bold"))
Display_label.pack(side=TOP, fill=X)

myframe=Display_Frames(display_content_frame)
 

# Initially show frame1
myframe.show_frame(myframe.frame1)
 
###########################################################################


for i in range(3):
    option_frame.columnconfigure(i, weight=2)  # Allow columns to expand equally
for j in range(2):
    option_frame.rowconfigure(j, weight=2)  # Allow rows to expand 
    

    
button1 = Frame(option_frame, bg="white", width=200, height=75)
button1.grid(row=0, column=0, padx=5, pady=10)  # Reduced padding
button1.bind("<Button-1>", lambda event: b1_click(Display_label,myframe))
label_text = "List Prn"
label = Label(button1, text=label_text,bg="white",font=("Times New Roman", 20,"bold"))
label.place(relx=0.5, rely=0.5, anchor=CENTER)




button2 = Frame(option_frame, bg="white", width=200, height=75)
button2.grid(row=1, column=0, padx=5, pady=15)  # Reduced padding
button2.bind("<Button-1>", lambda event: b2_click(Display_label,myframe))
label_text = "Staticstic"
label = Label(button2, text=label_text,bg="white",font=("Times New Roman", 20,"bold"))
label.place(relx=0.5, rely=0.5, anchor=CENTER)





button3 = Frame(option_frame, bg="white",  width=200, height=75)
button3.grid(row=0, column=1, padx=5, pady=5)  # Reduced padding
button3.bind("<Button-1>", lambda event: b3_click(Display_label,myframe))
label_text = "Find Result"
label = Label(button3, text=label_text,bg="white",font=("Times New Roman", 20,"bold"))
label.place(relx=0.5, rely=0.5, anchor=CENTER)
 




button4 = Frame(option_frame, bg="white",  width=200, height=75)
button4.grid(row=1, column=1, padx=5, pady=5)  # Reduced padding
button4.bind("<Button-1>", lambda event: b4_click(Display_label,myframe))
label_text = "Pass & Fail"
label = Label(button4, text=label_text,bg="white",font=("Times New Roman", 20,"bold"))
label.place(relx=0.5, rely=0.5, anchor=CENTER)
 





button5 = Frame(option_frame, bg="white",  width=200, height=75)
button5.grid(row=0, column=2, padx=5, pady=5)  # Reduced padding
button5.bind("<Button-1>", lambda event: b5_click(Display_label,myframe))
label_text = "Sort List"
label = Label(button5, text=label_text,bg="white",font=("Times New Roman", 20,"bold"))
label.place(relx=0.5, rely=0.5, anchor=CENTER)
 



button6 = Frame(option_frame, bg="white", width=200, height=75)
button6.grid(row=1, column=2, padx=5, pady=5)  # Reduced padding
button6.bind("<Button-1>", lambda event: b6_click(Display_label,myframe))
label_text = "Top 5"
label = Label(button6, text=label_text,bg="white",font=("Times New Roman", 20,"bold"))
label.place(relx=0.5, rely=0.5, anchor=CENTER)



main_frame.mainloop()
 
