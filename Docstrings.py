# Docstrings in Python: Python Docstring are the string literal that appear right after the defination of a funcion, method, class,or module
# syntax of Docstring is It IS after written in function and weitten in .__doc__
# Example of docstring

def square(n):
	'''Taking the Number n, return the sqaure of n'''
	print(n**2)
square(5)	


def square(n):
	'''Takes in a number n, return the square n'''
	print(n**2)
square(5)
print(square.__doc__)

# Diffrence between with Comment and Docstrings
# Comments :
# comments are description that help programmer better understand the intent and functionality of the program. The completely ignored by the python interpeter.
# Docstrings :
# python docstrings are strings used right after the defination of a function,method,class or module . They are used to document our code.




# PEP-8 :
# PEP 8 is a document that provide guidline and beast practices on how to write the python code. It was written in 2001 by Guido Van Rossum . The priary focus of PEP 8 is to improve the reability and consistency of python code
# PEP Stand for Python Enhancement Proposal , And there are sevaral of them . A PEP is a document that describe new features proposed for python and documents aspects of python like design and style for the community.

#Zen Of Python :
# 