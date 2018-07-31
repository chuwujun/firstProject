from Tkinter import *

class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()


#create the application
app=App()
app.master.title("hello simon")
app.master.maxsize(1000,400)
#start the program
app.mainloop()
