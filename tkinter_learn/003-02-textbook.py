#this is a textbook which can write content to a file

from Tkinter import *

if __name__ == '__main__':
    #create the application
    root=Tk()
    root.title("your textbook")
    #create frame1,it contains label1 and entry1
    frame1=Frame(root)
    frame1.pack({'side':'top'})
    #this is the filename
    label1=Label(frame1,text="filename:")
    label1.pack({'side':'left'}) 
    entry1=Entry(frame1)
    #you can not set entry default value by param text
    entry1.config(text='output.txt')
    content=StringVar()
    content.set('output.txt')
    entry1['textvariable']=content
    entry1.pack({'side':'left'})
    #this is the content that we need to save
    text1=Text(root,height=30)
    text1.pack({'side':'top'})
    #this is the frame contains buttons
    frame3=Frame(root)
    frame3.pack({'side':'top'})
    #this button is to write file content
    button1=Button(frame3,text="write")
    button1.pack({'side':'left'})
    #this button is to read file to text
    button4=Button(frame3,text="read")
    button4.pack({'side':'left'})
    #this button is to clear text content
    button2=Button(frame3,text="clear")
    button2.pack({'side':'left'})
    #this content is to quit the GUI
    button3=Button(frame3,text="quit",command=quit)
    button3.pack({'side':'left'})
    root.mainloop()
