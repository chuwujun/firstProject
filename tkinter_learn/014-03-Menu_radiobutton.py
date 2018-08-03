from Tkinter import *

def printItem():
    print vLang.get()

root=Tk()
menuBar=Menu(root)
vLang=StringVar()
filemenu=Menu(menuBar,tearoff=0)
for k in ['PHP','Python','C']:
    filemenu.add_radiobutton(label=k,command=printItem,variable=vLang)
menuBar.add_cascade(label='language',menu=filemenu)
root['menu']=menuBar
mainloop()
