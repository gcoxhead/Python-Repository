# Write your code here :-)
# Examples of casting data types to ensure value

#Take in input as a string from the user.
hoursSleep = input("How many hours do you sleep each night?\n")

#cast hoursSleep to an integer data type and perform calculation.
hoursWeek = int(hoursSleep)*7

#print message to console
print("You sleep",hoursWeek, "hours per week!\n")

#Create float variable
weeksPerMonth = 4.35

#Perform calulation but cast back into a user friendly integer
hoursMonth = int(hoursWeek*weeksPerMonth)

print ("That's",hoursMonth, "hours each month!")
