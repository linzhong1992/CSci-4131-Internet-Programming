#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import MySQLdb
import Cookie
import os
import time


login = 'NULL'
configHandler = {}
fileConfig = open('config.txt', 'r')
while 1:
	line = fileConfig.readline()
	if not line:
		break
	line = line.split(':')
	configHandler[line[0].strip()] = line[1].strip()
fileConfig.close()


form = cgi.FieldStorage()
cookie = Cookie.SimpleCookie()

name_input = form['username'].value
passwd_input = form['password'].value

query = 'select * from Users'
db = MySQLdb.connect(host="egon.cs.umn.edu", user=configHandler['MySQLuserID'], passwd=configHandler['MySQLpassword'], port=3307)
db.select_db(configHandler['MySQLuserID'])
cursor = db.cursor()
cursor.execute(query)

for row in cursor:
	if name_input == row[1] and passwd_input == row[3]:
		login = row[2]
		break
cookie['LOGIN'] = login
cookie['LOGIN']['max-age'] = configHandler['expirationTime']
print cookie
if login == 'Owner':
	print "Content-type: text/html"
	print "Location:ownermenu.cgi"
	print
elif login == 'Visitor':
	print "Content-type: text/html"
	print "Location:Gallery.cgi"
	print
elif login == 'NULL':
	print "Content-type: text/html"
	print "Location:login.html"
	print
