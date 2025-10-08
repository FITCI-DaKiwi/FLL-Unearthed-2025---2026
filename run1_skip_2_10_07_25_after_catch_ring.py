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

drive_base.settings(400)
# The main program starts here.
drive_base.use_gyro(True)
print('tHIS iS dAIlY NeWs pREsEnTInG aLeXS BrAiNCeLl LOsS pEr SeCoNd, WhICh iS ', prime_hub.battery.voltage())
print('aLExs iQ LoSs iS  ', prime_hub.battery.current())
# drive_base.settings(400)
# drive_base.straight(205)
# wait(500)
# drive_base.turn(-40)
# wait(500)
# drive_base.straight(540)
# wait(500)
# drive_base.turn(90)
# wait(500)

# # going to hit table
# drive_base.straight(-130)
# # finish hitting table
# wait(500)
# drive_base.straight(150)
# wait(500)
# drive_base.turn(-35)
# wait(500)
# drive_base.straight(130)
# wait(500)
# leftattach.run_angle(500,-118)
# #ready to hit the flip table
# wait(500)
# drive_base.turn(-35)
# #after hitting the flip table
# wait(500)
# drive_base.turn(45)
# wait(500)
# leftattach.run_angle(500,135)
# wait(500)
# drive_base.turn(20)
# wait(500)
# drive_base.straight(235)
# wait(500)
# leftattach.run_angle(500,-180)
drive_base.straight(-30)
drive_base.turn(30)
drive_base.curve(-180,110)
drive_base.straight(-600)