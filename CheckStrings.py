#Check if two strings are equal
import re

string_one = "Bubble"
string_two = "Bobble"
string_three = "Arcade"
string_four = "Bubble"

def check_strings(first_string, second_string):
    if first_string == second_string:
        print("True")
        
        return True
    else:
        print ("False")
        
        return False
    
check_strings(string_one, string_four)  

