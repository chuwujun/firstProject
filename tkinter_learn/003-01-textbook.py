# write content in entry Widget and write it to a file
# a textbook can write
from Tkinter import *

class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.entry1=Entry()
        self.entry1.pack()
        self.content=StringVar()
        self.content.set("")
        self.entry1['textvariable']=self.content
        self.entry1.bind('<Key-Return>',self.print_to_file)
    
    #a function which writes entry content to file output.txt
    def print_to_file(self,filename='output.txt'):
        f=open(filename,'a')
        f.write(str(elf.content.get()))
        f.close()
        print self.content.get()
        self.content.set('')
        
root=Tk()
app=App(root)
app.mainloop()
root.destroy()
        
