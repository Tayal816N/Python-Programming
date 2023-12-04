# In Exception handling :
# They are the Try..Except in python simply mean that:
''' Try..except are the blocks are used in python to handle errors and exceptions. the code in try block runs when there is no error. If the try block catches the error , then the exception block will executed.'''

# Suntax:
''' try:
		num = int(intput("Enter the integer:"))
	except valueerror:	
		print("Number Entered is not an integers")'''

# Example

try:
	num = int(input("Enter The Number"))
	print("Your choice is right")
except ValueError:	
	print("Number Entered is not an integer")
except SyntaxError: 	
	print("Syntax occured ")

''' In addition to try and except blocks, we also have else and finally blocks. the code in else block is executed when there is no error in try block.'''

try:
	int(input("Enter an Integer:"))
except ValueError:	
	print("You Enter The Wrong Integer")
else:	
	print("I Accept Integer")

''' The finally block is executed whatever is the outcome of try except else block'''

try:
	num = int(input("Enter The number"))
except ValueError:	
	print("You enter wrong Integer")
else:	
	print("I Accept Integer")
finally:	
	print("This Block Is always Executed")

# More Example	
try:
	a = int(input("Enter The number"))
	num = ("lakshay","Tayal",17)
	print(num[a])
except ValueError: 	
	print("You Enter The Invalid String")
except IndexError:	
	print("Index Error")
else:	
	print("We accept String")