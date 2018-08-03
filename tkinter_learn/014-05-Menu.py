from Tkinter import *

def printItem():
    print "pop"

def pop_event(event):
    menuBar.post(event.x_root,event.y_root)

root=Tk()
menuBar=Menu(root)
filemenu=Menu(menuBar,tearoff=0)
for k in ['PHP','C','Python']:
    filemenu.add_command(label=k,command=printItem)
    filemenu.add_separator()
menuBar.add_cascade(label='Language',menu=filemenu)
root.bind('<Button-3>',pop_event)



mainloop()

