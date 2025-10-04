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
print('tHIS iS dAIlY NeWs pREsEnTInG aLeXS BrAiNCeLl LOsS pEr SeCoNd, WhICh iS ', prime_hub.battery.voltage())
print('aLExs iQ LoSs iS  ', prime_hub.battery.current())
#drive_base.straight(-485)
#rightattach.run_angle(100,-400)
#now beginning to wack wack wack the silo for free food
"""
rightattach.run_angle(500,-95.67)
drive_base.turn(30)
rightattach.run_angle(500,95.67)
drive_base.turn(40)
"""
"""
drive_base.settings(900)
#roast in peace
drive_base.turn(2.5)
drive_base.straight(350)
for count in range(4):
    leftattach.run_angle(100000,-90.5)
    leftattach.run_angle(100000,90.5)
    #finished wack wack wack the the silo
leftattach.run_angle(500,-69.67)
drive_base.straight(305)
leftattach.run_angle(1000, 75)
drive_base.straight(75)
drive_base.turn(40)
rightattach.run_angle(1000,500)


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
# rightattach.run_angle(50, -150)
# rightattach.run_angle(200,155)

#nEgAtIvE iS fOrWaRd
drive_base.use_gyro(True)
drive_base.straight(-206)
drive_base.turn(-45)
drive_base.straight(-375)
drive_base.turn(55)
for count in range(4):
    leftattach.run_angle(1000,-115)
    leftattach.run_angle(1000,115)
    wait(10)
#finished wack wack wack the the silo
drive_base.turn(-30)
wait(500)
drive_base.straight(-250)
wait(500)
drive_base.turn(82)
#BEGINNING TO STEAL ROCKS FROM THE CAVE FOR FUN BECAUSE WHY NOT
wait(500)
drive_base.straight(-205)
drive_base.turn(-20)
rightattach.run_angle(500, -180)