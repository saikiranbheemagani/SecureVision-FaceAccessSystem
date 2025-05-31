from tkinter import *
from tkinter import messagebox
import mysql.connector

def store():
    global n, c, e, u, p
    n = E1.get()
    c = E2.get()
    e = E3.get()
    u = E4.get()
    p = E5.get()
    p1 = E6.get()

    if (len(n) and len(c) and len(e) and len(u) and len(p) and len(p1)) != 0:
        if p == p1:
            mydb = mysql.connector.connect(
                host='localhost', user='root', password='password', database='world', auth_plugin='mysql_native_password')
            mycursor = mydb.cursor()

            sql = """INSERT INTO register(n,num,em,u,p) VALUES (%s,%s,%s,%s,%s)"""
            d = (n, c, e, u, p)
            mycursor.execute(sql, d)
            # sql = """INSERT INTO register(username, num, email, u, p) VALUES (%s, %s, %s, %s, %s)"""
            # d = (n, c, e, u, p)
            # mycursor.execute(sql, d)
            sql1 = """INSERT INTO admin(u,p) VALUES(%s,%s)"""
            d1 = (u, p)
            mycursor.execute(sql1, d1)

            mycursor.close()
            mydb.commit()
            mydb.close()

            top.destroy()
        else:
            messagebox.showerror(' ', 'Passwords do not match')
    else:
        messagebox.showerror(' ', 'Please provide complete information')

top = Tk()
top.geometry("500x300")

L1 = Label(top, text="Name of Admin")
L1.pack()
E1 = Entry(top)
E1.pack()

L2 = Label(top, text="Contact Number")
L2.pack()
E2 = Entry(top)
E2.pack()

L3 = Label(top, text="e-Mail")
L3.pack()
E3 = Entry(top)
E3.pack()

L4 = Label(top, text="Username")
L4.pack()
E4 = Entry(top)
E4.pack()

L5 = Label(top, text="Password")
L5.pack()
E5 = Entry(top, show="*")
E5.pack()

L6 = Label(top, text="Confirm Password")
L6.pack()
E6 = Entry(top, show="*")
E6.pack()

B = Button(top, text='Register', command=store)
B.pack(padx=5, pady=5)

top.mainloop()
