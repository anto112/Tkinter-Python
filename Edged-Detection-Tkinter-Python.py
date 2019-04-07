import tkinter as Tk
from tkinter import messagebox 
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import cv2
import numpy as np

class LoginPage:
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("Python")
        self.frame = Tk.Frame(parent)
        self.frame.pack()
        self.frameButton=Tk.Frame(parent)
        self.frameButton1=Tk.Frame(parent)
        self.frameButton2=Tk.Frame(parent)

        Tk.Label (text ="LOGIN PAGE", bg ="green",fg="brown",width="350",height="1",font=("tahoma",16)).pack() 
        self.label_username =Tk.Label(text="Username :")
        self.label_password =Tk.Label(text="Password :")
        self.entry_username =Tk.Entry()
        self.entry_password =Tk.Entry(show="*")
        self.label_username.place(x=80,y=55)
        self.label_password.place(x=80,y=85)
        self.entry_username.place(x=170, y=58)
        self.entry_password.place(x=170, y=88)
        Tk.Label (text ="", bg ="green",fg="brown",width="350",height="1",font=("tahoma",16)).place(x=0, y=185)

        self.makeButton()

    def makeButton (self):
        self.checkbox = Tk.Checkbutton(self.frameButton, text="Keep me logged in").grid(row=0, column=1)
        self.frameButton.place(x=90, y=110)
        self.logbtn = Tk.Button(self.frameButton1, text="Login",command=self.logInBttn).grid(row=0, column=1)
        self.frameButton1.place(x=130, y=145)
        self.Quitbutton = Tk.Button(self.frameButton2, text="exit",command=self.quit).grid(row=0, column=1)
        self.frameButton2.place(x=220, y=145)

    def hide(self):
        """"""
        self.root.withdraw()
 
    def logInBttn(self):
        """"""
        username = self.entry_username.get()
        password = self.entry_password.get()
        if username == "1" and password == "1":
            self.hide()
            subFrame = MainPage(self)
        else:
            messagebox.showerror("Login error", "Incorrect username")

    def quit(self):
        """"""
        answer = messagebox.askquestion('', "Are you sure want to exit ?" )
        if answer == 'yes':
            self.root.destroy()
        elif answer == 'no':  # 'no'
            pass

    def logOut(self):
        """"""
        self.root.update()
        self.entry_username.delete(0, 'end')
        self.entry_password.delete(0, 'end')
        self.root.deiconify()

class MainPage(Tk.Toplevel):
    """"""
    def __init__(self, page):
        """Constructor"""
        Tk.Toplevel.__init__(self)
        self.mainPageFrame = page             
        self.iconbitmap(r'11.ico')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width = 750
        height = 450
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))
        self.resizable(0, 0)
        self.title("MainPage")
        Tk.Label (self,text ="IMAGE PROCESSING", bg ="grey",fg="black",width="600",height="1",font=("calibri",20)).pack() 
        Tk.Label (self,text ="Original Image",fg="red",font=("tahoma",14)).place(x=120,y=55)
        Tk.Label (self,text ="Result",fg="blue",font=("tahoma",14)).place(x=520,y=55)
        Tk.Label (self,text ="compiled by : Haryanto (M07158031)",bg ="grey",
            fg="red",width="750",height="1",font=("tahoma",9)).place(x=0,y=440)
        self.cvs=Tk.Canvas(self, width=350, height=250,bg='white')
        self.cvs.pack
        self.canvas1=Tk.Canvas(self, width=350, height=250, bg='white')
        self.canvas1.pack

        self.ButtonInPage()

    def ButtonInPage (self):
        Tk.Button(self, text="Logout",command=self.backLoginPage).place(x=620, y=405)
        Tk.Button(self,relief='raised', text="Load Media", command=self.browseButton).place(x=75, y=375)
        Tk.Button(self,relief='raised', text="New Image", command=self.openCAM).place(x=225, y=375)
        Tk.Button(self,relief='raised', text="exit", command=self.quit).place(x=685, y=405)
        Tk.Button(self,relief='raised', text="Edged Detect", command=self.edgeDetection).place(x=500, y=375)
 
    def backLoginPage(self):
        """"""
        self.destroy()
        self.mainPageFrame.logOut()

    def browseButton(self):
        try :
            tipeFile = (('image files', '*.jpg'), ('png files', '*.png'), ('all files', '*'))
            self.path = filedialog.askopenfilename(filetypes=tipeFile)
            global img
            self.img = cv2.imread(self.path)
            self.img1 = cv2.cvtColor(self.img,cv2.COLOR_BGR2RGB)
            self.img1 = Image.fromarray(np.array(self.img1).copy())
            self.img1.thumbnail((350, 260))
            self.img1 = ImageTk.PhotoImage(self.img1)
            self.cvs=Tk.Canvas(self, width=350, height=250)
            self.cvs.create_image(0,0,image=self.img1, anchor='nw')
            self.cvs.place(x=20,y=100)
        except :
            messagebox.showwarning("error","wrong format media, please check again")

    def edgeDetection(self):
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.gray = cv2.GaussianBlur(self.gray, (5, 5), 0)
        self.gray1 = cv2.GaussianBlur(self.gray, (7, 7), 0)
        self.edged = cv2.Canny(self.gray, 50, 200)
        self.edged = cv2.dilate(self.edged, None, iterations=1)
        self.edged = cv2.erode(self.edged, None, iterations=1)      
        self.edged = Image.fromarray(np.array(self.edged).copy())
        self.edged.thumbnail((350, 260))
        self.img2 = ImageTk.PhotoImage(self.edged)
        self.canvas1=Tk.Canvas(self, width=355, height=250)
        self.canvas1.create_image(0,0,image=self.img2, anchor='nw')
        self.canvas1.place(x=380,y=100)

    def openCAM(self):
        print("Still in development now !!!")
        
    def quit(self):
        answer = messagebox.askquestion('', "Are you sure want to exit ?" )
        if answer == 'yes':
            self.destroy()
        elif answer == 'no':  # 'no'
            pass

def main ():
    root = Tk.Tk()
    root.bind('<Escape>', lambda e: root.quit())
    root.iconbitmap(r'1123.ico')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = 350
    height = 200
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    root.resizable(0, 0)
    app = LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
