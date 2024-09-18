from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector


def memregister():
    root=Tk()
    mid = bookInfo1.get()
    name = bookInfo2.get()
    phone = bookInfo3.get()
    #status = bookInfo4.get()
    #status = status.lower()
    
    insertmem = "insert into member values('"+mid+"','"+name+"','"+phone+"')"#'"+status+"')"
    #try:
    cur.execute(insertmem)
    con.commit()
    messagebox.showinfo('Success',"member added successfully")
    #except:
        #messagebox.showinfo("Error","Can't add data into Database")
    
    
    root.destroy()

def addmember(): 
    
    global bookInfo1 ,bookInfo2, bookInfo3,Canvas1,con,cur,root,memtable
    
    root = Toplevel()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("800x800")


    

    con = mysql.connector.connect( host="localhost",user="root",password='tarun12345',database='library')
    cur = con.cursor()

    memtable="member"
    #bookTable = "books"


    same=True
    n=2

    background_image =Image.open("C:/Users/TEAM/Pictures/image1.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 
        
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(background_image)
    Canvas1 = Canvas(root)
    Canvas1.create_image(400,400,image = img)      
    Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)

    

        
    headingFrame1 = Frame(root,bg="purple",bd=10)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Member", bg='white', fg='purple', font=('Courier',30,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)





    

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    
    lb1 = Label(labelFrame,text="MemID : ", bg='black', fg='white',font=('Courier'))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    
    lb2 = Label(labelFrame,text="Name : ", bg='black', fg='white',font=('Courier'))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    
    lb3 = Label(labelFrame,text="Phone : ", bg='black', fg='white',font=('Courier'))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
        
    
    #lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='black', fg='white',font=('Courier',8,'bold'))
    #lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    #bookInfo4 = Entry(labelFrame)
    #bookInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

    
    
    SubmitBtn = Button(root,text="ADD",bg='white', fg='purple',command=memregister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    
    quitBtn = Button(root,text="BACK",bg='white', fg='purple', command=root.destroy)
    quitBtn.place(relx=0.58,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()


