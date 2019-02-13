from Tkinter import *
#https://blog.csdn.net/jcodeer/article/details/1811316
root=Tk()
#increment not used,
spinbox=Spinbox(root,values=(0,2,20,4,-1),increment=2)
spinbox.pack()
print spinbox['values']
mainloop()
