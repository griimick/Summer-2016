try:
        # python2
    import tkinter as tk
except ImportError:
        # python3
    import Tkinter as tk

# Python Imaging Library to process images
from connection import *
from src.MainView import * 
import bcrypt
from PIL import ImageTk, Image
from src.center import center
# from MainView import * 
# from connection import *

import tkMessageBox


# the main LoginWindow Layout Class
# it will be the layout for the top level login window


class LoginWin(tk.Toplevel):
    def __init__(self, root):
        tk.Toplevel.__init__(self)
        # instance variables
        self.var_showpass = tk.IntVar()
        self.root = root
        self.var_maxf = 3
        self.var_status = "Ready, Enter userID and password to login"
        self.var_imagePath = "images/logo.png"

        self.title("HRDB Login")
        self.resizable(
            width=False,
            height=False,
        )

        # the main container frame
        self.mainContainer = tk.Frame(self)
        self.mainContainer.configure(
            height=150,
            width=450,
        )
        self.mainContainer.pack()

        # the userID label
        self.label_userID = tk.Label(self.mainContainer)
        self.label_userID.configure(
            text="EmployeeID",
        )
        self.label_userID.pack()
        self.label_userID.place(
            x=136,
            y=20,
            width=69,
            height=21,
        )

        # the password Label
        self.label_password = tk.Label(self.mainContainer)
        self.label_password.configure(
            text="Passowrd",
        )
        self.label_password.pack()
        self.label_password.place(
            x=147,
            y=44,
            width=59,
            height=21,
        )

        # the userID entry field
        self.entry_userID = tk.Entry(self.mainContainer)
        self.entry_userID.configure(
            background="white",
        )
        self.entry_userID.pack()
        self.entry_userID.place(
            x=209,
            y=20,
            width=214,
            height=20,
        )
        # let the cursor appear on the userID entry
        self.entry_userID.focus_set()

        # the password entry field
        self.entry_password = tk.Entry(self.mainContainer)
        self.entry_password.configure(
            background="white",
            show="*",
        )
        self.entry_password.pack()
        self.entry_password.place(
            x=209,
            y=45,
            width=214,
            height=20,
        )

        # the HRDB logo label
        img = ImageTk.PhotoImage(Image.open(self.var_imagePath))
        self.label_logo = tk.Label(self.mainContainer)
        self.label_logo.configure(
            image=img,
            bg="red",
        )
        self.label_logo.image = img
        self.label_logo.pack()
        self.label_logo.place(
            x=10,
            y=10,
            width=114,
            height=101,
        )

        # the showpassword checkbox
        self.checkb_showPass = tk.Checkbutton(self.mainContainer)
        self.checkb_showPass.configure(
            text="Show Password",
            variable=self.var_showpass,
            command=self.check_var_showpass,
        )
        self.checkb_showPass.pack()
        self.checkb_showPass.place(
            x=206,
            y=77,
            width=110,
            height=25,
        )

        # the Login Button
        self.button_login = tk.Button(self.mainContainer)
        self.button_login.configure(
            text="Login",
            command=self.check_password,
        )
        self.button_login.pack()
        self.button_login.place(
            x=326,
            y=78,
            width=97,
            height=24,
        )

        # Bind the Enter Button on the keyboard to submit when pressed
        self.entry_password.bind('<Return>', self.check_clickpassword)

        # the status frame
        self.frame_status = tk.Frame(self.mainContainer)
        self.frame_status.configure(
            relief=tk.GROOVE,
            borderwidth=2,
        )
        self.frame_status.pack()
        self.frame_status.place(
            x=3,
            y=122,
            width=444,
            height=25,
        )

        # the status frame text
        self.text_status = tk.Text(self.frame_status)
        self.text_status.configure(
            background=self.frame_status.cget('bg'),
            font=self.label_password.cget('font'),
            borderwidth=0,
            state=tk.DISABLED,
        )
        self.change_status("Enter userID and password to login (Attempt 1/3)")
        self.text_status.pack()
        self.text_status.place(
            x=4,
            y=2,
            width=434,
            height=18,
        )

        # Class Funcitons

        # Check password visibility checkbox
    def check_var_showpass(self):
        # print(self.var_showpass.get())
        if(self.var_showpass.get()):
            self.entry_password.configure(show="")
            print("Password Visible")
        else:
            self.entry_password.configure(show="*")
            print("Password Hidden")

    # Change the status frame text
    def change_status(self, text):
        self.var_status = text
        self.text_status.configure(state=tk.NORMAL)
        self.text_status.delete(1.0, tk.END)
        self.text_status.insert(1.0, self.var_status)
        self.text_status.configure(state=tk.DISABLED)

    # Get passwords from passdb table in database
    def get_passwords(self):
        cursor = db.cursor()
        sql = "SELECT CAST(`empdb_empID` AS char), `password` FROM `passwords`"
        cursor.execute(sql)
        passwords = cursor.fetchall()
        return passwords

    def get_usernames(self):
        cursor = db.cursor()
        sql="SELECT `empdb_empID` FROM `passwords`"
        cursor.execute(sql)
        usernames =[item[0] for item in cursor.fetchall()]
        return usernames

    def check_clickpassword(self, failures):
        self.check_password()

    # Authentication function
    def check_password(self, failures=[]):
        print(self.entry_userID.get(), self.entry_password.get())

        usernames = self.get_usernames()
        passwords = self.get_passwords()
        print(usernames)
        print(passwords)
        userID = self.entry_userID.get()
        password = self.entry_password.get()
        if int(userID) in usernames:
            #validate password
            if(self.check_pass(userID,password)):
                tkMessageBox.showinfo("Status", "Logged in")
                self.destroy()
                self.root = MainView(userID)
                center(self.root)
                self.root.deiconify()
                return
            else:
                failures.append(1)
                if sum(failures) >= self.var_maxf:
                    self.destroy()
                    tkMessageBox.showerror('Error', 'Unauthorized login attempt')
                else:
                    print('Try again. Attempt %i/%i' %
                          (sum(failures) + 1, self.var_maxf))
                    self.change_status('Try again (Attempt %i/%i)' %
                                       (sum(failures) + 1, self.var_maxf))

        failures.append(1)
        if sum(failures) >= self.var_maxf:
            self.destroy()
            tkMessageBox.showerror('Error', 'Unauthorized login attempt')
        else:
            print('Try again. Attempt %i/%i' %
                  (sum(failures) + 1, self.var_maxf))
            self.change_status('Try again (Attempt %i/%i)' %
                               (sum(failures) + 1, self.var_maxf))


    def check_pass(self,id,password):
        cursor = db.cursor()
        sql = "SELECT password FROM `passwords` WHERE `empdb_empID` = %s"
        cursor.execute(sql,id)
        hashed = cursor.fetchone()[0]
        print(password + " >> " + hashed)
        if bcrypt.hashpw(password, hashed) == hashed:
            print("It Matches!")
            return True
        else:
            print("It Does not Match :(")
            return False




    


