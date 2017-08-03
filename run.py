
# the main run file that imports all the view classes
# the mainloop is present in this file
# all the objects and filepath are relative 

from src.MainView import * 
from src.LoginWin import *
from src.center import center

root = tk.Tk()
center(root)
root.withdraw()

myapp = LoginWin(root)
center(myapp)
root.mainloop()