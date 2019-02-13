from Tkinter import *
#https://blog.csdn.net/jcodeer/article/details/1811321
def print_hello():
    print "hello"
#menuBar contains filemenu
root=Tk()
menuBar=Menu(root)
filemenu=Menu(menuBar,tearoff=0)
for items in ['PHP','Python','C','Java']:
    filemenu.add_command(label=items,command=print_hello)
menuBar.add_cascade(label='language',menu=filemenu)
root['menu']=menuBar

mainloop()

