import os
import sys
import subprocess
import os.path
if len(sys.argv)==1:
	os.system("echo 'No argument found'")
	sys.exit()
else:
	if len(sys.argv)==2:
		if sys.argv[1]=="path":
			helloPath=subprocess.check_output('find / -type d -name Hello 2>&1| grep -v "Permission denied"',shell=True)
			helloPath=helloPath.replace(b"\n",b"")
			helloPath=str(helloPath,'utf-8')
			findCommand="find "+helloPath+" -type d -name 'dist'"
			distPath=subprocess.check_output(findCommand,shell=True)
			distPath=distPath.replace(b"\n",b"")
			distPath=str(distPath,'utf-8')
			distPath=":"+distPath
			environment=subprocess.check_output('sudo cat /etc/environment',shell=True)
			environment=environment.replace(b"\n",b"")
			environment=str(environment,"utf-8")
			if distPath in environment:
				os.system('echo "Hello is already in path"')
				sys.exit()
			environment=environment.replace('"',"")
			environment=environment.replace("PATH=","")
			environment=environment+distPath
			os.system('echo "Creating backup of environment file into environmentHello.bak"')
			os.system('sudo cp /etc/environment /etc/environmentHello.bak')
			environment='PATH=\"'+environment+'\"'
			os.system("echo 'Adding Hello to path:'")
			os.system("echo '" +environment+"'| sudo tee /etc/environment")
			sys.exit()
		else:
			command="cat"

	else:
		command=sys.argv[2]
	path=sys.argv[1]
	bashCommand='test -f "' +path+ '"&& echo "found" || echo "not found"'
	exist=subprocess.check_output(bashCommand,shell=True)
	dir=""
	pathArray=[]
	x=range(len(path))
	if not ("." in path):
		os.system("echo 'Suffix not found'")
		sys.exit()
	for pos in x:
		dir=dir+path[pos]
		if path[pos]=="/" or path[pos]==".":
			if dir!="":
				pathArray.append(dir)
				dir=""
	pathArray.append(dir)
	pathArray[-2]=pathArray[-2]+pathArray[-1]
	if pathArray[0]=="." and pathArray[1]=="/":
		pathArray[1]=pathArray[0]+pathArray[1]
		pathArray.pop(0)
		pathArray[1]=pathArray[0]+pathArray[1]
		pathArray.pop(0)
	elif pathArray[0]=="/":
		pathArray[1]=pathArray[0]+pathArray[1]
		pathArray.pop(0)
	if "." in pathArray[-2]:
		suffix=pathArray[-1]
	else:
		os.system("echo 'error: suffix not found'")
		sys.exit
	bashCommand="basename "+pathArray[-2]
	test=subprocess.check_output(bashCommand,shell=True)
	filename=pathArray[-2]
	if pathArray[-2] in str(test):
		filename=pathArray[-2]
	else:
		sys.exit()
	pathArray.pop(-1)
	pathArray.pop(-1)
	pathlen=len(pathArray)
	dirnum=0
	while pathlen>0:
		i=dirnum
		newdir=pathArray[dirnum]
		while i>0:
			newdir=pathArray[i-1]+newdir
			i=i-1
		bashCommand='test -d "' +newdir+ '"&& echo "found" || echo "not found"'
		test=subprocess.check_output(bashCommand,shell=True)
		if "not" in str(test):
			bashCommand='mkdir "' +newdir+ '"'
			os.system(bashCommand)
		dirnum=dirnum+1
		pathlen=pathlen-1
	new=False
	if "not" in str(exist):
		new=True
		os.system("touch '"+path+"'")
		f=open(path,"w")
		if suffix=="py":
			text='print("Hello world!")\n'
			f.write(text)
		elif suffix=="java":
			name=str(filename)
			name = name.replace('.java','')
			name = name.replace('./','')
			f.write('public class '+ name + '\n')
			f.write('{\n')
			f.write('\tpublic static void main(String args[])\n')
			f.write('\t\t{\n')
			f.write('\t\tSystem.out.println("Hello world");\n')
			f.write('\t\t}\n')
			f.write('\t}\n')
		elif suffix=="c":
			f.write('#include <stdio.h>\n')
			f.write('int main() {\n')
			f.write('\tprintf("Hello World!\\n");\n')
			f.write('\treturn 0;\n')
			f.write('}\n')
		elif suffix=="cpp":
			f.write('#include<iostream>\n')
			f.write('using namespace std;\n')
			f.write('int main()\n')
			f.write('{\n')
			f.write('\tcout<<"Hello World";\n')
			f.write('\treturn 0;\n')
			f.write('}\n')
		elif suffix=="php":
			f.write('<html>\n')
			f.write('  <head>\n')
			f.write('    <title>Hello World</title>\n')
			f.write('  </head>\n')
			f.write('  <body>\n')
			f.write('  <?php \n')
			f.write('    echo "Hello World";\n')
			f.write('  ?>\n')
			f.write('  </body>\n')
			f.write('</html>\n')
		elif suffix=="html":
			f.write('<!DOCTYPE html>\n')
			f.write('<html>\n')
			f.write('  <head>\n')
			f.write('    <title>Hello World</title>\n')
			f.write('  </head>\n')
			f.write('  <body>\n')
			f.write('    <h1>Hello World!</h1>\n')
			f.write('  </body>\n')
			f.write('</html>\n')
		elif suffix=="sh":
			f.write('#!/bin/bash\n')
			f.write('echo "Hello World"\n')
		else:
			os.system("echo 'Hello is not supported for this file type'")
		f.close()
		os.system("echo '"+filename+" was created'")
	if len(sys.argv)==2 and not(new):
		os.system("echo 'file already exists'")
	if len(sys.argv)>2:
		command=sys.argv[2]
		if command=="exe":
			if len(pathArray)==0:
				if path[0]!="/" or path[1]!="/":
					path="/"+path
				if path[1]!=".":
					path="."+path
			exe=""
			if suffix=="py":
				os.system("python3 "+path)
			elif suffix=="sh":
				os.system("chmod +x "+path)
				os.system(path)
			elif suffix=="c":
				os.system("gcc -o "+path.replace(".c"," ")+path)
				os.system(path.replace(".c"," "))
			elif suffix=="cpp":
				os.system("gcc -o "+path.replace(".cpp"," ")+path)
				os.system(path.replace(".cpp",""))
			elif suffix=="java":
				os.system("javac -d '"+ path.replace(filename,"") +"' "+path)
				os.system("java -cp "+path.replace(filename," ")+filename.replace(".java",""))
			elif suffix=="html":
				os.system("firefox "+path)
			else:
				exe="echo 'This file type is not executable'"
		else:
			os.system(command+" "+path)

