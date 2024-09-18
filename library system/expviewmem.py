from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector



con = mysql.connector.connect( host="localhost",user="root",password='tarun12345',database='library')
cur = con.cursor()
cur = con.cursor(buffered=True)
bookTable ="books"

def viewmem():
      
    root = Toplevel()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("800x800")

    
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




    #Canvas1 = Canvas(root) 
    #Canvas1.config(bg="#12a4d9")
    #Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="purple",bd=10)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Members", bg='white', fg='purple', font = ('Courier',30,'bold'))

    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-10s%-40s%-30s"%('MID','NAME','PHONE'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text = "----------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    
    memBooks = "select * from member"
    #try:
    
    cur.execute("SELECT * FROM member")
    con.commit()


    for i in cur:
        Label(labelFrame,text="%-10s%-30s%-30s"%(i[0],i[1],i[2]) ,bg='black', fg='white').place(relx=0.07,rely=y)
        y += 0.1
    #except:
        
        #messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Back",bg='white', fg='purple', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    
    root.mainloop()
