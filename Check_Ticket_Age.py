age = 0

def takeUserAge():
    global age
    _age = input("Please enter your age:")
    
    print("You are",_age, "years old")
    age = int(_age)
    return age
                

def checkAge(age):
    
    adult_ticket = age >= 16
    senior_ticket = age >= 65
    child_ticket = age <= 15
    
    if age >= 65:
        print("Senior Ticket", senior_ticket)
        
    elif age > 15:
        print("Adult Ticket", adult_ticket)
        
    else:
        print("Child Ticket", child_ticket)

takeUserAge()

checkAge(age)
    

