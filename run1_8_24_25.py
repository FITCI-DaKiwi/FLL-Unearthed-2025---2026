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
#drive_base.straight(-485)
#rightattach.run_angle(100,-400)
drive_base.settings(900)
drive_base.straight(450)
for count in range(4):
    leftattach.run_angle(100000,-83.5)
    leftattach.run_angle(100000,83.5)
leftattach.run_angle(500,-60)
drive_base.straight(300)
drive_base.turn(10)
drive_base.straight(15)
drive_base.turn(-60)
# leftattach.run_angle(500,55)
# drive_base.straight(75)
# drive_base.turn(-110)



"""
drive_base.settings(900)
drive_base.straight(300)
drive_base.turn(95)
drive_base.straight(515)
drive_base.turn(95)
drive_base.settings(900)
drive_base.straight(90)
drive_base.settings(900)
drive_base.straight(-90)
drive_base.settings(900)
drive_base.straight(90)
drive_base.settings(900)
drive_base.straight(-90)
drive_base.settings(900)
drive_base.straight(90)
drive_base.settings(900)
drive_base.straight(-90)
"""