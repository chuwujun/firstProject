from Tkinter import *
#https://blog.csdn.net/jcodeer/article/details/1811321
def printItem():
    print "add separator"

root=Tk()
menuBar=Menu(root)
filemenu=Menu(menuBar,tearoff=0)
for k in ['PHP','Python','C']:
    filemenu.add_command(label=k,command=printItem)
    filemenu.add_separator()
menuBar.add_cascade(label='Language',menu=filemenu)
root['menu']=menuBar

mainloop()
