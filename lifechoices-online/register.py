from tkinter import *
from tkinter import messagebox
import rsaidnumber
import mysql.connector

window = Tk()
window.geometry("600x400")
window.title("Register")
window.config(bg="green")


def register_id():
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="lifechoices",
    password="@Lifechoices1234",
    auth_plugin="mysql_native_password",
    database="lifechoicesonline"
                                )
    mycursor = mydb.cursor()

    sql = "INSERT INTO register_user (Name, Surname, Id_number, NoK_name, NoK_number) VALUES (%s, %s, %s, %s, %s)"
    val = (e1.get(),  e2.get(),  str(rsaidnumber.parse(e3.get())), e4.get(), e5.get())
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


def delete_id():
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="lifechoices",
    password="@Lifechoices1234",
    auth_plugin="mysql_native_password",
    database="lifechoicesonline"
                                )
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM register_user")

    #   Where the the id in the database is chosen to delete the users info.
    for i in cursor:
        if e3.get() == i[3]:
            delete_sql_nok = "DELETE FROM register_user WHERE nok_id='" + e3.get() + "'"
            cursor.execute(delete_sql_nok)
            mydb.commit()
            messagebox.showinfo("Deleted!", "You Have Deleted The Record")
        else:
            messagebox.showerror("Check Your Details", "Check Your Details")
            mydb.commit()


header = Label(window, text="Enter your details here:", fg="white", bg="green", font="Arial 15")
header.place(x=200, y=2)


lb1 = Label(window, text="Enter your Name:", fg="white", bg="green", font="Arial 12")
lb1.place(x=2, y=70)
e1 = Entry(state="normal", bg="white", fg="black", font="Arial 12")
e1.place(x=200, y=70)

lb2 = Label(window, text="Enter your Surname:", fg="white", bg="green", font="Arial 12")
lb2.place(x=2, y=110)
e2 = Entry(state="normal", bg="white", fg="black", font="Arial 12")
e2.place(x=200, y=110)

lb3 = Label(window, text="Enter your Id number:", fg="white", bg="green", font="Arial 12")
lb3.place(x=2, y=150)
e3 = Entry(state="normal", bg="white", fg="black", font="Arial 12")
e3.place(x=200, y=150)


next_of_kin = Label(window, text="Enter your Next Of Kin(NOK)'s details", fg="white", bg="green", font="Arial 15")
next_of_kin.place(x=150, y=250)

lb4 = Label(window, text="Enter your NOK name:", fg="white", bg="green", font="Arial 12")
lb4.place(x=2, y=300)
e4 = Entry(state="normal", bg="white", fg="black", font="Arial 12")
e4.place(x=200, y=300)

lb5 = Label(window, text="Enter your NOK contact number:", fg="white", bg="green", font="Arial 12")
lb5.place(x=2, y=330)
e5 = Entry(state="normal", bg="white", fg="black", font="Arial 12")
e5.place(x=250, y=330)

register_btn = Button(window, text="Register", fg="white", bg="green", font="Arial 12", command=register_id)
register_btn.place(x=450, y=360)

delete_btn = Button(window, text="Delete", fg="white", bg="green", font="Arial 12", command=delete_id)
delete_btn.place(x=350, y=360)

window.mainloop()
