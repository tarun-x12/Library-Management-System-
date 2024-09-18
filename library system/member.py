


#def members():
from tkinter import *
from tkinter.ttk import *
boot=Tk()
boot.title("Members")
boot.geometry("800x800")
boot.configure(bg='black')
boot.minsize(width=700,height=700)

bg=PhotoImage(file="C:/Users/TEAM/Pictures/xxx.png")

my_label=Label(boot,image=bg)
my_label.place(x=1,y=1)

def goback():
    boot.destroy()
    import main



but1=Button(boot,text="BACK",command=goback)#,bg='black',fg='white',bd=4,font=('Courier New',16))
but1.place(relx=0,rely=0,relwidth=0.1,relheight=0.05)

boot.mainloop()
