from tkinter import *
from tkinter import messagebox
import rsaidnumber
import mysql.connector

window = Tk()
window.geometry("600x300")
window.title("Login")
window.config(bg="green")


def login_id():
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="lifechoices",
    password="@Lifechoices1234",
    auth_plugin="mysql_native_password",
    database="lifechoicesonline"
                                )
    mycursor = mydb.cursor()

    sql = "INSERT INTO login (Name, Id_number) VALUES (%s, %s)"
    val = (e1.get(), str(rsaidnumber.parse(e2.get())))
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


header = Label(window, text="Login: ", fg="white", bg="green", font="Arial 15")
header.place(x=270, y=2)

lb1 = Label(window, text="Enter your name: ", fg="white", bg="green", font="Arial 12")
lb1.place(x=2, y=70)
e1 = Entry(state="normal", bg="white", fg="black", font="Arial 12")
e1.place(x=150, y=70)

lb2 = Label(window, text="Enter your Id: ", fg="white", bg="green", font="Arial 12")
lb2.place(x=2, y=100)
e2 = Entry(state="normal", bg="white", fg="black", font="Arial 12")
e2.place(x=150, y=100)

login_btn = Button(window, text="Login", fg="white", bg="green", command=login_id)
login_btn.place(x=270, y=200)

window.mainloop()
