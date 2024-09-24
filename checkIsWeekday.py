from datetime import datetime

def isWeekday(mydate):
    day = mydate.weekday()
    
    if day<5:
        return True
    else:
        return False

print(isWeekday(datetime.now()))