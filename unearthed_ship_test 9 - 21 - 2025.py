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

# the initial position is:
# back: 2nd thin line 
# side: dark black line
drive_base.use_gyro(False)
drive_base.settings(straight_speed = 300)
drive_base.straight(-375)
drive_base.use_gyro(False)
drive_base.settings(straight_speed = 300)
drive_base.straight(-150)
drive_base.settings(straight_speed = 300)
right_side.run_angle(300, 120)
drive_base.straight(10)
drive_base.straight(340)
right_side.run_angle(1000, -120)
