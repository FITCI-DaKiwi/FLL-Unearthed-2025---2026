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


while True:
    drive_base.settings(straight_speed = 100)
    #drive_base.straight(400)
    drive_base.drive(200,0)
    print('1st step')
    reflection = color_sensor.reflection()   # get reflection value, which is a number
    print(reflection)

    if reflection >= 30 and reflection <= 40: # b/c the color red's reflection number is always between the numbers 30 and 40
        drive_base.settings(straight_speed = 600)
        drive_base.straight(200)
        drive_base.straight(-300)
        print('girls are better than boys')
        break

