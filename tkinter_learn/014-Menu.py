from Tkinter import *
#https://blog.csdn.net/jcodeer/article/details/1811321
def print_hello():
    print "hello"

root=Tk()
menuBar=Menu(root)
for items in ['PHP','Python','C','Java']:
    menuBar.add_command(label=items,command=print_hello)
root['menu']=menuBar

mainloop()

