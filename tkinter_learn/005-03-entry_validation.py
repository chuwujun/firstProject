from Tkinter import *
import tkMessageBox

#https://blog.csdn.net/bemorequiet/article/details/54731512

def test(content,reason,name):
    if content=="mini":
        print('right password')
        print content,reason,name
        return True
    else:
        print 'wrong password'
        print(content,reason,name)
        return False

root=Tk()
testCmd=root.register(test)
v=StringVar()
e1=Entry(root,textvariable=v,validate='focusout',\
         validatecommand=(testCmd,'%P','%v','%W'))
e2=Entry(root)
e1.pack(padx=10,pady=10)
e2.pack(padx=10,pady=10)
mainloop()
        
