import MySQLdb
import tkMessageBox
import Tkinter as tk
root = tk.Tk()
root.withdraw()

try:
	db = MySQLdb.connect(host="localhost",user="root",passwd="",db="u186140256_eims")
except:
	tkMessageBox.showerror('Error', 'Database Server not reachable')
	root.destroy()
	exit()
