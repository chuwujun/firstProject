#this is a textbook which can write content to a file

from Tkinter import *
import tkMessageBox
import os

#read file and show its content on text
def read_file():
    filename=content.get()
    if not os.path.exists(filename):
        tkMessageBox.showinfo("warning","file "+filename+" does not exist.")
        return
    f=open(filename,'r')
    file_content_list=f.readlines()
    f.close()
    file_content=''.join(file_content_list)
    #clear the content in text
    text1.delete(1.0,END)
    #write file content to txt
    text1.insert(1.0,file_content)
    #print file_content

#write text content to file
def write_file():
    filename=content.get()
    text_content=text1.get(1.0,END)
    # judge path exist and make sure whether save or not
    if os.path.exists(filename):
         tkMessageBox.askyesno('file has exist','save or not?')
    f=open(filename,'w')
    f.write(text_content)
    f.close()
    print text_content

#clear content of text
def clear_text():
    #this is to set entry is ""
    #content.set("")
    text1.delete(1.0,END)

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
    button1=Button(frame3,text="write",command=write_file)
    button1.pack({'side':'left'})
    #this button is to read file to text
    button4=Button(frame3,text="read",command=read_file)
    button4.pack({'side':'left'})
    #this button is to clear text content
    button2=Button(frame3,text="clear",command=clear_text)
    button2.pack({'side':'left'})
    #this content is to quit the GUI
    button3=Button(frame3,text="quit",command=quit)
    button3.pack({'side':'left'})
    root.mainloop()
