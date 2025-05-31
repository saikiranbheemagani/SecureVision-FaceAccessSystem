
import sys
import mysql.connector
import os
from tkinter import *
from tkinter import messagebox

def validate():
    global un
    global ps
    un =  E1.get()
    ps = E2.get()
    mydb = mysql.connector.connect(host='localhost', user='root', password='password', database='world', auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()
    mycursor.execute('SELECT u,p FROM admin')
    result = mycursor.fetchall()
    result = dict(result)
    if un in result.keys() and ps in result.values():
        return True
    else:
        return False

def end():
    top.destroy()

def stop():
    messagebox.showerror(' ', ' Access Denied' + "\n" + ' Please Sign in with Valid Credentials')

def scan():
    if validate():
        end()
        os.system('python create_data.py')
    else:
        stop()

def callfr1():
    if validate():
        end()
        os.system('python camera_select.py')
    else:
        stop()

def callreg():
    end()
    os.system('python register.py')

top = Tk()
top.title("Home Page")
top.geometry("700x320")

L = Label(top, text="Dynamic Human Authentication System", font="Helvetica 25", fg="black")
L.pack()
Label().pack()

L1 = Label(top, text="Enter Username", font="Helvetica 10 ", fg="black")
L1.pack()
E1 = Entry(top)
E1.pack()

L2 = Label(top, text="Enter Password", font="Helvetica 10 ", fg="black")
L2.pack()
E2 = Entry(top, show="*")
E2.pack()

Label().pack()

B1 = Button(top, text="Sign in To Scan a Person", command=scan)
B1.pack()

B2 = Button(top, text="Scan The Locality", command=callfr1)
B2.pack()

B3 = Button(top, text="Register A New Admin", command=callreg)
B3.pack()

B4 = Button(top, text="Exit", command=end)
B4.pack()

top.mainloop()
