from tkinter import *
import tkinter.messagebox as tm


class Interface:
    def __init__(self, root):

        self.frameButton=Frame(root)
        self.frameButton1=Frame(root)

        root.iconbitmap(r'11.ico')
        root.title('Python User Interface')
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        width = 350
        height = 200
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        root.resizable(0, 0)
        Label (text ="LOGIN PAGE", bg ="green",fg="brown",width="600",height="1",font=("tahoma",16)).pack() 
        self.label_username = Label(text="Username :")
        self.label_password = Label(text="Password :")
        self.entry_username = Entry()
        self.entry_password = Entry(show="*")
        self.label_username.place(x=80,y=58)
        self.label_password.place(x=80,y=87)
        self.entry_username.place(x=170, y=60)
        self.entry_password.place(x=170, y=90)

        self.makeButton()

    def makeButton(self):
        self.checkbox = Checkbutton(self.frameButton, text="Keep me logged in").grid(row=0, column=1)
        self.frameButton.place(x=90, y=115)

        self.logbtn = Button(self.frameButton1, text="Login", command=self._login_btn_clicked).grid(row=0, column=1)
        self.frameButton1.place(x=150, y=155)


    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_username.get()
        password = self.entry_password.get()

        # print(username, password)

        if username == "user1" and password == "12345678":
            tm.showinfo("Login info", "Welcome John")
        else:
            tm.showerror("Login error", "Incorrect username")

class LoginIn(Interface):
    """docstring for LoginIn"""
    pass
        

root = Tk()
Interface(root)
root.mainloop()