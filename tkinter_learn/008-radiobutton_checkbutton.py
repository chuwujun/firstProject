from Tkinter import *

def helloChecked():
    labelHello.config(fg=color.get())

def typeChecked():
    textType=typeBold.get()+typeAtalic.get()
    if textType==1:
        labelHello.config(font=('Arial',12,'bold'))
    elif textType==2:
        labelHello.config(font=('Arial',12,'italic'))
    elif textType==3:
        labelHello.config(font=('Arial',12,'bold italic'))
    else:
        labelHello.config(font=('Arial',12))

root=Tk()
root.title("radiobutton and checkbutton")
labelHello=Label(root,text='I am a label to be operated',height=3,font=('Arial',12))
labelHello.pack()
#set RadioButton
color=StringVar()
Radiobutton(root,text="Red",variable=color,value='red',command=helloChecked)\
           .pack(side='left')
Radiobutton(root,text="Blue",variable=color,value='blue',command=helloChecked)\
           .pack(side='left')
Radiobutton(root,text="Yellow",variable=color,value='yellow',command=helloChecked)\
           .pack(side='left')
#set checkbutton
typeBold=IntVar()
typeAtalic=IntVar()
Checkbutton(root,text='Bold',variable=typeBold,onvalue=1,offvalue=0,command=typeChecked).pack(side='left')
Checkbutton(root,text='Atalic',variable=typeAtalic,onvalue=2,offvalue=0,command=typeChecked).pack(side='left')

mainloop()
