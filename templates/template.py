from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from utils import turn_exact

hub = PrimeHub()
right = Motor(Port.A, Direction.COUNTERCLOCKWISE)
left = Motor(Port.B, Direction.CLOCKWISE)
right_side = Motor(Port.E, Direction.CLOCKWISE)
left_side = Motor(Port.F, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(right, left, 62.4, 87.5)
# color_sensor = ColorSensor(Port.C)
