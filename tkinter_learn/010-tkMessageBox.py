from Tkinter import *
import tkMessageBox

def answer():
    tkMessageBox.showerror('Answer','Sorry,no answer exists.')

def b_quit():
    if tkMessageBox.askyesno('Quit','quit or not?'):
        tkMessageBox.showwarning('Warning','not yet implement')
    else:
        tkMessageBox.showinfo('No','quit has been canceled')    

root=Tk()
button1=Button(root,text='answer',command=answer)
button2=Button(root,text='quit',command=b_quit)
button1.pack(fill=X)
button2.pack(fill=X)
mainloop()

