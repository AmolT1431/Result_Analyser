from tkinter import *
from Center import *

main_frame = Tk()
main_frame.title("Test")
main_frame.geometry('1000x700')
main_frame.maxsize('1000','700')
main_frame.minsize('500','300')

main_frame.update_idletasks()
 
Center.center_window(main_frame,main_frame.winfo_width(),main_frame.winfo_height())

# Create the main frame
main_frame_bg = Frame(main_frame, bg="lightgray", width=1000, height=700)
main_frame_bg.pack(fill=BOTH, expand=True)


# Create the inner frame
display = Frame(main_frame_bg, bg="lightblue", width=200, height=100)
display.pack(side=BOTTOM, anchor='sw', padx=20, pady=20)


main_frame.mainloop()
 
