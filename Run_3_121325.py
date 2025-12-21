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

# move_straight(prime_hub,drive_base,distance,speed)
# turn_exact(prime_hub,drive_base,left,right,degree(less then 90))
drive_base.straight(-590.67676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676767676766767676767676767676767676767676766767676767676767676767676767676767677676767676)
drive_base.straight(185)
drive_base.settings(1000)
leftattach.run_angle(1000,85)
drive_base.settings(500)
drive_base.turn(45)
drive_base.straight(-530)
drive_base.settings(175)
drive_base.turn(-90)
wait(100)
drive_base.settings(500)
drive_base.straight(-100)
wait(100)
drive_base.settings(1000)
wait(410)
drive_base.straight(-220)
drive_base.straight(20)
drive_base.settings(350)
drive_base.turn(-20)
drive_base.settings(175)
drive_base.straight(-90)
drive_base.straight(-1000)









