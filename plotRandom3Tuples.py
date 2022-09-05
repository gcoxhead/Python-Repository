import time
import random

while True:
    # Just keep print three random numbers in a Python tuple.

    # Data can be plotted using the mu plotter function.


    # Call sleep function
    time.sleep(0.25)

    tuple = (random.randint(0, 100), random.randint(-100, 0), random.randint(-50, 50))

    print(tuple)

    #Convert tuple into string
    tuple = str(tuple)

    #Join tuple
    data = " ".join(tuple)

    # Open txt file
    f = open("muTuple.txt", "w+")

    # Write data into txt file
    f.write(data)

    #Close txt file
    f.close()
