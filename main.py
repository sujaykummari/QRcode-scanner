from tkinter import *
#from tkinter import filedialog
from cv2 import cv2
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os

root = Tk()
root.title("QR code scanner")
root.geometry('350x200')

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
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
    os.startfile(r"C:\Users\G.P\Desktop\qr\videoexe.pyc")
'''
def openpic():
    
    filename1 = fd.askopenfilename(
        title='Open a file',
        initialdir='/')
    
    print(filename1)
'''  

root.configure(background='lightgrey')
Label_0 = Label(root, text="QR and Barcode scanner",width=20,font="cambria 20 bold",bg="lightgrey")
Label_0.grid(row=0,column=1,pady=10, padx=10)

Button_1 = Button(root, text="Scan", command=openvid, width = 15, font="cambria 15 ", bg = 'grey',fg='white',bd=5)
Button_1.grid(row=1,column=1, padx=10, pady =(10,0))

#Button_2 = Button(root, text="Upload",command=openpic, width = 20, bg = 'grey',fg='white',bd=5)
#Button_2.grid(row=1,column=2)

Button_3 =Button(root, text="Recent scans", command=select_file, width = 15, font="cambria 15 ", bg = 'grey',fg='white',bd=5)
Button_3.grid(row=2,column=1, padx=10)

Label_1 = Label(root, text = "Made by Prajwal,Jishnu,Aditya", font="cambria 10", bg = 'lightgrey')
Label_1.grid(row=3, column=1, pady=(20,0))
root.mainloop()