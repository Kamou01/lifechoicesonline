from tkinter import *
from tkinter import messagebox
import rsaidnumber
import mysql.connector

window = Tk()
window.geometry("600x400")
window.title("Admin")
window.config(bg="green")


def sign_in():
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="lifechoices",
    password="@Lifechoices1234",
    auth_plugin="mysql_native_password",
    database="lifechoicesonline"
                                )
    mycursor = mydb.cursor()

    sql = "INSERT INTO admin (name, id_number) VALUES (%s, %s)"
    val = (e1.get(), str(rsaidnumber.parse(e2.get())))
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


header = Label(window, text="Enter your details here:", fg="white", bg="green", font="Arial 15")
header.place(x=200, y=2)


lb1 = Label(window, text="Enter your name:", fg="white", bg="green", font="Arial 12")
lb1.place(x=2, y=70)
e1 = Entry(state="normal", bg="white", fg="black", font="Arial 12")
e1.place(x=200, y=70)


lb3 = Label(window, text="Enter your id number:", fg="white", bg="green", font="Arial 12")
lb3.place(x=2, y=150)
e2 = Entry(state="normal", bg="white", fg="black", font="Arial 12")
e2.place(x=200, y=150)


login_btn = Button(window, text="Sign in", fg="white", bg="green", font="Arial 12", command=sign_in)
login_btn.place(x=450, y=360)

window.mainloop()
