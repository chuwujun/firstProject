#https://blog.csdn.net/bemorequiet/article/details/54731145

from Tkinter import *

root=Tk()
#user grid to plat
Label(root,text='bookname:').grid(row=0,column=0)
Label(root,text='author:').grid(row=1,column=0)
e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)

def show():
    print "bookname is "+e1.get()
    print "author is "+e2.get()

Button(root,text='get message',width=10,command=show)\
       .grid(row=3,column=0,sticky=W,pady=5)
Button(root,text='quit',width=10,command=root.quit)\
       .grid(row=3,column=1,sticky=E,padx=10,pady=5)
mainloop()
