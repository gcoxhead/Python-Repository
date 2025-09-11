
""" 
@author: garycoxhead

"""

#import modules
import string
from random import *


def generate_password():
	characters = string.ascii_letters + string.punctuation  + string.digits
	
	password =  "".join(choice(characters) for x in range(randint(8, 16)))
	
	new_password = password
	
	print ("\nYour new password is " + password)
	print ("\nPlease keep your password safe and secure\n")
	
	return new_password

generate_password()
