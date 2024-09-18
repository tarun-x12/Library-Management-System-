import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="tarun12345",database="db")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE books(BOOK_ID char(10) PRIMARY KEY, TITLE VARCHAR(50) NOT NULL, AUTHOR CHAR(30) NOT NULL, STATUS CHAR(10) NOT NULL")
# MEM_EMAIL CHAR(100) NOT NULL,MEM_DOJ DATE NOT NULL, MEM_BK_ELG INT ,MEM_BK_AVL INT )"
