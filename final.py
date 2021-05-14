from tkinter import *
#from tkinter import filedialog
from cv2 import cv2
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os

root = Tk()
root.title("QR code scanner")
root.geometry('550x175')

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='C:/Users/Prajwal/Desktop/College/SEM 4/SEPM/LAB/LAB8/',
        filetypes=filetypes)
    file = open(filename, 'r')
    print(file.read())
    file.close()
    '''
    showinfo(
        title='Selected File',
        message=filename
    )
    '''
def openvid():
    os.startfile(r"D:\visual code\vid.py")

root.configure(background='lightgrey')
Label_0 = Label(root, text="QR and barcode scanner",width=20,font=("bold",15),bg="lightgrey")
Label_0.grid(row=0,column=1,pady=10)

Button_1 = Button(root, text="Scan", command=openvid, width = 20, bg = 'grey',fg='white',bd=5)
Button_1.grid(row=1,column=0)

Button_2 = Button(root, text="Upload",width = 20, bg = 'grey',fg='white',bd=5)
Button_2.grid(row=1,column=2)

Button_3 =Button(root, text="Recent scans", command=select_file, width = 20, bg = 'grey',fg='white',bd=5)
Button_3.grid(row=2,column=1)

Label_1 = Label(root)
root.mainloop()