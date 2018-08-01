from Tkinter import *
#https://blog.csdn.net/bemorequiet/article/details/54731029

root=Tk()
lbx=Listbox(root,height=10)
lbx.pack()
#add list item to listbox
for items in ['apple','peer','orange','strawberry']:
    lbx.insert(END,items)

#when list item has been chosen,its status is ACTIVE.
button1=Button(root,text='delete the item',command=lambda x=lbx:x.delete(ACTIVE))
button1.pack()
root.mainloop()
