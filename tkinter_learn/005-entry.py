from Tkinter import *
#https://blog.csdn.net/bemorequiet/article/details/54731029

root=Tk()
entry1=Entry(root)
entry1.pack(padx=20,pady=20)
entry1.delete(0,END)
entry1.insert(0,"this is default value")
root.mainloop()
