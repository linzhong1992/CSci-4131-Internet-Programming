#!/soft/python-2.7/bin/python
import cgi
import cgitb
cgitb.enable()  # for troubleshooting
import os,sys
import time

picPath = "picture"
txtPath = "text"
form = cgi.FieldStorage()
if form.has_key("file_name"):
	fileName = form["file_name"].value
	textFile = open(txtPath + "/" + fileName, 'r')
	textContent = textFile.read()
	print "Content-type: text/html\n\n"
	print """
	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
	<html>
	<head>
	<title>Edit</title>
	<link rel="stylesheet" href="style.css" type="text/css">
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
	</head>
	<body>
	<center><h1>Delete Picture</h1></center>
	<center><h3>Are you sure? You want to delete picture [""" + textContent + """].</h3></center>
	<center><form action="delete.cgi" method="POST" enctype="multipart/form-data">
	<input value="Delete" type="submit">
	<input value="Cancel" type="button" onclick="window.location.href = 'Gallery.cgi'">
	<input type="hidden" name="file_name_2" value='""" + fileName + """'>
	</form></center>
	</body>
	</html>"""
elif form.has_key("file_name_2"):
	fileName = form["file_name_2"].value
	os.remove(picPath + "/" + fileName)
	os.remove(txtPath + "/" + fileName)
	os.remove(fileName)
	print "Content-type: text/html"
	print "Location:Gallery.cgi"
	print
else:
	if 'HTTP_COOKIE' in os.environ:
		cookies = os.environ['HTTP_COOKIE']
		cookies = cookies.split(';')
		handler = {}
		for cookie in cookies:
			cookie = cookie.split('=')
			handler[cookie[0]] = cookie[1]
		if handler.has_key('LOGIN'):
			if handler['LOGIN'] == 'Owner' or handler['LOGIN'] == 'Visitor':
				print "Content-type: text/html"
				print "Location:Gallery.cgi"
				print
		else:
			print "Content-type: text/html"
			print "Location:login.html"
			print	



