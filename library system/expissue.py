from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector


con = mysql.connector.connect( host="localhost",user="root",password='tarun12345',database='library')
cur = con.cursor()
cur = con.cursor(buffered=True)

#issueTable='books_issued'
bookTable='books'

allBid=[]

def issue():
    
    global issueBtn,labelFrame,lb1,lb2,inf1,inf2,quitBtn,root,Canvas1,status
    
    bid = inf1.get()
    mem = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    #lb2.destroy()
    inf1.destroy()
    inf2.destroy()
    
    
    extractBid = "select bid from "+bookTable
    
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])
        
        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    #issueSql = "insert into "+issueTable+" values ('"+bid+"','"+issueto+"')"
    #show = "select * from "+issueTable
    
    updateStatus = "update "+bookTable+" set status = 'issued',memname='"+mem+"' where bid = '"+bid+"'"
    try:
        if bid in allBid and status == True:
            #cur.execute(issueSql)
            #con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Issued Successfully")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message',"Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")

    print(bid)
    #print(issueto)
    
    allBid.clear()



def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
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
    #Canvas1.config(bg="#D6ED17")
    #Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="white",bd=8)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    
    #Issue Button
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="BACK",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
