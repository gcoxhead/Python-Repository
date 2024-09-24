from datetime import datetime

def isWeekday(mydate):
    day = mydate.weekday()
    
    if day<5:
        return True
    else:
        return False

if isWeekday(datetime.now()):
    print("It's a weekday!")
    
else:
    print("It's a weekend!")
    