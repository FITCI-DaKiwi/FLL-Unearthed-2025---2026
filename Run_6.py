from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
left = Motor(Port.A, Direction.CLOCKWISE)
right = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_side = Motor(Port.E, Direction.CLOCKWISE)
left_side = Motor(Port.F, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(left, right, 62.4, 110)


#Drop off the stuff
drive_base.straight(-100)
drive_base.turn(115)
drive_base.settings(1000)
drive_base.straight(-900)
right_side.run_angle(100,50)

