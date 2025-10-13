from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
right = Motor(Port.A, Direction.CLOCKWISE)
left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_side = Motor(Port.E, Direction.CLOCKWISE)
left_side = Motor(Port.F, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(right, left, 62.4, 110)

drive_base.straight(200)
drive_base.turn(110)
drive_base.settings(straight_speed = 100)
drive_base.settings(straight_speed = 50)
drive_base.straight(100)
left_side.run_angle(100,-15)
drive_base.settings(straight_speed = 100)
drive_base.straight(-200)
left_side.run_angle(500,-20)

