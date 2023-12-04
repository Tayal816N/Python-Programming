print("Welcome To Snake Water Gun Game ")
print("Dosto!")
name1 = "Lakshay Tayal"
print(f"My Name is:{name1}")
name = input("Enter Your Full Name:")
age = int(input("Enter Your Actual Age:"))
computer = ["Snake","Water","Gun"]
import random
def check(comp,user):
	if comp == user:
		return 0
	if comp == 0 and user == 1:	
		return -1
	if comp == 1 and user == 2:
		return -1
	if comp == 2 and user == 0:
		return -1
	return 0
	

comp = random.randint(0,2)		
user = int(input("0 for Snake, 1 for Water and 2 for Gun:\n"))

score = check(comp,user)
print("You: ", user )
print("Computer: ", comp)
if score == 0:
	print(f"{name},You game is draw")
elif score == -1:	
	print(f"Sorry!, {name}, You Loose The Game score")
else: 
	print(f"Hurray!,{name},You Won The Match")