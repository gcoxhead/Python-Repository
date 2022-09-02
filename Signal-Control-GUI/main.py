# Please note: This program requires installation of the GPIO Zero interface 
# For more info please visit : 
# https://gpiozero.readthedocs.io/en/stable/installing.html

from guizero import App, Text, PushButton
from gpiozero import TrafficLights

lights = TrafficLights(22, 27, 17)

app=App("Signal Controller", layout="grid")

Text(app, "Control 1", grid=[0,0])
PushButton(app, command=lights.red.on, text="on", grid=[1,0])
PushButton(app, command=lights.red.off, text="off", grid=[2,0])
PushButton(app, command=lights.red.blink, text ="blink", grid =[3,0])

Text(app, "Control 2", grid=[0,1])
PushButton(app, command=lights.amber.on, text="on", grid=[1,1])
PushButton(app, command=lights.amber.off, text="off", grid=[2,1])
PushButton(app, command=lights.amber.blink, text ="blink", grid =[3,1])

Text(app, "Control 3", grid=[0,2])
PushButton(app, command=lights.green.on, text="on", grid=[1,2])
PushButton(app, command=lights.green.off, text="off", grid=[2,2])
PushButton(app, command=lights.green.blink, text ="blink", grid =[3,2])

Text(app, "All", grid=[0,3])
PushButton(app, command=lights.green.on, text="on", grid=[1,3])
PushButton(app, command=lights.green.off, text="off", grid=[2,3])
PushButton(app, command=lights.green.blink, text ="blink", grid =[3,3])

app.display()
