# import tkinter as tk
# import tkinter.messagebox as tm
# from tkinter import *
# import sys

# FontType = ("Times", "12", "bold italic")

# class Interface: 
   
#     def __init__(self,root):
#         frame = Frame(root)
#         frame.pack(side = "top", fill = "both", expand = True)
#         frame.grid_rowconfigure(0,weight = 1)
#         frame.grid_columnconfigure(0,weight = 1)

#         self.frames = {}

#         frame = LoginPage(frame,self)
#         self.frames[LoginPage] = frame
#         frame.grid(row = 0,column = 0,sticky = "nsew")

#         self.show_frame(LoginPage)

#     def show_frame(self,cont):

#         frame = self.frames[cont]
#         frame.tkraise()    



# class LoginPage(Interface):

#     def __init__(self,parent,controller):
#         tk.Frame.__init__(self,parent)
#         usr_login = StringVar()
#         pwd_login = StringVar()
#         userLabel = tk.Label(self,text = "Name",font = FontType )
#         passwordLabel = tk.Label(self,text = "Password", font = FontType)

#         userEntry = tk.Entry(self, textvariable = usr_login, bd=5)
#         passwordEntry = tk.Entry(self, textvariable=pwd_login,bd=5,show = "*")

#         submitButton = tk.Button(self,text = "Login",command = lambda: loginValidate(usr_login.get(),pwd_login.get()))
#         quitButton = tk.Button(self,text = "Quit",command =lambda: app.destroy)

#         userLabel.grid(row = 0,sticky = "E",padx =10,pady =10)
#         passwordLabel.grid(row =1,sticky = "E",padx =10,pady =10)
#         userEntry.grid(row=0,column=1,padx =10,pady =10)
#         passwordEntry.grid(row=1,column=1,padx =10,pady =10)
#         submitButton.grid(row =2,column =1,padx =10,pady =10)
#         quitButton.grid(row=2,column=2,padx =10,pady =10)

# def loginValidate(user,pwd):
#     if(user == "yogesh" and pwd == "123456"):
#         print("1")
#     else:
#         print("2")
#         tm.showerror("Login error", "Incorrect username or password")
        
# root = Tk()
# Interface(root)
# root.mainloop()

import tkinter as tk

class MainWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.olFrame = tk.LabelFrame(text = 'Initial Frame', bg = 'grey')
        self.olFrame.grid(column = 0, row = 0, sticky = 'w')

        self.simpleButton = ButtonField(self.olFrame, text = "Press Me",bg= "green"
                                     ,command = ButtonField(self).pressMe)
        self.simpleButton.grid(column = 0, row = 0)

class ButtonField(tk.Button):
    def __init__(self, parent, *args, **kwargs):
        tk.Button.__init__(self, parent, *args, **kwargs)
        self.parent = parent

    def pressMe(self):
        print ("In Press Me Method")
        self.configure(text = "Pressed Now", background = "yellow")
        #self.parent.configure(self, text = "Pressed Now", background = "yellow")  #returns TclError: unknow option "-text"

root = tk.Tk()
root.geometry('500x400')
root.title('Test GUI')
root.configure(background = "black")

a = MainWindow(root)
root.mainloop()