#Program to check if a flat can be rented

#Ask the user to enter their age
input_age = input("Enter your age:")

#Convert the input_age string into an integer
age = int(input_age)

# Check the condition of the users age
if age >= 21:
    #Ask the users salary
    input_salary = input("Enter your salary: ")
    salary = int(input_salary)
    
    #Check the condition of users salary
    if salary > 15000:
        print("You can rent the flat")
    else: 
        print("You don't earn enough to rent the flat")        

elif age >= 18 and age <21:
    #Ask user if they have a guarantor
    guarantor = input("Do you have a guarantor (Yes/no): ")
    
    #Check condition of guarantor
    if guarantor == "Yes":
        print ("We will need to contact your guarantor")

    else:
        print("I am sorry but you need a guarantor")

else:
    print("I am sorry but you can't rent the flat")

                    