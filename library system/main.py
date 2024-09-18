#CSC PROJECT

from tkinter import *
import tkinter.ttk
import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="tarun12345",database="db")
curosr=db.cursor()



root=Tk()
root.title("Library")
root.configure(bg='black')
root.minsize(width=700,height=700)
root.geometry("800x800")


bg=PhotoImage(file="C:/Users/TEAM/Pictures/daylight2.png")

my_label=Label(root, image=bg)
my_label.place(x=1,y=1,relwidth=1,relheight=1)



def members():
    



    root.destroy()
    import member

def Add():
    
    boot=Tk()
    boot.title("Members")
    boot.geometry("800x800")
    
    boot.minsize(width=700,height=700)
    root.destroy()

def Booklist():
    
    boot=Tk()
    boot.title("Members")
    boot.geometry("800x800")
    boot.minsize(width=700,height=700)
    root.destroy()

def issue():
    
    root.destroy()
    import issue

def status():
    
    boot=Tk()
    boot.title("Members")
    boot.geometry("800x800")
    boot.minsize(width=700,height=700)
    root.destroy()

def returns():
    
    boot=Tk()
    boot.title("Members")
    boot.geometry("800x800")
    boot.minsize(width=700,height=700)
    root.destroy()





headingFrame1 = Frame(root,bg="white",bd=8)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n XXX LIBRARY", bg='black', fg='white', font=('Courier',22,"bold"))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)



btn1 = Button(root,text="View/Update Member Details",bg='black', fg='white',bd=4,font=('Courier New',15,'bold'),command=members) #, command=addBook)
btn1.place(relx=0,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Add Member",bg='black', fg='white',bd=4,font=('Courier New',15,'bold'), command=Add)
btn2.place(relx=0.,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="Book List",bg='black', fg='white',bd=4,font=('Courier New',15,'bold'),command=Booklist)
btn3.place(relx=0,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book",bg='black', fg='white',bd=4,font=('Courier New',15,'bold'),command =issue)
btn4.place(relx=0,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="View Book Status",bg='black', fg='white',bd=4,font=('Courier New',15,'bold'),command =status)
btn5.place(relx=0,rely=0.8, relwidth=0.45,relheight=0.1)

btn6= Button(root,text="Return Book",bg='black', fg='white',bd=4,font=('Courier New',15,'bold'),command =returns)
btn6.place(relx=0,rely=0.9, relwidth=0.45,relheight=0.1)
root.mainloop()

