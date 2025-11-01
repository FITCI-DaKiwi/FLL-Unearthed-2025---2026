from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
right = Motor(Port.A, Direction.COUNTERCLOCKWISE)
left = Motor(Port.B, Direction.CLOCKWISE)
right_side = Motor(Port.E, Direction.CLOCKWISE)
left_side = Motor(Port.F, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(right, left, 62.4, 110)

color_sensor = ColorSensor(Port.C)
reflection=color_sensor.reflection()

while True:
    drive_base.drive(200,0)
    print('1st step')
    reflection = color_sensor.reflection()   # get reflection value, which is a number
    print(reflection)

    if reflection <= 15: # because this is about the reflection percentage of the average black color
        drive_base.settings(straight_speed = 600)
        drive_base.stop()
        wait(1000)
        drive_base.stop()
        drive_base.turn(120)
        break # breaks the loop so that it wont happen over and over again

while True:
    drive_base.drive(200,0)
    print('1st step')
    reflection = color_sensor.reflection()   
    print(reflection)

    if reflection <= 15: 
        drive_base.settings(straight_speed = 600)
        drive_base.stop
        break