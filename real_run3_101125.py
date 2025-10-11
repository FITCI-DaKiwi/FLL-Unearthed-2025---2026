from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

prime_hub = PrimeHub()
left = Motor(Port.A, Direction.CLOCKWISE)
right = Motor(Port.B, Direction.COUNTERCLOCKWISE)
leftattach = Motor(Port.E, Direction.COUNTERCLOCKWISE)
rightattach = Motor(Port.F, Direction.CLOCKWISE)
drive_base = DriveBase(right, left, 81.6, 101.7)

drive_base.use_gyro(True)
print('vOltAgE', prime_hub.battery.voltage())
print('mA iS', prime_hub.battery.current())

# initial position is the position is where the attachment is slightly lower than 
# flat, and the front of the robot is aligned with the 18th line and the right 
# side of the robot is aligned with the 11th line
drive_base.straight(725)
drive_base.settings(200)
drive_base.straight(-200)
drive_base.settings(275)
drive_base.straight(67)
# wait(1250)
drive_base.settings(400)
drive_base.turn(10)
drive_base.turn(-10)
drive_base.turn(10)
drive_base.turn(-10)
drive_base.settings(200)
leftattach.run_angle(500, 135)