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

drive_base.use_gyro(True)
drive_base.settings(straight_speed = 300)
drive_base.straight(370)
drive_base.settings(straight_speed = 700)
drive_base.straight(250)
drive_base.settings(straight_speed = 1000)
drive_base.straight(-10)
drive_base.straight(-340)
drive_base.curve(radius = 250, angle = -35)
