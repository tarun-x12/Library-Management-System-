from tkinter import *
from PIL import ImageTk,Image 
import mysql.connector
from tkinter import messagebox
from expaddbook import *
from expdelete import *
from expview import *
from expissue import *
from expreturn import *
from expmember import *
from expmemadd import *
from expviewmem import *
from expmemdelete import *

con = mysql.connector.connect(host="localhost",user="root",password='tarun12345',database='library')


cursor = con.cursor()



root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("800x800")



same=True

n=1.75

background_image =Image.open("C:/Users/TEAM/Pictures/image1.jpg")

[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n)
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight))
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(400,400,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)
Canvas1.create_text(400,150,text="NATIONAL LIBRARY \n     CHENNAI",font=("CourieR",55,'bold'),fill="black")
                    




btn1= Button(root,text="Issue Book",bg='purple', fg='white',font=('Courier New',15,'bold'),command=issueBook)
btn1.place(relx=0,rely=0.5, relwidth=0.45,relheight=0.1)

btn2 = Button(root,text="Return Book",bg='white', fg='purple',font=('Courier New',15,'bold'),command=returnBook)
btn2.place(relx=0.5,rely=0.5, relwidth=0.45,relheight=0.1)

btn3 = Button(root,text="Add a Book ",bg='white', fg='purple',font=('Courier New',15,'bold'),command=addBook)
btn3.place(relx=0,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="View List of Books",bg='purple', fg='white',font=('Courier New',15,'bold'),command=View)
btn4.place(relx=0,rely=0.7, relwidth=0.45,relheight=0.1)

btn5 = Button(root,text="Delete a Book",bg='purple',fg='white',font=('Courier New',15,'bold'),command=delete)
btn5.place(relx=0.5,rely=0.6, relwidth=0.45,relheight=0.1)

btn6 = Button(root,text="Add Members",bg='purple',fg='white',font=('Courier New',15,'bold'),command=addmember)
btn6.place(relx=0.5,rely=0.8, relwidth=0.45,relheight=0.1)

btn7=Button(root,text="View Members",bg='white',fg='purple',font=('Courier New',15,'bold'),command=viewmem)
btn7.place(relx=0.5,rely=0.7, relwidth=0.45,relheight=0.1)

btn8=Button(root,text="Delete Members",bg='white',fg='purple',font=('Courier New',15,'bold'),command=deletem)
btn8.place(relx=0,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()




