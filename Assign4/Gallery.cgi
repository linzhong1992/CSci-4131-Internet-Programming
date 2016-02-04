#!/soft/python-2.7/bin/python
import cgi
import cgitb
cgitb.enable()  # for troubleshooting
import os
from PIL import Image

picPath = "Pictures"
txtPath = "text"
listPic = os.listdir(picPath)
listTN = []
listText = os.listdir(txtPath)
olistText = []
listTitle = []


for picName in listPic:	
	size = (140, 140)
	im=Image.open(picPath + '/' + picName)
	im.thumbnail(size)
	tnName = picName
	im.save(tnName, "JPEG")
	listTN.append(tnName)
	for txtName in listText:
		if txtName == picName:
			olistText.append(txtName)
			textFile = open(txtPath + "/" + txtName, 'r')
			listTitle.append(textFile.read())
			break
#print header
print "Content-type: text/html\n\n"

print """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<title>Picture Gallery</title>
<link rel="stylesheet" href="style.css" type="text/css">
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<script type="text/javascript">
	function expand(i){
		var bg = document.getElementById(i);
		bg.style.visibility = 'visible';
		bg.onclick = function(){
			bg.style.visibility = 'hidden';
		};
	}
</script>
</head>
<body>
<center><h1>Picture Gallery</h1></center>"""
print """<div align="center">
	<input type="button" value="Refresh" onclick="window.location.href = 'Gallery.cgi'">
	<input type="button" value="Upload New Picture" onclick="window.location.href = 'upload.cgi'">
	</div>
	<div class="grid">"""
for i in range(len(listTN)):
	print "<div class='tnbox'>"
	print """<img onclick="expand('""" + str(i) + """')" class="thumb" src='""" + listTN[i] + """'>"""
	print "<p>" + listTitle[i] + "</p>"
	print """<center><form action="delete.cgi">
	<input type="submit" value="Delete">
	<input name="file_name" type="hidden" value='""" + olistText[i] + """'>
	</form>
	<form action="edit.cgi">
	<input type="submit" value="Edit">
	<input name="file_name" type="hidden" value='""" + olistText[i] + """'>
	</form></center>"""
	print "</div>"
print "</div>"
print "<div>"
for j in range(len(listTN)):
	print "<div id='" + str(j) + "' class='background'>"
	print "<p style='color:blue'>" + listTitle[j] + "</p>"
	print """<img src='""" + picPath + '/' + listTN[j] + """'>"""
	print "</div>"	
print """</div></body></html>"""
