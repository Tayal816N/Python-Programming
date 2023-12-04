''' write a python program to translate a meassage into secret code language . Use the rules below to translate normal english into secret code language.'''
# Coding:
''' if the word contains atleast 3 character , remove the first letter and append it at the end  and now append three random character at the starting and the end 
else:
	simply reverse the string'''
# Decoding	
''' if the word contain less than 3 charcter , reverse it
else:
	rempve 3 random character from start and end. Now remove the last letter and append it to the beginning.'''

st = input("Enter The Message")
words = st.split(" ")
coding = False
if coding:
	nwords = []
	for word in words:
		if len(word) >= 3:
			r1 = "dcg"
			r2 = "uio"
			stnew = r1 + word[1:] + word[0] + r2
			nwords.append(stnew)
		else:	
			nwords.append(word[::-1])
			print(" ". join(nwords))
else:
	nwords = []
	for word in words:
		if len(word) >= 3:
			stnew = word[3:-3]
			stnew = stnew[-1] + stnew[:-1]
			nwords.append(stnew)
		else:	
			nwords.append(word[::-1])
			print(" ". join(nwords))

