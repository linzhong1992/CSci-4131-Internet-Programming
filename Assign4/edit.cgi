#!/soft/python-2.7/bin/python
import cgi
import cgitb
cgitb.enable()  # for troubleshooting
import os,sys
import time

picPath = "Pictures"
txtPath = "text"
HTML_TEMPLATE = """
	<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
	<html>
	<head>
	<title>Edit</title>
	<link rel="stylesheet" href="style.css" type="text/css">
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
	</head>
	<body>
	<center><h1>Edit Picture Title</h1></center>
	<center><span>{}<span></center>
	<center><form action="edit.cgi" method="POST" enctype="multipart/form-data">
	Title: <input name="title" type="text" value={}><br> 
	<input value="Update" type="submit">
	<input value="Cancel" type="button" onclick="window.location.href = 'Gallery.cgi'">
	<input type="hidden" name="file_name_2" value={}>
	</form></center>
	</body>
	</html>"""



def edit_title(new_title, prev_file_name, curr_file_name):
	if form.has_key(prev_file_name):
		txtName = form[prev_file_name].value
		textFile = open(txtPath + "/" + txtName, 'r')
		textContent = textFile.read()
		print "Content-type: text/html\n\n"
		print HTML_TEMPLATE.format('', textContent, txtName)
	else:
		newTextContent = form[new_title]
		txtName = form[curr_file_name].value
		if len(newTextContent.value) == 0:
			print HTML_TEMPLATE.format('Picture Title Cannot Be Empty', '', txtName)
			return
		txtout = file (os.path.join(txtPath, txtName), 'w')
		while 1:
			chunk = newTextContent.file.read(100000)
			if not chunk: break
			txtout.write (chunk)
		txtout.close()
		print "Content-type: text/html"
		print "Location:Gallery.cgi"
		print
form = cgi.FieldStorage()
edit_title("title", "file_name", "file_name_2")

