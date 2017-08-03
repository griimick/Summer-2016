try:
        # python2
    import tkinter as tk
except ImportError:
        # python3
    import Tkinter as tk


import datetime
from printReport import * 
import tkMessageBox

from connection import *

# Python Imaging Library to process images

from PIL import ImageTk, Image

class MainView(tk.Tk):
    def __init__(self, empID):
        tk.Tk.__init__(self)

        self.var_photopath = "images/photo.png"
        self.var_logopath = "images/centerlogo.png"
        self.empID = empID
        self.set_layout()
        self.result = self.get_data()
        self.set_data()
        

    def set_layout(self):
        self.geometry('1008x321')
        self.title("Personal Details")
        self.resizable(
            width=False,
            height=False,
        )

        # Menu Bar
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Refresh", command=self.refresh_data)
        filemenu.add_command(label="Change Passowrd", command=self.change_pass)
        filemenu.add_command(label="Print")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="Option", menu=filemenu)
        self.config(menu=menubar)

        # Head Frame
        self.frame_head = tk.Frame(self)
        self.frame_head.configure(
            relief='groove',
            borderwidth=2,
        )
        self.frame_head.pack()
        self.frame_head.place(
            x=0,
            y=0,
            width=self.winfo_screenwidth(),
            height=60,
        )

        # Label Employee ID
        self.label_EmpID = tk.Label(self.frame_head)
        self.label_EmpID.configure(
            text='EmployeeID',
        )
        self.label_EmpID.pack()
        self.label_EmpID.place(
            x=2,
            y=5,
            width=69,
            height=21,
        )

        # Entry EmpID
        self.entry_EmpID = tk.Entry(self.frame_head)
        self.entry_EmpID.configure(

        )
        self.entry_EmpID.pack()
        self.entry_EmpID.place(
            x=70,
            y=5,
            width=74,
            height=20,
        )

        # Entry EmpName
        self.entry_EmpName = tk.Entry(self.frame_head)
        self.entry_EmpName.configure(

        )
        self.entry_EmpName.pack
        self.entry_EmpName.place(
            x=148,
            y=5,
            width=164,
            height=20,
        )

        # Label Logo
        # img2 = ImageTk.PhotoImage(Image.open(self.var_logopath))
        self.label_centerlogo = tk.Label(self.frame_head)
        self.label_centerlogo.configure(
            bg="red",
        )
        # self.label_centerlogo.image = img2
        self.label_centerlogo.pack()
        self.label_centerlogo.place(
            x=316,
            y=4,
            width=164,
            height=51,
        )

        # Label Head Date
        self.label_headdate = tk.Label(self.frame_head)
        self.label_headdate.configure(
            text='Date',
        )
        self.label_headdate.pack()
        self.label_headdate.place(
            x=481,
            y=5,
            width=34,
            height=21,
        )

        # Entry Head Date
        self.entry_headdate = tk.Entry(self.frame_head)
        self.entry_headdate.configure()
        self.entry_headdate.pack()
        self.entry_headdate.place(
            x=515,
            y=5,
            width=120,
            height=20,
        )
        self.entry_text(self.entry_headdate,
                        datetime.date.today().strftime("%d/%m/%Y"))

        # Button Head Refresh
        self.button_headrefresh = tk.Button(self.frame_head)
        self.button_headrefresh.configure(
            text='Refresh',
            command=self.refresh_data
        )
        self.button_headrefresh.pack()
        self.button_headrefresh.place(
            x=20,
            y=30,
        )

        # Button Head Print
        self.button_headprint = tk.Button(self.frame_head)
        self.button_headprint.configure(
            text="Print",
            command=self.printR
        )
        self.button_headprint.pack()
        self.button_headprint.place(
            x=80,
            y=30,
        )

        # Frame Body
        self.frame_body = tk.Frame(self)
        self.frame_body.configure(
            relief='groove',
            borderwidth=2,
        )
        self.frame_body.pack()
        self.frame_body.place(
            x=0,
            y=62,
            width=1008,
            height=260,
        )

        # Lframe Personal Details
        self.lframe_personal = tk.LabelFrame(self.frame_body)
        self.lframe_personal.configure(
            text='Personal Details',
        )
        self.lframe_personal.pack()
        self.lframe_personal.place(
            x=5,
            y=5,
            width=520,
            height=180,
        )

        # Label Personal Number
        self.label_personalno = tk.Label(self.lframe_personal)
        self.label_personalno.configure(
            text="Personal No :",
        )
        self.label_personalno.pack()
        self.label_personalno.place(
            x=4,
            y=22,
            width=94,
            height=21,
        )

        # Label Name
        self.label_name = tk.Label(self.lframe_personal)
        self.label_name.configure(
            text="Name :",
        )
        self.label_name.pack()
        self.label_name.place(
            x=25,
            y=43,
            width=84,
            height=21,
        )

        # Label Designation
        self.label_designation = tk.Label(self.lframe_personal)
        self.label_designation.configure(
            text="Designation :",
        )
        self.label_designation.pack()
        self.label_designation.place(
            x=10,
            y=64,
            width=84,
            height=21,
        )

        # Label Department
        self.label_department = tk.Label(self.lframe_personal)
        self.label_department.configure(
            text="Department :",
        )
        self.label_department.pack()
        self.label_department.place(
            x=14,
            y=85,
            width=75,
            height=21,
        )

        # Label Unit
        self.label_unit = tk.Label(self.lframe_personal)
        self.label_unit.configure(
            text="Unit :",
        )
        self.label_unit.pack()
        self.label_unit.place(
            x=55,
            y=106,
            width=34,
            height=21,
        )

        # Label EmailID
        self.label_emailid = tk.Label(self.lframe_personal)
        self.label_emailid.configure(
            text="Email id :",
        )
        self.label_emailid.pack()
        self.label_emailid.place(
            x=35,
            y=127,
            width=54,
            height=21,
        )

        # Label Pan ID
        self.label_pan = tk.Label(self.lframe_personal)
        self.label_pan.configure(
            text="Pan No :",
        )
        self.label_pan.pack()
        self.label_pan.place(
            x=283,
            y=22,
            width=74,
            height=21,
        )

        # Label Adhar ID
        self.label_adhar = tk.Label(self.lframe_personal)
        self.label_adhar.configure(
            text="Adhar No :",
        )
        self.label_adhar.pack()
        self.label_adhar.place(
            x=284,
            y=43,
            width=63,
            height=21,
        )

        # Label Mobile
        self.label_mobile = tk.Label(self.lframe_personal)
        self.label_mobile.configure(
            text="Mobile No :"
        )
        self.label_mobile.pack()
        self.label_mobile.place(
            x=279,
            y=64,
            width=68,
            height=21,
        )

        # Entry Personal Number
        self.entry_personalno = tk.Entry(self.lframe_personal)
        self.entry_personalno.configure()
        self.entry_personalno.pack()
        self.entry_personalno.place(
            x=90,
            y=22,
            width=164,
            height=20,
        )

        # Entry Name
        self.entry_name = tk.Entry(self.lframe_personal)
        self.entry_name.configure()
        self.entry_name.pack()
        self.entry_name.place(
            x=90,
            y=43,
            width=164,
            height=20,
        )

        # Entry Designation
        self.entry_designation = tk.Entry(self.lframe_personal)
        self.entry_designation.configure()
        self.entry_designation.pack()
        self.entry_designation.place(
            x=90,
            y=64,
            width=164,
            height=20,
        )

        # Entry Department
        self.entry_department = tk.Entry(self.lframe_personal)
        self.entry_department.configure()
        self.entry_department.pack()
        self.entry_department.place(
            x=90,
            y=85,
            width=164,
            height=20,
        )

        # Entry Unit
        self.entry_unit = tk.Entry(self.lframe_personal)
        self.entry_unit.configure()
        self.entry_unit.pack()
        self.entry_unit.place(
            x=90,
            y=106,
            width=164,
            height=20,
        )

        # Entry EmailID
        self.entry_emailid = tk.Entry(self.lframe_personal)
        self.entry_emailid.configure()
        self.entry_emailid.pack()
        self.entry_emailid.place(
            x=90,
            y=127,
            width=164,
            height=20,
        )

        # Entry Pan ID
        self.entry_pan = tk.Entry(self.lframe_personal)
        self.entry_pan.configure()
        self.entry_pan.pack()
        self.entry_pan.place(
            x=348,
            y=22,
            width=164,
            height=20,
        )

        # Entry Adhar ID
        self.entry_adhar = tk.Entry(self.lframe_personal)
        self.entry_adhar.configure()
        self.entry_adhar.pack()
        self.entry_adhar.place(
            x=348,
            y=43,
            width=164,
            height=20,
        )

        # Entry Mobile
        self.entry_mobile = tk.Entry(self.lframe_personal)
        self.entry_mobile.configure()
        self.entry_mobile.pack()
        self.entry_mobile.place(
            x=348,
            y=64,
            width=164,
            height=20,
        )

        # Lframe Employee Address
        self.lframe_address = tk.LabelFrame(self.frame_body)
        self.lframe_address.configure(
            text="Employee Address",
        )
        self.lframe_address.pack()
        self.lframe_address.place(
            x=530,
            y=5,
            width=310,
            height=180,
        )

        # Label Address
        self.label_address = tk.Label(self.lframe_address)
        self.label_address.configure(
            text="Address :"
        )
        self.label_address.pack()
        self.label_address.place(
            x=16,
            y=22,
            width=54,
            height=21,
        )

        # Label State
        self.label_state = tk.Label(self.lframe_address)
        self.label_state.configure(
            text="State :"
        )
        self.label_state.pack()
        self.label_state.place(
            x=32,
            y=85,
            width=38,
            height=21,
        )

        # Label Pin
        self.label_pin = tk.Label(self.lframe_address)
        self.label_pin.configure(
            text="Pin :",
        )
        self.label_pin.pack()
        self.label_pin.place(
            x=41,
            y=106,
            width=29,
            height=21,
        )

        # Entry Address
        self.entry_address = tk.Text(self.lframe_address)
        self.entry_address.configure()
        self.entry_address.pack()
        self.entry_address.place(
            x=71,
            y=22,
            width=230,
            height=62,
        )

        # Entry State
        self.entry_state = tk.Entry(self.lframe_address)
        self.entry_state.configure()
        self.entry_state.pack()
        self.entry_state.place(
            x=71,
            y=85,
            width=164,
            height=20,
        )

        # Entry pin
        self.entry_pin = tk.Entry(self.lframe_address)
        self.entry_pin.configure()
        self.entry_pin.pack()
        self.entry_pin.place(
            x=71,
            y=106,
        )

        # Frame Photo
        self.frame_photo = tk.Frame(self.frame_body)
        self.frame_photo.configure(
            relief=tk.GROOVE,
            borderwidth=2,
            )
        self.frame_photo.pack()
        self.frame_photo.place(
            x=844,
            y=5,
            width=160,
            height=160,
        )

        # Label Photo Image
        # img1 = ImageTk.PhotoImage(Image.open(self.var_photopath))
        self.label_photo = tk.Label(self.frame_photo)
        self.label_photo.configure(
            bg="black",
        )
        # self.label_photo.image = img1
        self.label_photo.pack()
        self.label_photo.place(
            x=8,
            y=20,
            width=144,
            height=121,
        )

        # Lframe Bank AC
        self.lframe_bank = tk.LabelFrame(self.frame_body)
        self.lframe_bank.configure(
            text="Employee Bank A/C Details",
        )
        self.lframe_bank.pack()
        self.lframe_bank.place(
            x=6,
            y=185,
            width=1000,
            height=70,
        )

        # Label ACno
        self.label_acno = tk.Label(self.lframe_bank)
        self.label_acno.configure(
            text="A/C No :",
        )
        self.label_acno.pack()
        self.label_acno.place(
            x=4,
            y=19,
            width=64,
            height=21,
        )

        # Label IFSC
        self.label_ifsc = tk.Label(self.lframe_bank)
        self.label_ifsc.configure(
            text="IFSC Code :"
        )
        self.label_ifsc.pack()
        self.label_ifsc.place(
            x=228,
            y=20,
            width=66,
            height=21,
        )

        # Label Branch
        self.label_branch = tk.Label(self.lframe_bank)
        self.label_branch.configure(
            text="Bank and Branch",
        )
        self.label_branch.pack()
        self.label_branch.place(
            x=461,
            y=20,
            width=104,
            height=21,
        )

        # Entry ACno
        self.enrtry_acno = tk.Entry(self.lframe_bank)
        self.enrtry_acno.configure()
        self.enrtry_acno.pack()
        self.enrtry_acno.place(
            x=62,
            y=20,
            width=164,
            height=20,
        )

        # Entry IFSC
        self.entry_ifsc = tk.Entry(self.lframe_bank)
        self.entry_ifsc.configure()
        self.entry_ifsc.pack()
        self.entry_ifsc.place(
            x=294,
            y=20,
            width=164,
            height=20,
        )

        # Entry Branch
        self.entry_branch = tk.Entry(self.lframe_bank)
        self.entry_branch.configure()
        self.entry_branch.pack()
        self.entry_branch.place(
            x=562,
            y=20,
            width=434,
            height=20,
        )

    def entry_text(self, widget, text=""):
        widget.configure(state=tk.NORMAL)
        try:
        	widget.delete(0, tk.END)
        	widget.insert(0, text)
        except:
        	widget.delete(1.0, tk.END)
        	widget.insert(1.0, text)
        widget.configure(state=tk.DISABLED)

    def get_data(self):
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        sql = "SELECT e.*, b.*, d.`depName` "
        sql += "FROM `employees` e, `baccounts` b, `departments` d "
        sql +="WHERE e.`empID` = b.`empdb_empID` "
        sql +="AND e.`depDB_depID` = d.`depID` "
        sql +="AND e.`empID` = '"+ self.empID +"'"
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result[0])
        return result

    def set_data(self):
    	result = self.result[0]
    	self.entry_text(self.entry_name, result['firstName']+" "+result['lastName'] )
    	self.entry_text(self.entry_EmpID, result['empID'])
    	self.entry_text(self.entry_EmpName, result['firstName']+" "+result['lastName'])
    	self.entry_text(self.entry_personalno, result['empID'])
    	self.entry_text(self.entry_address,result['address'] )
    	self.entry_text(self.entry_pin, result['pin'])
    	self.entry_text(self.entry_state, result['state'])
    	self.entry_text(self.entry_adhar, result['adharID'])
    	self.entry_text(self.entry_pan, result['panID'])
    	self.entry_text(self.entry_designation, result['designation'])
    	self.entry_text(self.entry_unit, result['unit'])
    	self.entry_text(self.entry_emailid, result['email'])
    	self.entry_text(self.entry_mobile, result['mobile'])
    	self.entry_text(self.entry_department, result['depName'])
    	self.entry_text(self.entry_ifsc, result['IFSC'])
    	self.entry_text(self.enrtry_acno, result['ACNo'])
    	self.entry_text(self.entry_branch, result['BranchAdd'])

    def refresh_data(self):
        tkMessageBox.showinfo(title="Notification", \
        message="Refresh Complete")
        self.result = self.get_data()
        self.set_data()

    def printR(self):
        print_report(self.empID)

    def change_pass(self):
        tkMessageBox.showinfo(title="Notification", \
        message="Admin has been notified")
        

# root = tk.Tk()
# myapp = MainView('101403179')
# # center(myapp)
# root.mainloop()

