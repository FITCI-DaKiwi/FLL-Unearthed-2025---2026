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
drive_base.settings(400)
drive_base.straight(205)
wait(500)
drive_base.turn(-40)
wait(500)
drive_base.straight(540)
wait(500)
drive_base.turn(90)
wait(500)

# going to hit table
drive_base.straight(-130)
# finish hitting table
wait(500)
drive_base.straight(150)
wait(500)
drive_base.turn(-35)
wait(500)
drive_base.straight(130)
wait(500)
leftattach.run_angle(500,-125)
wait(500)
drive_base.turn(-30)
wait(500)
leftattach.run_angle(500,145)
wait(500)
drive_base.turn(60)
wait(500)
drive_base.straight(235)
wait(500)
leftattach.run_angle(500,-180)

# drive_base.settings(200)
# drive_base.straight(300)
# # leftattach.run_angle(100,-180)



#now beginning to wack wack wack the silo for free food
"""
# rightattach.run_angle(500,-95.67)
# drive_base.turn(30)
# rightattach.run_angle(500,95.67)
# drive_base.turn(40)
# """
# """
# drive_base.settings(900)
# #roast in peace
# drive_base.turn(2.5)
# drive_base.straight(350)
# for count in range(4):
#     leftattach.run_angle(100000,-90.5)
#     leftattach.run_angle(100000,90.5)
#     #finished wack wack wack the the silo
# leftattach.run_angle(500,-69.67)
# drive_base.straight(305)
# leftattach.run_angle(1000, 75)
# drive_base.straight(75)
# drive_base.turn(40)
# rightattach.run_angle(1000,500)


# drive_base.turn(10)
# leftattach.run_angle(1000, 75)
# drive_base.straight(120.58163)
# drive_base.turn(35)
# #drive_base.turn(-60)
# # leftattach.run_angle(500,55)
# # drive_base.straight(75)
# # drive_base.turn(-110)

# drive_base.settings(900)
# drive_base.straight(300)
# drive_base.turn(95)
# drive_base.straight(515)
# drive_base.turn(95)
# drive_base.settings(900)
# drive_base.straight(90)
# drive_base.settings(900)
# drive_base.straight(-90)
# drive_base.settings(900)
# drive_base.straight(90)
# drive_base.settings(900)
# drive_base.straight(-90)
# drive_base.settings(900)
# drive_base.straight(90)
# drive_base.settings(900)
# drive_base.straight(-90)
# """
# # rightattach.run_angle(50, -150)
# # rightattach.run_angle(200,155)

# #nEgAtIvE iS fOrWaRd
# drive_base.use_gyro(True)
# drive_base.settings(500)
# drive_base.straight(-240)
# drive_base.turn(-45)
# drive_base.straight(-296)
# drive_base.turn(45)
# wait(500)
# drive_base.settings(300)
# for count in range(3):
#     leftattach.run_angle(750,-115)
#     leftattach.run_angle(750,115)
#     wait(10)
# #finished wack wack wack the silo
# drive_base.turn(-35)
# wait(1000)
# drive_base.straight(-335)
# wait(1000)
# drive_base.turn(86)
# # BEGINNING TO STEAL ROCKS FROM THE CAVE FOR FUN BECAUSE WHY NOT
# wait(2000)
# drive_base.straight(-280)
# wait(000)
# rightattach.run_angle(500, -180)