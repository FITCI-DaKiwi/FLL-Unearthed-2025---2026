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
drive_base.straight(-600)
drive_base.straight(185)
leftattach.run_angle(670, 90)
drive_base.turn(45)
drive_base.straight(-580)
drive_base.settings(175)
drive_base.turn(-95)
drive_base.settings(300)
drive_base.straight(-100)
drive_base.settings(500)
wait(410)
drive_base.settings(600)
drive_base.straight(-300)
drive_base.turn(-35)
drive_base.straight(200)
drive_base.turn(-20)
drive_base.straight(300)
drive_base.turn(-20)
drive_base.straight(-700)









