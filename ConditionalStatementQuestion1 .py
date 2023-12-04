# if, else question 
salary = int(input("Enter The Salary in Ruppee:"))
year_of_service = int(input("Enter The Number:"))
if(year_of_service<5):
	print("Employers will not get Bonus")
else:
	print("Net Bonus Amount",.05*salary)

# Second Question 
length = int(input("Enter The Length"))
breadth = int(input("Enter The Breadth"))
if(length==breadth):
	print("It Is Square")
else:	
	print("It Is Not Square")

# Third Question
a = int(input("Enter The Number"))
b = int(input("Enter The Number"))
if(a>b):
	print("a is greater")
else:	
	print("a Is Smaller")

# Fourth Question 
age = int(input("Enter Your Age:"))	
if(age<18):
	print(" Person Is Not Eligible For Vote")
elif(age>=18):	
	print("Person Is Eligible For Vote")

# Fivth question 
signal = input("Enter Your Traffic signal:")
if(signal=='green'):
	print("Car Allow To Go")
elif(signal=='orange'):	
	print("Car Has To wait")
elif(signal=='red'):
	print("Car Are Not Allowed To Go ")
else:	
	print("Unrecoganised Signal")

# Sixth Question 
name = input("Enter Your Name:")	
clas=int(input("enter your class"))
section=input("enter your section")
grade = input("Enter your Grade:")
if grade=='A' or grade=='a':
	print("Outstanding")
elif grade=='B' or grade=='b':	
	print("Excellent")
elif grade=='C' or grade=='c':	
	print("Very Good")
elif grade=='D' or grade=='d':	
	print("Good")
elif grade=='E' or grade=='e':
	print("satisfactory")
elif grade=='F' or grade=='f':	
	print("Fail")
else:
	print("abee BSDK galt grade kyu add kar raha hai")

# Seventh Question 
name = input("Enter Your Name:")
clas = int(input("Enter Your Class:"))
section =(input("Enter your Section :")).upper()
english = int(input("Enter  English Marks:"))
math = int(input("Enter Math Marks:"))
science = int(input("Enter Science Marks:"))
punjabi = int(input("Enter Punjabi Marks:"))
hindi = int(input("Enter Hindi Marks:"))
total_marks = int(input("Enter The Total Marks:"))
obtain_marks = english + math + science + punjabi + hindi
percentage = obtain_marks / total_marks * 100
print(percentage)
if percentage < 45:
	print("Student Grade Fail")
elif percentage > 45 and percentage <= 60:	
	print("student  Grade Passed")
elif percentage > 60 and percentage<=75:	
	print("Student  Grade is good")
elif percentage > 75 and percentage <= 85:	
	print("Student  Grade is very good")
elif percentage > 85 and percentage <= 100:	
	print("Student Grade Is Excellent ")
elif percentage > 100:	
	print("Student graded Error")

# tenth Question 
marks = int(input("Enter your Marks:"))
if marks > 0 and marks < 100:
	if marks < 50:
		print("Fail")
	elif marks >= 50 and marks < 60:	
		print("Good")
	elif marks >= 60 and marks < 80:	
		print("Very Good ")
	elif marks >= 80 and marks < 100:
		print("Outstanding")
else:
   print("Error")