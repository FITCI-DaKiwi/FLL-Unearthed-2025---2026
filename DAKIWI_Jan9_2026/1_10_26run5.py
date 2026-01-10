from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B, Direction.CLOCKWISE)
right_side = Motor(Port.E, Direction.CLOCKWISE)
left_side = Motor(Port.F, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(left, right, 62.4, 110)

#the initial position of the robot is that its horizontal
#its touching the vertical second thick line
#do the wheely thing
drive_base.use_gyro(True)
drive_base.straight(-710)
drive_base.turn(-30)
drive_base.straight(-70)
drive_base.turn(40)
drive_base.straight(-100)
drive_base.use_gyro(False)
right_side.run_angle(700,2000)
drive_base.use_gyro(True)
#Drop off the stuff
drive_base.turn(-30)
drive_base.straight(200)
drive_base.turn(63)
drive_base.straight(-550)
left_side.run_angle(100,70)
wait(1000)
#Go back to not touch the stuff just in case
drive_base.straight(500)


