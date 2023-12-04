i = 1
for i in range(12):
	print("5 X", i , "=" , 5 * i)
	i += 1
	if(i==10):
		break
print("Exit from loop")

i = 1
for  i in range (10):
	if(i==4):
		print("Exit of iteration ")
		continue
	print("4 X", i , "=" , 4 * i)
	i += 1
	
# how to emulate the do while function 	
while True:
	n = int(input("Enter"))#1
	print(n)
	if not n>0:#false
		break


