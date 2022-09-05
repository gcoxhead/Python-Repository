# Write your code here :-)
import time
import random

# loop using time.sleep
while True:
    message = "\n Matt is a loser...:("
    print(message)

    f = open("loserFile.txt", "a")

    f.write(message)

    f.close()

    time.sleep(1)

