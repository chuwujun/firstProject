from Tkinter import *

def print_selection():
    value=lb.get(lb.curselection())
    var1.set(value)

root=Tk()
root.title('listbox')
root.geometry('200x200')
var1=StringVar()
label1=Label(bg='green',width=6,textvariable=var1)
label1.pack()
button1=Button(root,text='print selection',width=15,height=1,command=print_selection)
button1.pack()
var2=StringVar()
var2.set((55,22,11))
lb=Listbox(root,listvariable=var2)
list_items=[1,2,3,4]
#insert list item to listbox
for item in list_items:
    lb.insert(END,item)
lb.insert(1,'first')
lb.insert(2,'second')
#delete listbox item whose index is 2
lb.delete(2)
lb.pack()
mainloop()


