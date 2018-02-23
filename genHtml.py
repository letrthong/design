#!/usr/bin/python
# Thong LT
#
#
'''
├── 1. Overview
│   └── decription.txt
├── 2. Web Service
│   ├── 2.1 setUserWebServerInfoStore
│   │   ├── decription.txt
│   │   ├── function.txt
│   │   ├── Parameters.txt
│   │   └── Returns.txt
│   └── 2.2 getUserWebServerInfoStore
│       ├── decription.txt
│       └── function.txt
└── 3. Demo
'''
#


import os, sys

htmlbegin = """<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
<title> Document</title>  
<style>
pre , h2, h3, h4{
    font-family: "Times New Roman";
    text-align: left;
}

table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 5px;
}
</style>
</head>
<body>"""

htmlContentsBegin="""<!--Begin tables of contents-->
<pre style=" overflow: scroll; position: fixed;  top: 100px;  right: 0;  width:20%; height: 600px;  border: 1px solid #73AD21;"><h5 id="TableOfContent">Table Of Contents</h5>"""

htmlContentsEnd="""</pre>
<!--End tables of contents-->
"""

htmlDivBegin ="""<div style="width: 75%;">
<!--Begin Div-->"""

htmldiv2 ="""<!--Begin Div-->
<div id="$id">
<h2 style="color:blue;"> $title </h2>
  <div  style=" position: relative; left: 15px;">
    $data
  </div>
</div>
<!--End Div-->"""

htmldiv3 ="""<!--Begin Div-->
<div id="$id">
<h3> $title </h3>
  <div  style=" position: relative; left: 15px;">
	$data
  </div>
</div>
<!--End Div-->"""

htmldivDecription="""<pre>$data</pre>"""
			
htmldivFunction  ="""<pre style="background-color:powderblue;  border: 1px solid  #3498db;" >

		$data

</pre>"""
	
htmldivReturn="""<h4 > <font color="#EDDA74" > Returns </font></h4> 
<div  style=" position: relative; left: 15px;">  <pre>$data</pre>
</div>"""

htmldivParameter="""<h4 > <font color="#EDDA74" > Parameters </font></h4> 
<div  style=" position: relative; left: 15px;">  <pre>$data</pre>
</div>"""

htmlDivEnd="""</div>
<!--End Div-->"""

htmlend="""
</body>
</html>	"""

rootPath= os.getcwd()

def readFile(path):
	data = ""
	file = open(path, "r") 
	data =file.read() 
	file.close()
	return data;
		
def writefile(path, data):
	file = open(path,"w") 
	file.write(data) 
	file.close()
	
def getDiv(dirPath , level):
	data = "";
	dirs = os.listdir( dirPath )
	dirs.sort()
	for dir in dirs:
		path= rootPath + "/" +  dirPath + "/" + dir
		if os.path.isdir(path): 
			subDir= dirPath + "/" + dir
			pos = dir.find(" ");
			id =  dir[0:pos]
			fullPath =  rootPath +  "/" + subDir;
			
			body = "";
			functionpath = fullPath + "/function.txt"
			if os.path.exists(functionpath) :
				text = readFile(functionpath );
				divFunction = htmldivFunction.replace("$data", text)
				body = body +  divFunction;
				
			decriptionpath = fullPath + "/decription.txt"
			if os.path.exists(decriptionpath) :
				text = readFile(decriptionpath );
				divDecription = htmldivDecription.replace("$data", text)
				body = body +  divDecription;
			
			Parameterspath = fullPath + "/Parameters.txt"
			if os.path.exists(Parameterspath) :
				text = readFile(Parameterspath );
				divParameter = htmldivParameter.replace("$data", text)
				body = body +  divParameter;
				
			Returnspath = fullPath + "/Returns.txt"
			if os.path.exists(Returnspath) :
				text = readFile(Returnspath);
				divReturn = htmldivReturn.replace("$data", text)
				body = body +  divReturn;
				
			if  level == 0:
				div = htmldiv2.replace("$id", id)
			else:
				div = htmldiv3.replace("$id", id)
				
			div = div.replace("$title", dir)
			div = div.replace("$data", body)
			data = data + div + "\n" + getDiv(subDir, level + 1) 
	return data;

def getTableofcontent(dirPath , level ):
	data = "";
	dirs = os.listdir( dirPath )
	dirs.sort()
	for dir in dirs:
		path= rootPath + "/" +  dirPath + "/" + dir
		if os.path.isdir(path): 
			subDir= dirPath + "/" + dir
			pos   = dir.find(" ");
			id    =  dir[0:pos]
			link  = ""
			link0 = """$id <a href="#$link"><font size="4"> $text  </font></a> """;
			link1 = """   $id  <a href="#$link"><font size="3" color="DeepSkyBlue"> $text </font></a> """;
			
			if level == 0:
				link = link0.replace("$link", id)
			else:
				link = link1.replace("$link", id)
				
			link = link.replace("$id", id)
			link = link.replace("$text", dir[pos:])
			#print link
			data = data + link + "\n" + getTableofcontent(subDir , level + 1) 
	return data;

def genHtml(dir):
	tableOfcontenttableOfcontent = getTableofcontent(dir, 0)
	div = getDiv(dir, 0)
	html= htmlbegin + htmlContentsBegin + tableOfcontenttableOfcontent + htmlContentsEnd + 	htmlDivBegin + div + htmlDivEnd +  htmlend	
	writefile("text.html" , html)
	
print "running... "
genHtml("interface")
print "done"			
		
