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
drive_base = DriveBase(right, left, 62.0, 101.7)


# The main program starts here.
drive_base.use_gyro(True)
print('tHIS iS dAIlY NeWs pREsEnTInG aLeXS BrAiNCeLl LOsS, WhICh iS ', prime_hub.battery.voltage())
print('mA iS', prime_hub.battery.current())
#drive_base.straight(-485)
#rightattach.run_angle(100,-400)
#now beginning to wack wack wack the silo for free food
drive_base.settings(900)
#roast in peace like a good boy
drive_base.turn(2.5)
drive_base.straight(350)
for count in range(4):
    leftattach.run_angle(100000,-83.5)
    leftattach.run_angle(100000,83.5)
    #finished wack wack wack the the silo
leftattach.run_angle(500,-57)
drive_base.straight(300)
leftattach.run_angle(1000, 75)
drive_base.straight(95)
"""
drive_base.turn(10)
leftattach.run_angle(1000, 75)
drive_base.straight(120.58163)
drive_base.turn(35)
#drive_base.turn(-60)
# leftattach.run_angle(500,55)
# drive_base.straight(75)
# drive_base.turn(-110)

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