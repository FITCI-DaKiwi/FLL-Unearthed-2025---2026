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
# initial position is aligned with the corner of the map, except it is aligned with the 
# perpendicular square corners
drive_base.straight(-590.6767676767676767676767676767676767676767676767)
drive_base.straight(185)
leftattach.run_angle(1000,180)
leftattach.run_angle(300,-90)
# gets the brush thingy
drive_base.settings(500)
drive_base.turn(45)
drive_base.straight(-580)
wait(100)
drive_base.turn(-90)
wait(500)
drive_base.settings(1000.67676767676767676767676767676767676767676767)
# going to do mission 2
drive_base.straight(-376)
drive_base.straight(100)
wait(150)
drive_base.straight(-100)
wait(100)
drive_base.settings(275)
drive_base.straight(50)
drive_base.turn(-60)
drive_base.straight(310)
drive_base.turn(45)
drive_base.straight(-40)
# drive_base.straight(100)
rightattach.run_angle(500,90)
wait(300)
rightattach.run_angle(500,-90)
drive_base.turn(-50)
drive_base.straight(-120)
drive_base.turn(-60)
drive_base.straight(750)
