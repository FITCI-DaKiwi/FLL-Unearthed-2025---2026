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
# MAKE ARM UNDER HORIZONATL OR ESLE
drive_base.use_gyro(True)
heading=0
print('tHIS iS dAIlY NeWs pREsEnTInG aLeXS BrAiNCeLl LOsS pEr SeCoNd, WhICh iS ', prime_hub.battery.voltage())
print('aLExs iQ LoSs iS  ', prime_hub.battery.current())
rightattach.run_angle(500,-95)
drive_base.straight(680)
#rightattach.run_angle(100,-400)
#now beginning to wack wack wack the silo for free food
rightattach.run_angle(500,105)
rightattach.run_angle(500,-105)
rightattach.run_angle(500,105)
rightattach.run_angle(500,-105)
rightattach.run_angle(500,105)
rightattach.run_angle(500,-105)
#after hitting silo
drive_base.straight(215)
drive_base.turn(-70)
drive_base.straight(625)
wait(500)
drive_base.straight(-120)
#Flag is out
wait(500)
drive_base.turn(-20)
drive_base.straight(400)
drive_base.turn(50)
wait(500)
drive_base.straight(-25)
#ready to hit basket
leftattach.run_angle(1000,150)
#finishing hitting basket
drive_base.turn(-10)
wait(100)
drive_base.straight(-370)
wait(500)
drive_base.straight(200)
wait(100)
drive_base.turn(-50)
drive_base.straight(800)



# drive_base.settings(400,200,60,120)
# drive_base.turn(65)

# drive_base.settings(400)
# drive_base.straight(100)
# drive_base.straight(-30)
# drive_base.turn(30)
# leftattach.run_angle(1000,150)
# wait(100)
# # leftattach.run_angle(1000,-150)
# drive_base.turn(-25)
# drive_base.straight(-400)

# drive_base.settings(500)
# drive_base.straight(700)
# drive_base.straight(-500)