from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Set up all devices.
prime_hub = PrimeHub()
left = Motor(Port.A, Direction.CLOCKWISE)
right = Motor(Port.B, Direction.COUNTERCLOCKWISE)
leftattach = Motor(Port.E, Direction.COUNTERCLOCKWISE)
rightattach = Motor(Port.F, Direction.CLOCKWISE)
drive_base = DriveBase(right, left, 81.6, 101.7)


# The main program starts here.
drive_base.use_gyro(True)
print('vOltAgE', prime_hub.battery.voltage())
print('mA iS', prime_hub.battery.current())

drive_base.settings(400)
drive_base.straight(350)
drive_base.turn(45)
drive_base.straight(510)
drive_base.turn(-43)
drive_base.straight(105)
drive_base.turn(-49)
drive_base.settings(175)
drive_base.straight(375)
drive_base.settings(400)
drive_base.turn(-70)
drive_base.settings(250)
drive_base.straight(300)
drive_base.straight(-400)
drive_base.turn(-60)
drive_base.settings(375)
drive_base.straight(1050)