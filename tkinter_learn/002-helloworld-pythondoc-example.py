# https://docs.python.org/2/library/tkinter.html
# 24.1.2.2


from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "say hi,everybody"
    
    def createWidgets(self):
        #quit button
        self.QUIT=Button(self)
        self.QUIT['text']='QUIT'
        self.QUIT['fg']='red'
        self.QUIT['command']=self.quit
        self.QUIT.pack({'side':'left'})
        #say hello button
        self.hi_there=Button(self)
        self.hi_there['text']='hi there'
        self.hi_there['command']=self.say_hi
        self.hi_there.pack({'side':'left'})
        
    def __init__(self,master):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()


root=Tk()
app=Application(master=root)
app.mainloop()
root.destroy()
  
        
        
