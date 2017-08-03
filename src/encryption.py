import bcrypt
from connection import *

empID = '101403180'
password= '123456'

hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print ("Password " + password)
print("Hashed " + hashed)
if bcrypt.hashpw(password, hashed) == hashed:
    print("It Matches!")
else:
    print("It Does not Match :(")
cursor = db.cursor()
try:
   sql = "INSERT INTO `passwords`(`password`, `empdb_empID`) VALUES (%s,%s)"
   cursor.execute(sql,(hashed,empID))
   db.commit()
   print("done")
except:
   db.rollback()
   print("error")


def check_pass(id,password):
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

print(check_pass(empID, password))

def get_usernames():
        cursor = db.cursor()
        sql="SELECT `empdb_empID` FROM `passwords`"
        cursor.execute(sql)
        usernames = [item[0] for item in cursor.fetchall()]
        return usernames

print(get_usernames())

if int(empID) in get_usernames():
	print("asdasd")

