#!/soft/python-2.7/bin/python
import cgi
import cgitb
cgitb.enable()  # for troubleshooting
import os,sys
import time


picPath = "picture"
txtPath = "text"
#print header




HTML_FORM_TEMPLATE = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<title>File Upload</title>
<link rel="stylesheet" href="style.css" type="text/css">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<script type="text/javascript">
	function typeCheck(){
		var fileinput = document.getElementById("fileInput");
		var filename = fileinput.value;
		var suffix = filename.substring(filename.length - 3).toLowerCase();
		if (suffix == 'jpg'){
			return true;
		}
		else {
			suffix = filename.substring(filename.length - 4).toLowerCase();
			if (suffix == 'jpeg') {
				return true;
			}
			else {
				alert("Please submit jpg or jpeg!");
				return false;
			}
		}
	}
</script>
</head>
<body>
<center><h1>Upload a New JPEG Picture</h1></center>
<center><form onsubmit="return typeCheck();" action="upload.cgi" method="POST" enctype="multipart/form-data">
Title name: <input name="title" type="text" ><br> 
File: <input id="fileInput" name="file_input" type="file"><br>
<input value="Upload" type="submit">
<input value="Cancel" type="button" onclick="window.location.href = 'Gallery.cgi'">
</form></center>
</body>
</html>"""

HTML_FORM_TEMPLATE_2 = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<title>File Upload</title>
<link rel="stylesheet" href="style.css" type="text/css">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<script type="text/javascript">
	function typeCheck(){
		var fileinput = document.getElementById("fileInput");
		var filename = fileinput.value;
		var suffix = filename.substring(filename.length - 3).toLowerCase();
		if (suffix == 'jpg'){
			return true;
		}
		else {
			suffix = filename.substring(filename.length - 4).toLowerCase();
			if (suffix == 'jpeg') {
				return true;
			}
			else {
				alert("Please submit jpg or jpeg!");
				return false;
			}
		}
	}
</script>
</head>
<body>
<center><h1>Upload a New JPEG Picture</h1></center>
<center><span>Picture Title Cannot Be Empty</span></center>
<center><form onsubmit="return typeCheck();" action="upload.cgi" method="POST" enctype="multipart/form-data">
Title name: <input name="title" type="text"><br> 
File: <input id="fileInput" name="file_input" type="file"><br>
<input value="Upload" type="submit">
<input value="Cancel" type="button" onclick="window.location.href = 'Gallery.cgi'">
</form></center>
</body>
</html>"""

def save_uploaded_file (form_pic, form_title, pic_dir, txt_dir):
	if not form.has_key(form_pic) or not form.has_key(form_title):
		print "Content-type: text/html\n\n"
		print HTML_FORM_TEMPLATE
		return
	filepic = form[form_pic]
	filetxt = form[form_title]		
	if not len(filetxt.value) == 0 and len(filepic.filename) == 0:
		print "Content-type: text/html\n\n"
		print HTML_FORM_TEMPLATE
		return			
	if len(filetxt.value) == 0:
		print "Content-type: text/html\n\n"
		print HTML_FORM_TEMPLATE_2
		return
	filename = str(time.time())
	imgout = file (os.path.join(pic_dir, filename), 'w')
	txtout = file (os.path.join(txt_dir, filename), 'w')
	while 1:
		chunk1 = filepic.file.read(100000)
		if not chunk1: break
		imgout.write (chunk1)
	imgout.close()
	while 1:
		chunk2 = filetxt.file.read(100000)
		if not chunk2: break
		txtout.write (chunk2)
	txtout.close()	
	print "Content-type: text/html"
	print "Location:Gallery.cgi"
	print

if 'HTTP_COOKIE' in os.environ:
	cookies = os.environ['HTTP_COOKIE']
	cookies = cookies.split(';')
	handler = {}
	for cookie in cookies:
		cookie = cookie.split('=')
		handler[cookie[0]] = cookie[1]
	if handler.has_key('LOGIN'):
		if handler['LOGIN'] == 'Owner':
			form = cgi.FieldStorage()
			save_uploaded_file("file_input", "title", picPath, txtPath)
		elif handler['LOGIN'] == 'Visitor':
			print "Content-type: text/html"
			print "Location:Gallery.cgi"
			print
	else:
		print "Content-type: text/html"
		print "Location:login.html"
		print