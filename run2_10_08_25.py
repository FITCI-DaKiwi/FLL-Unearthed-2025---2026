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

drive_base.settings(300)
# The main program starts here.
drive_base.use_gyro(True)
heading=0
print('tHIS iS dAIlY NeWs pREsEnTInG aLeXS BrAiNCeLl LOsS pEr SeCoNd, WhICh iS ', prime_hub.battery.voltage())
print('aLExs iQ LoSs iS  ', prime_hub.battery.current())
rightattach.run_angle(500,-95)
drive_base.straight(660)
#rightattach.run_angle(100,-400)
#now beginning to wack wack wack the silo for free food
rightattach.run_angle(500,95)
rightattach.run_angle(500,-95)
rightattach.run_angle(500,95)
rightattach.run_angle(500,-95)
rightattach.run_angle(500,95)
rightattach.run_angle(500,-95)
#finish hitting silo
drive_base.straight(200)

drive_base.turn(-66)
wait(500)
drive_base.straight(700)
wait(500)

#ready to turn to deliver a flag


# drive_base.straight(-310)
# drive_base.settings(600)
# drive_base.straight(-200)
# drive_base.straight(200)
# drive_base.straight(-400)
# drive_base.straight(200)
# wait(500)
# #drive_base.turn(45)
# wait(500)

