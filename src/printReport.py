from __future__ import print_function
from connection import *
from jinja2 import Environment, FileSystemLoader
import webbrowser

def print_report(id):
	env = Environment(loader=FileSystemLoader('.'))
	template = env.get_template("src/template.html")


	cursor = db.cursor(MySQLdb.cursors.DictCursor)
	sql = "SELECT e.*, b.*, d.`depName` "
	sql += "FROM `employees` e, `baccounts` b, `departments` d "
	sql +="WHERE e.`empID` = b.`empdb_empID` "
	sql +="AND e.`depDB_depID` = d.`depID` "
	sql +="AND e.`empID` = '"+ id +"'"
	# print(sql)
	cursor.execute(sql)
	result = cursor.fetchall()
	# print(result[0])
	result = result[0]
	print(result)

	template_vars = {"empID" : result['empID'],
					 "firstName" : result['firstName'],
					 "lastName" : result['lastName'],
					 "address" : result['address'],
					 "pin" : result['pin'],
					 "state" : result['state'],
					 "adharID" : result['adharID'],
					 "panID" : result['panID'],
					 "designation" : result['designation'],
					 "unit" : result['unit'],
					 "email" : result['email'],
					 "mobile" : result['mobile'],
					 "depName" : result['depName'],
					 "IFSC" : result['IFSC'],
					 "ACNo" : result['ACNo'],
					 "BranchAdd" : result['BranchAdd']
					}

	content = template.render(template_vars)

	with open('print.html', 'w') as static_file:
	            static_file.write(content)

	webbrowser.open_new_tab('print.html')

#     	self.entry_text(self.entry_name, result['firstName']+" "+result['lastName'] )
#     	self.entry_text(self.entry_EmpID, result['empID'])
#     	self.entry_text(self.entry_EmpName, result['firstName']+" "+result['lastName'])
#     	self.entry_text(self.entry_personalno, result['empID'])
#     	self.entry_text(self.entry_address,result['address'] )
#     	self.entry_text(self.entry_pin, result['pin'])
#     	self.entry_text(self.entry_state, result['state'])
#     	self.entry_text(self.entry_adhar, result['adharID'])
#     	self.entry_text(self.entry_pan, result['panID'])
#     	self.entry_text(self.entry_designation, result['designation'])
#     	self.entry_text(self.entry_unit, result['unit'])
#     	self.entry_text(self.entry_emailid, result['email'])
#     	self.entry_text(self.entry_mobile, result['mobile'])
#     	self.entry_text(self.entry_department, result['depName'])
#     	self.entry_text(self.entry_ifsc, result['IFSC'])
#     	self.entry_text(self.enrtry_acno, result['ACNo'])
#     	self.entry_text(self.entry_branch, result['BranchAdd'])
