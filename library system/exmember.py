from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector



con = mysql.connector.connect( host="localhost",user="root",password='tarun12345',database='library')
cur = con.cursor()
cur = con.cursor(buffered=True)

