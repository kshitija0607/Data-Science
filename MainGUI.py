from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import Bridge_Crack_Detection
#import ViewResult
# import viewgui


def center_window(w,h):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
root=Tk()

root.title("Bridge Crack Detection System")
center_window(1600, 1000)
# Read the Image
image = Image.open("main_image.jpg")

# Resize the image using resize() method
resize_image = image.resize((1600, 1000))

img = ImageTk.PhotoImage(resize_image)

# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()

    
def read_input():
    filepath=textBox1.get()
    print(" filepath is ",filepath)
    
    Bridge_Crack_Detection.initDetection(filepath)
    
    root.destroy()
   

    

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                        ("all files",
                                                        "*.*")))
      
    textBox1.insert(0, filename)

# def open_New_Frame():
#     p1=viewgui.Results()
#     p1.initNewWindow()
       
    
    


# code to create label 
label1 = Label(root,text = "Select File: ",fg='#FFFFFF',bg='#000000',font=("Ariel", 12)).place(x = 350,y = 305)


#code to insert textbox
textBox1 = tk.Entry(root, width = 60)
textBox1.place(x = 520,y = 305,height=35)


browsebutton=Button(root, height=1, width=13, font=("Ariel", 10,'bold'),fg='#FFFFFF',bg='#FF5F1F',text="Browse",  command=lambda: browseFiles()).place(x=1150,y=305)
#command=lambda: retrieve_input() >>> just means do this when i press the button
submitebutton=Button(root, height=1, width=13, font=("Ariel", 10,'bold'),fg='#FFFFFF',bg='#FF5F1F',text="Submit", command=lambda: read_input()).place(x=650,y=430)
# Button for closing
exit_button = Button(root, height=1, width=13, font=("Ariel", 10,'bold'),fg='#FFFFFF',bg='#FF5F1F',text="Exit", command=root.destroy).place(x=850,y=430)



mainloop()