#https://blog.csdn.net/bemorequiet/article/details/54731029

from Tkinter import *

root=Tk()
s1=Scale(root,from_=0,to=42,tickinterval=5,resolution=5,length=150)
s1.pack()
s2=Scale(root,from_=0,to=200,orient=HORIZONTAL)
s2.pack()

def show():
    print(s1.get(),s2.get())

Button(root,text='get location',command=show).pack()
mainloop()
