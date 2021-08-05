from tkinter import *

window = Tk()
window.geometry("600x300")
window.title("Life Choices - Online")
window.config(bg="white")


def admin_window():
    window.destroy()
    import admin


def register_window():
    window.destroy()
    import register


def login_window():
    window.destroy()
    import login


def exit_window():
    window.destroy()


label_1 = Label(window, text="Welcome to Life-Choices Academy Online", fg="white", bg="green", font="Arial 15")
label_1.place(x=120, y=40)

admin_btn = Button(window, text="Admin", fg="white", bg="green", font="Arial 12", command=admin_window)
admin_btn.place(x=150, y=150)

register_btn = Button(window, text="Register", fg="white", bg="green", font="Arial 12", command=register_window)
register_btn.place(x=250, y=150)

login_btn = Button(window, text="Login", fg="white", bg="green", font="Arial 12", command=login_window)
login_btn.place(x=350, y=150)

exit_btn = Button(window, text="Exit", fg="white", bg="green", font="Arial 12", command=exit_window)
exit_btn.place(x=500, y=250)

window.mainloop()
