from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from dakiwi_lib import turn_exact,move_straight
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

# move_straight(prime_hub,drive_base,distance,speed)
# turn_exact(prime_hub,drive_base,left,right,degree(less then 90))
drive_base.straight(-600)
drive_base.straight(185)
leftattach.run_angle(670, 90)
drive_base.turn(45)
drive_base.straight(-600)
drive_base.turn(-90)
drive_base.straight(-250)