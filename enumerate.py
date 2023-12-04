# Enumerate Function In Python:
''' The enumerate function is a built in function in python that allow you to loop over a sequence (such as list , tuple,string) and get the index and value of each element in the sequence as the same time. Here is a basic example of how it works:'''

# marks = [12,23,45,64,67,89,1,3,5]
# index = 0
# for marks in marks:
# 	print(marks)
# 	if index == 4:
# 		print("Lakshay Is Awesome!")	
# 	index += 1	


marks = [12,45,67,87,90,56,34,1,3,2]	
for index,marks in enumerate(marks):
	print(marks)
	if index==4:
		print("Lakshay Awesome!")
	index +=1

name = ["Jack","Maichal","Root","Buttler","Rahul"]
for index,name in enumerate(name):
	print(index,name)

# Changing the Start Index:
''' By default the enumerate function starts the index at 0, but you can specify a different starting index by passing it as an arguments to the enumerate function:'''

# loop over a list and print the index (starting at 1) and value of each element

fruits = ["Mango","Bannana","Pineapple","Apple"]
for index,fruits in enumerate(fruits,start = 1):
	print(index,fruits)

fruits = ["Mango","Bannana","Pineapple","Apple"]	
for index,fruits in enumerate(fruits):
	print(f"{index+1}:{fruits}")

# loop over a tuple and print the index and value of each element:

colors = ("Red","Blue","Green","Pink","Grey")
for index,colors in enumerate(colors):
	print(index,colors)

# loop over a string and print the index and value of each character:

st = "Lakshay Tayal"
for index , st in enumerate(st):
	print(index,st)

  
