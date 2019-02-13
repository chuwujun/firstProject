from Tkinter import *
#https://blog.csdn.net/bemorequiet/article/details/54731029

root=Tk()
scb=Scrollbar(root)
scb.pack(side='right',fill=Y)
lb=Listbox(root,yscrollcommand=scb.set)
for i in range(1000):
    lb.insert(END,i)
lb.pack(side='left',fill=BOTH)
scb.config(command=lb.yview)
root.mainloop()

