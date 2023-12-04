# Opening a file
''' We can perform any operation on a file, me must first open it.Python provide the open() function to open file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r'for reading ,'w' for writing and 'a' for appending.'''

# Reading and opening a File
f = open("myfiles.txt","r")
print(f)
text = f.read()
print(text)
f.close


# Modes of file
# A. read(r): This mode opens the files for reading only and given an error if the file does not exist. This is default mode if no mode is passed as a parameter.
# B. write(w): This mode opens the files for writing only and creates a new files if the file does not exist.
# C. append(a): This mode opens the file  for appending only and creates a new file if the files does not exist.
# D. create(x): This Mode create a file and gives an error if the file already exist.
# E. text(t): Apart from these modes we also need to specify hoe the file must be handeled. t mode id used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt sice text mode is the default . the default mode is 'r'(open for reading text, synonym of 'rt').
# F. binary(b): used to handle binary files (images,pdfs, etc)

# Writing A Files
f = open("myfiles.txt","w")
f.write("Hello, World!")
f.close

f = open("myfiles.txt","a")
f.write("Hello, Lakshay")
f.close

# Closing a Files
# with statement
''' you can use the with statement to automatically close the file after you are done with it.'''

with open("myfiles.txt", 'a') as f:
	f.write("Hey I am Lakshay Tayal")



# Methods:
# A. readline() method:
''' the readline() method read a single line from the file . If we want to read multiple lines, we can use loop.'''
# the readline() method reads all the lines of the file and returns them as a list of string

f = open("myfiles1.txt","r")
i = 0
while True:
	i += 1
	line = f.readline()
	if not line:
		break
	m1 = int(line.split(",")[0])
	m2 = int(line.split(",")[1])
	m3 = int(line.split(",")[2])
	print(f"marks of Student {i} in maths in : {m1*2}")
	print(f"Marks of student {i} in Physics is: {m2*2}")
	print(f"Marks of student {i} in SSt is: {m3*2}")
	print(line)


# Writeline() method:
''' The writeline() method in python writes a sequence of string to a file. the sequence can be any iterable object, such as list or a tuple.'''

f = open('Myfiles.txt','w')
lines = ['line1\n','line2\n','line3\n']
f.writelines(lines)
f.close()

# Keep in mind that the writeline() method does not add newline character between the strings in the sequence . If you want to add newline between the string yu can use a loop to write each strings separately:

f = open('myfiles.txt','w')
line = ['linw1','line2','line3']
for line in line:
	f.write(line + '\n')
f.close()	


# seek() and tell() functions
''' In pyhton the seeks() and tell() function are used to work with fioe object and their position within a file. These function are part of the built in module , which provide a consistent interface for reading and writing to various file- like object such as files, pipes, and in memory buffers.'''

# seek() functions
''' The seek() function allow you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position For Example:'''
with open('files.txt','r') as f:
	print(type(f))
	# move to the 10th byte in the file
	f.seek(10)
	#Read the next 5 bytes
	data = f.read(5)
	print(data)

# tell() method:

''' The tell() function returns the current position within the files in bytes. this can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position. For Example:'''

with open('files.txt','r') as f:
	print(type(f))
	# move to the 10th byte in the file
	f.seek(10)
	#Read the next 5 bytes
	print(f.tell())
	data = f.read(5)
	print(data)	


# truncate() function:

''' When you open a files in pyhton using the open function you can specify the mode in which you want to open file . if you specify the mode as 'w' or 'a'. the file is opened in write mode and you can write to the files. However, if you want to truncate the file to a file to a specific size , you can use the truncate function.
'''
with open('sample.txt','w') as f:
	f.write("Hello World")
	f.truncate(5)
with open('sample.txt','r') as f:	
	print(f.read())

	

