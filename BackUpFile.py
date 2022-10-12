# import tkinter module
import tkinter as tk
from tkinter import *
import shutil, os, datetime, time, sys
# read File Destination
file_path = "filepaths.txt"
file = open(file_path)
data = file.readlines()
file.close()
path=(data[0])
path2=(data[1])
path1 = path.replace(os.sep, '/')
source=path1.replace('\n',"")
parent_dir = path2.replace(os.sep, '/')

# Copy file
def run_copy(parent_dir,source):
    newFolderName = datetime.datetime.now()
    newFolder = str(newFolderName.strftime('%b_%d_%Y_%I%p_%M_%S'))
    path = os.path.join(parent_dir, newFolder)
    os.mkdir(path)
    destination = ("BackUpLocation: \n"+path)
    shutil.copy(source, path)
    return (destination)

# Tkinter Start
window = tk.Tk()
window.iconbitmap('logo.ico')
window.geometry('800x300')
window.title('Back Up file!')
window.configure(background="#F4EBD0")
#Labels
label_source_location = tk.Label(window, text=("Source Path--File to copy: \n"+source),fg="#004369", bg="#F4EBD0",font=('Aerial 12 bold'))
label1 = tk.Label(window, text="", fg="#004369", bg="#F4EBD0",font=('Aerial 12 bold'))
label_source_location.place(relx=0.1, rely=0.35)
label1.place(relx=0.1, rely=0.55)
# First Button
def btn1_click():
    txt =(run_copy(parent_dir,source))
    label1.configure(text=txt)
btn1 = tk.Button(window, text="Back Up file",fg="#004369",font=("Comic Sans MS", 20, "bold"), command=btn1_click)
btn1.place(relx=0.5, rely=0.2,anchor=CENTER )

# Second Button
def close():
    window.destroy()
btn2 =tk.Button(window, text="exit",fg="#004369", font=("Comic Sans MS", 20, "bold"), command=close)
btn2.place(relx=0.5, rely=0.85, anchor=CENTER  )
window.mainloop()