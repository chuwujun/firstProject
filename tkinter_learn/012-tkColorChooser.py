from Tkinter import *
from tkColorChooser import *

def callback():
    color=askcolor(color='red',title='hi,baby,come to choose a color')
    print color

root=Tk()
Button(root,text='choose a color',command=callback).pack(fill=X)
Button(root,text='quit',command=quit).pack(fill=X)
mainloop()
