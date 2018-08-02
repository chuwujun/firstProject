from Tkinter import *

root=Tk()
root.title=('canvas test')
cvs=Canvas(root,width=600,height=400)
cvs.pack()
cvs.create_line(50,50,50,300)
cvs.create_line(100,50,200,300,fill='red',dash=(4,4),arrow=LAST)
cvs.create_rectangle(200,50,400,200,fill='blue')
cvs.create_polygon(200, 250, 350, 250, 350, 350, 220, 300, fill="yellow")


mainloop()
