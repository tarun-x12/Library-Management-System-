from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector



con = mysql.connector.connect( host="localhost",user="root",password='tarun12345',database='library')
cur = con.cursor()
cur = con.cursor(buffered=True)

mem="member"

def deleteMember():
    memid=memInfo1.get()
        
    
    deleteSql = "delete from "+mem+" where MID = '"+memid+"'"

    try:
        cur.execute(deleteSql)
        con.commit()
        

        messagebox.showinfo('Success',"Member Record Deleted Successfully")

    except:
        messagebox.showinfo("Please check Mmeber ID")
    
    #print(bid)

    memInfo1.delete(0, END)
    root.destroy()

    
def deletem(): 
    
    global memInfo1,memInfo2,memInfo3,memInfo4,Canvas1,con,cur,mem,root
    
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




        
    headingFrame1 = Frame(root,bg="purple",bd=10)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Member", bg='white', fg='purple', font=('Courier',30,'bold'))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    
    lb2 = Label(labelFrame,text="Member ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.5)
        
    memInfo1 = Entry(labelFrame)
    memInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    

    addBtn = Button(root,text="DELETE",bg='white', fg='purple',command=deleteMember)
    addBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="BACK",bg='white', fg='purple', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
       
