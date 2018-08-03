from Tkinter import *
#checkbutton and Menu
def printItem():
    print 'PHP=',vPHP.get()
    print 'CPP=',vCPP.get()
    print 'C=',vC.get()
    print 'Python=',vPython.get()

root=Tk()
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
vPHP=StringVar()
vCPP=StringVar()
vC=StringVar()
vPython=StringVar()
for k,v in {'PHP':vPHP,'CPP':vCPP,'C':vC,'Python':vPython}.items():
    filemenu.add_checkbutton(label=k,command=printItem,variable=v)
menubar.add_cascade(label='language',menu=filemenu)
root['menu']=menubar
mainloop()
