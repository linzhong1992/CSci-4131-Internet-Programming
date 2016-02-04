#!/soft/python-2.7/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb
import Cookie
import os,sys
import time

TEMPLATE = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<title>Owner Menu</title>
<link rel="stylesheet" href="style.css" type="text/css">
</head>
<body>
<center>
<div>
<h1>Add User</h1>
<span>{}</span>
<br/>
<form action="ownermenu.cgi" method="POST" enctype="multipart/form-data">
Name: <input type="text" name="add_username">
Password: <input type="text" name="add_password">
<br/>
<br/>
<input type="submit">
</form>
</div>
</center>
<center>
<div>
<h1>Change User's Password</h1>
<span>{}</span>
<br/>
<form action="ownermenu.cgi" method="POST" enctype="multipart/form-data">
Name: <input type="text" name="change_username">
Password: <input type="text" name="change_password">
<br/>
<br/>
<input type="submit">
</form>
</div>
</center>
<center>
<div>
<h1>Delete User</h1>
<span>{}</span>
<br/>
<form action="ownermenu.cgi" method="POST" enctype="multipart/form-data">
Name: <input type="text" name="delete_username">
<br/>
<br/>
<input type="submit">
</form>
</div>
</center>
<center>
<h1>Show Gallery</h1>
<br/>
<br/>
<input type="button" value="Show Gallery" onclick="window.location.href = 'Gallery.cgi'">
</center>
</body>
</html>"""
form = cgi.FieldStorage()
configHandler = {}
fileConfig = open('config.txt', 'r')
while 1:
	line = fileConfig.readline()
	if not line:
		break
	line = line.split(':')
	configHandler[line[0].strip()] = line[1].strip()
fileConfig.close()
query = 'select * from Users'
db = MySQLdb.connect(host="egon.cs.umn.edu", user=configHandler['MySQLuserID'], passwd=configHandler['MySQLpassword'], port=3307)
db.select_db(configHandler['MySQLuserID'])
cursor = db.cursor()

def checkDup(name_input, cursor):
	cursor.execute('select * from Users')
	for row in cursor:
		if name_input == row[1]:
			return 1
	return 0

def checkOwner(name_input, cursor):
	cursor.execute('select * from Users')
	for row in cursor:
		if row[1] == name_input and row[2] == 'Owner':
			return 1
	return 0


if 'HTTP_COOKIE' in os.environ:
	cookies = os.environ['HTTP_COOKIE']
	cookies = cookies.split(';')
	handler = {}
	for cookie in cookies:
		cookie = cookie.split('=')
		handler[cookie[0]] = cookie[1]
	if handler.has_key('LOGIN'):
		if handler['LOGIN'] == 'Owner':
			if form.has_key('add_username'):
				name_input = form['add_username'].value
				passwd_input = form['add_password'].value
				dup = checkDup(name_input, cursor)	
				if dup == 1 or len(name_input) == 0 or len(passwd_input) == 0:
					print 'content-type: text/html\n'
					print TEMPLATE.format('Username is duplicated OR at least one of the fields is empty OR you are trying to change an Owner!', '', '')
				else:
					query1 = "insert INTO Users(userID, Name, Role, Password) VALUES (null, '"+name_input+"', 'Visitor', '"+passwd_input+"')"
					cursor.execute(query1)
					db.commit()
					print "Content-type: text/html"
					print "Location:success.html"
					print	
			elif form.has_key('change_password'):
				name_input = form['change_username'].value
				passwd_input = form['change_password'].value
				dup = checkDup(name_input, cursor)
				owner = checkOwner(name_input,cursor)								
				if dup == 0 or owner == 1 or len(name_input) == 0 or len(passwd_input) == 0:
					print 'content-type: text/html\n'
					print TEMPLATE.format('', 'Cannot find the username OR at least one of the fields is empty OR you are trying to change an Owner!', '')
				else:
					query2 = "update Users set Password='"+passwd_input+"' where Name='"+name_input+"'"
					cursor.execute(query2)
					db.commit()
					print "Content-type: text/html"
					print "Location:success.html"
					print						
			elif form.has_key('delete_username'):
				name_input = form['delete_username'].value
				dup = checkDup(name_input, cursor)
				owner = checkOwner(name_input,cursor)				
				if dup == 0 or owner == 1 or len(name_input) == 0:
					print 'content-type: text/html\n'
					print TEMPLATE.format('', '', 'Cannot find the username OR the fields is empty OR you are trying to delete an Owner!')
				else:
					query3 = "delete from Users where Name='"+name_input+"'" 
					cursor.execute(query3)
					db.commit()
					print "Content-type: text/html"
					print "Location:success.html"
					print	
			else:								
				print 'content-type: text/html\n'
				print TEMPLATE.format('','','')
	else:
		print "Content-type: text/html"
		print "Location:login.html"
		print
