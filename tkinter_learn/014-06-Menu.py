from Tkinter import *
#https://blog.csdn.net/jcodeer/article/details/1811321

def printItem():
    print "aaaaaaaa"

root=Tk()
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
for k in range(5):
    filemenu.add_command(label=str(k),command=printItem)
menubar.add_cascade(label='language',menu=filemenu)
#insert a menu 
filemenu.insert_command(1,label='1000',command=printItem)
#insert a  checkbutton menu 
filemenu.insert_checkbutton(2,label='2000',command=printItem)
#insert a menu 
filemenu.insert_radiobutton(3,label='3000',command=printItem)
#insert a separator
filemenu.insert_separator(1)
filemenu.insert_separator(6)
#delete filemenu item
#filemenu.delete(0)
#filemenu.delete(6,9)
root['menu']=menubar
mainloop()
