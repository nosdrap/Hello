This is linux program made with python3 and shell commands.

Made and tested in Linux Ubuntu.

The program will create simple Hello World file. It does not rewrite any existing files with same name.

Manual:

Use path to add hello command to PATH.

If you are in Hello directory use:

	./dist/hello path

general use: 

	hello filename.extention command
	
filename: any filename including path to the filename
	
	hello ./test/HelloWorld.py
	
supported extentions: py,c,cpp,html,php,java,sh
	
command: 

	hello filename.extention exe 
	
- runs the file, supported extentions: py,c,cpp,sh,java,html
	
any other cmd commands - cat,nano,rm,etc...
	
	 hello filename.extention nano
	 hello filename.extention rm
	 
It executes only single command (atm):

	hello test.java nano exe

will run only:
	
	nano test.java

commands are executed as command filename.extention after they were created or they already exists
