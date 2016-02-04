#!/soft/python-2.7/bin/python
import cgi
import cgitb
cgitb.enable()  # for troubleshooting
import os,sys
import time

picPath = "Pictures"
txtPath = "text"
form = cgi.FieldStorage()
if not form.has_key("file_name_2"):
	fileName = form["file_name"].value
	textFile = open(txtPath + "/" + fileName, 'r')
	textContent = textFile.read()
else:
	fileName = form["file_name_2"].value
	os.remove(picPath + "/" + fileName)
	os.remove(txtPath + "/" + fileName)
	print "Content-type: text/html"
	print "Location:Gallery.cgi"
	print

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
<center><h1>Edit Picture Title</h1></center>
<center><h3>Are you sure? You want to delete picture [""" + textContent + """].</h3></center>
<center><form action="delete.cgi" method="POST" enctype="multipart/form-data">
<input value="Delete" type="submit">
<input value="Cancel" type="button" onclick="window.location.href = 'Gallery.cgi'">
<input type="hidden" name="file_name_2" value='""" + fileName + """'>
</form></center>
</body>
</html>"""

