from Tkinter import *

output=""
tmp_symbol=''
input_list=[]

def button_1_add():
    e1.insert(END,'1')
    input_list.append('1')

def button_2_add():
    e1.insert(END,'2')
    input_list.append('2')

def button_3_add():
    e1.insert(END,'3')
    input_list.append('3')

def button_4_add():
    e1.insert(END,'4')
    input_list.append('4')

def button_5_add():
    e1.insert(END,'5')
    input_list.append('5')

def button_6_add():
    e1.insert(END,'6')
    input_list.append('6')

def button_7_add():
    e1.insert(END,'7')
    input_list.append('7')

def button_8_add():
    e1.insert(END,'8')
    input_list.append('8')

def button_9_add():
    e1.insert(END,'9')
    input_list.append('9')

def button_0_add():
    e1.insert(END,'0')
    input_list.append('0')

def button_add_add():
    e1.insert(END,'+')
    input_list.append('+')

def button_del_add():
    e1.insert(END,'-')
    input_list.append('-')

def button_che_add():
    e1.insert(END,'*')
    input_list.append('*')

def button_div_add():
    e1.insert(END,'/')
    input_list.append('/')

def button_clear():
    input_list=[]
    tmp_symbol=''
    output=''
    e1.delete(0,END)
    content.set('')

def button_getResult():
    for i in ['+','-','*','/']:
        if i in input_list:
            tmp_symbol=i
    if tmp_symbol!='':
        handle_cal(tmp_symbol)

def handle_cal(sym):
    index_of_sym=input_list.index(sym)
    int1=int(''.join(input_list[0:index_of_sym]))
    int2=int(''.join(input_list[index_of_sym+1:]))
    if sym=='+':
        output=str(int1+int2)
    if sym=='-':
        output=str(int1-int2)
    if sym=='*':
        output=str(int1*int2)
    if sym=='/':
        output=str(int1/int2)
    content.set(output)
    
            
root=Tk()
root.title('calculator')
content=StringVar()
e1=Entry(root,textvariable=content)
e1.grid(row=0,columnspan=4)
button1=Button(root,text='1',width=5,height=5,command=button_1_add)
button1.grid(row=1,column=0)
button2=Button(root,text='2',width=5,height=5,command=button_2_add)
button2.grid(row=1,column=1)
button3=Button(root,text='3',width=5,height=5,command=button_3_add)
button3.grid(row=1,column=2)
button_add=Button(root,text='+',width=5,height=5,command=button_add_add)
button_add.grid(row=1,column=3)
button4=Button(root,text='4',width=5,height=5,command=button_4_add)
button4.grid(row=2,column=0)
button5=Button(root,text='5',width=5,height=5,command=button_5_add)
button5.grid(row=2,column=1)
button6=Button(root,text='6',width=5,height=5,command=button_6_add)
button6.grid(row=2,column=2)
button_del=Button(root,text='-',width=5,height=5,command=button_del_add)
button_del.grid(row=2,column=3)
button7=Button(root,text='7',width=5,height=5,command=button_7_add)
button7.grid(row=3,column=0)
button8=Button(root,text='8',width=5,height=5,command=button_8_add)
button8.grid(row=3,column=1)
button9=Button(root,text='9',width=5,height=5,command=button_9_add)
button9.grid(row=3,column=2)
button_che=Button(root,text='*',width=5,height=5,command=button_che_add)
button_che.grid(row=3,column=3)
button_clear=Button(root,text='C',width=5,height=5,command=button_clear)
button_clear.grid(row=4,column=0)
button0=Button(root,text='0',width=5,height=5,command=button_0_add)
button0.grid(row=4,column=1)
button_get=Button(root,text='=',width=5,height=5,command=button_getResult)
button_get.grid(row=4,column=2)
button_div=Button(root,text='/',width=5,height=5,command=button_div_add)
button_div.grid(row=4,column=3)
mainloop()
