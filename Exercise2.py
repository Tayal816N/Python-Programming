import time 
time_stamp = time.strftime('%H:%M:%S')
print(time_stamp)
time_stamp = time.strftime("%H")
print(time_stamp)
time_stamp = time.strftime("%M")
print(time_stamp)
time_stamp = time.strftime("%S")
print(time_stamp)
hour = int(time.strftime('%H'))
print(hour)
hour = int(input("Enter Your Hours "))

if(hour>=0 and hour<12):
	print("Good Morning Sir")
elif(hour>=12 and hour<17):	
	print("Good Afternoon Sir")
elif(hour>=17 and hour<0):	
	print("Good Night Sir")

