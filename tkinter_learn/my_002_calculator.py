from Tkinter import *

input=""
output=""
output_list=[]

def button_1_add():
    pass


root=Tk()
root.title('calculator')
content=StringVar()
e1=Entry(root,textvariable=content)
e1.grid(row=0,columnspan=4)
button1=Button(root,text='1',width=5,height=5)
button1.grid(row=1,column=0)
button2=Button(root,text='2',width=5,height=5)
button2.grid(row=1,column=1)
button3=Button(root,text='3',width=5,height=5)
button3.grid(row=1,column=2)
button_add=Button(root,text='+',width=5,height=5)
button_add.grid(row=1,column=3)
button4=Button(root,text='4',width=5,height=5)
button4.grid(row=2,column=0)
button5=Button(root,text='5',width=5,height=5)
button5.grid(row=2,column=1)
button6=Button(root,text='6',width=5,height=5)
button6.grid(row=2,column=2)
button_del=Button(root,text='-',width=5,height=5)
button_del.grid(row=2,column=3)
button7=Button(root,text='7',width=5,height=5)
button7.grid(row=3,column=0)
button8=Button(root,text='8',width=5,height=5)
button8.grid(row=3,column=1)
button9=Button(root,text='9',width=5,height=5)
button9.grid(row=3,column=2)
button_che=Button(root,text='*',width=5,height=5)
button_che.grid(row=3,column=3)
button_clear=Button(root,text='C',width=5,height=5)
button_clear.grid(row=4,column=0)
button0=Button(root,text='0',width=5,height=5)
button0.grid(row=4,column=1)
button_get=Button(root,text='=',width=5,height=5)
button_get.grid(row=4,column=2)
button_div=Button(root,text='/',width=5,height=5)
button_div.grid(row=4,column=3)
mainloop()
