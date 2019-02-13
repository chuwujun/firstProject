'''
Tkinter pydoc 24.1.6.4

The current-value setting of some widgets (like text entry widgets) can be connected directly to application variables by using special options. These options are variable, textvariable, onvalue, offvalue, and value. This connection works both ways: if the variable changes for any reason, the widget is connected to will be updated to reflect the new value.

Unfortunately, in the current implementation of Tkinter it is not possible to hand over an arbitrary Python variable to a widget through a variable or textvariable option. The only kinds of variables for which this works are variables that are subclassed from a class called Variable, defined in the Tkinter module.

There are many useful subclasses of Variable already defined: StringVar, IntVar, DoubleVar, and BooleanVar. To read the current value of such a variable, call the get() method on it, and to change its value you call the set() method. If you follow this protocol, the widget will always track the value of the variable, with no further intervention on your part.
'''
from Tkinter import *

class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.entrythingy=Entry()
        self.entrythingy.pack()
        #here is the application variable
        self.content=StringVar()
        self.content.set('this is a var')
        #tell the entry widget to watch the value
        self.entrythingy['textvariable']=self.content
        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.entrythingy.bind('<Key-Return>',self.print_contents)

    def print_contents(self,event):
        print "hi content now is :",self.content.get()


root=Tk()
app=App(root)
app.mainloop()
root.destroy()
