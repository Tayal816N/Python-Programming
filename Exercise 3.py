# Create the program capable to display question and give answer like in KBC
# Use any data type to perform this program .
# Display the final amount the person is taking home after playing the game.

name = input("Enter Your Full Name:")
print("Hello!",name,"Welcome to the Kaun Banega Crorepati!")
name1 = "Amitabh Bachchan"
print("My Name Is:",name1)
question = [["The International Literacy Day is observed on?","Sep8","Nov 28","Feb 2","None",1],["The language of Lakshadweep a Union Territory of Indiais?","Tamil","Hindi","Malyaman","Telugu",3],["In which group of places the Kumbha Mela is held everytwelveyears?","Ujjain.purl;Prayag Hariwar","Prayag.Haridwar;Ujjain Nasik","Badrinath. Dwaraka","Chitakoot.ujjain;prayag Haridwar",2],["Bahubali festival is related to?","Isalam","Hinduhism","Bhudhism","Jainism",4],["Which day is observed as the World Standards  Day?","June 26","Oct14","Nov15","Dec2",2],["Who is author of Mans-ka-ans?","Khushwant Singh","Prem Chand","Jayashankar Prasad","Amrit Lal Nagar",4],["Who is the author of Meghdoot?","Vishakadatta","Valmiki","Banabhatta","Kalidas",4],["Pongal is popular festival of which state?","Karnatka","kerala","Tamil Nadu","Andhra Pradesh",2],["Ghototkach in Mahabharat was the son of?","Duryodhana","Arjuna","Yudhishthir","Bhima",4],["The first month of the Indian national calendar is?","Magha","Chaitra","Asadha","Vaiskha",2]]
levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money = 0
for i in range (0,len(question)):
	Question = question[i]
	print(f"Question For Rs:{levels[i]}")
	print(question[0])
	print(f"A. {question[1]}           B. {question[2]}")
	print(f"C. {question[3]}            D. {question[4]}")
	reply = int(input("Enter Your Number In (1-4) or 0 or quit"))
	if reply == 0:
		money = levels[i]
		break
	if reply == question[-1]:
		print(f" WOW! Correct Answer , You Have Won The Rs.",levels[i])
	elif i == 4:	
		money == 10000
	elif i == 7:	
		money == 80000 
	elif i == 10:	
		money = 320000
	else:	
		print("Wrong Answer")
		break
print(f" You can Take Home Prize Money {money}")	
























	               


