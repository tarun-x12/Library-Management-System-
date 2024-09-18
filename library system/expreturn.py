from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector


con = mysql.connector.connect( host="localhost",user="root",password='tarun12345',database='library')
cur = con.cursor()
cur = con.cursor(buffered=True)

#issueTable = "books_issued" 
bookTable = "books"
allBid = []  #To store all the Book ID’S

def returnn():
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status
    check=[]
    bid = bookInfo1.get()

    extractBid = "select bid from books"
    #try:
        
    cur.execute(extractBid)
    con.commit()
    for i in cur:
        allBid.append(i[0])
        
    if bid in allBid:
        checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
        cur.execute(checkAvail)
        con.commit()
    for i in cur:
        print(i)
        check = i[0]
        print(check)
        
                
    if check == 'issued':
        status = True
    else:
        status = False

     #   else:
         #   messagebox.showinfo("Error","Book ID not present")
    #except:
        #messagebox.showinfo("Error","Can't fetch Book IDs")
    
    
    #issueSql = "delete from " where bid = '"+bid+"'"
    
    print(bid in allBid)
    #print(status)
    updateStatus = "update "+bookTable+" set status = 'avail',memname=' ' where bid = '"+bid+"'"
    #try:
    if bid in allBid and status == True:
        #cur.execute(issueSql)
        #con.commit()
        cur.execute(updateStatus)
        con.commit()
        messagebox.showinfo('Success',"Book Returned Successfully")

    else:
        allBid.clear()
        messagebox.showinfo('Message',"Please check the book ID")
        root.destroy()
        return
   # except:
    #    messagebox.showinfo("Search Error","The value entered is wrong, Try again")
   
    
    allBid.clear()
    root.destroy()

def returnBook(): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Toplevel()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("800x800")

    same=True

    n=2

    # Adding a background image
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
    
    #Canvas1.config(bg="#006B38")
    #Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="white",bd=8)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="BACK",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
