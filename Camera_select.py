# from tkinter import *
# import os

# def sel():
#     if var.get() == 1:
#         root.destroy()
#         os.system("python face_recognize1.py")
#     else:
#         root.destroy()
#         os.system("python face_recognize2.py")

# root = Tk()
# root.geometry("250x125")
# root.title("Device Selection")

# label = Label(root, text="Please Select the device")
# label.pack()

# var = IntVar()

# R1 = Radiobutton(root, text="IP Camera", variable=var, value=1, command=sel)
# R1.pack(anchor=W)

# R2 = Radiobutton(root, text="Phone Camera", variable=var, value=2, command=sel)
# R2.pack(anchor=W)

# root.mainloop()

from tkinter import *
import os

def sel():
    if var.get() == 1:
        root.destroy()
        os.system("python face_recognize.py")
    else:
        root.destroy()
        print("Please select the Laptop Camera.")

root = Tk()
root.geometry("250x75")
root.title("Device Selection")

label = Label(root, text="Laptop Camera is selected by default.")
label.pack()

var = IntVar()
var.set(1)  # Set default selection to Laptop Camera

R1 = Radiobutton(root, text="Laptop Camera", variable=var, value=1, command=sel)
R1.pack(anchor=W)

root.mainloop()
