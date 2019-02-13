from Tkinter import *
from tkFileDialog import *

root=Tk()
errmsg='error'

def openfile():
    name=askopenfilename()
    print name

button=Button(root,text='filename',command=openfile)
button.pack(fill=X)
mainloop()
