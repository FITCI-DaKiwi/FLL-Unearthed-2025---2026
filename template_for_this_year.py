from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
right = Motor(Port.A Direction.CLOCKWISE)
left = Motor(Port.B Direction.COUNTERCLOCKWISE)
right_side = Motor(Port.E Direction.CLOCKWISE)
left_side = Motor(Port.E Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(right, left, 62.4, 110)

