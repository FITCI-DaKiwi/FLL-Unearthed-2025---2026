from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait
#the initial position is the right hand robot's gray tile on the 10th light square
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
yaw=prime_hub.imu.heading()
print('the initial heading is', yaw)
print('tHIS iS dAIlY NeWs pREsEnTInG aLeXS BrAiNCeLl LOsS pEr SeCoNd, WhICh iS ', prime_hub.battery.voltage())
print('aLExs iQ LoSs iS  ', prime_hub.battery.current())
rightattach.run_angle(500,-110)
#was -95
drive_base.straight(660)
#rightattach.run_angle(100,-400)
#now beginning to wack wack wack the silo for free food
rightattach.run_angle(850,105)
rightattach.run_angle(850,-105)
rightattach.run_angle(850,105)
rightattach.run_angle(850,-105)
rightattach.run_angle(850,105)
rightattach.run_angle(850,-80)
#fried rice have msg yummy msg
#fried rice have msg yummy msg
#after hitting silo
drive_base.straight(215)
#it was turn 70. now is 70
drive_base.turn(-80)
drive_base.straight(580)
#was 600
#wait(500)
drive_base.settings(100)
drive_base.curve(130,93)
wait(400)
drive_base.settings(400)
yaw1=prime_hub.imu.heading()
print('the current heading yaw1 is', yaw1)
drive_base.straight(-140)
drive_base.turn(-17)
rightattach.run_angle(500, -75)
rightattach.run_angle(500, 145)
#finished hitting the basket
drive_base.turn(-45)
leftattach.run_angle(1000,140) # it used to be 150
wait(150)
drive_base.straight(-320)
#finished hitting the merchant table
drive_base.straight(290)
# was 145,
yaw2=prime_hub.imu.heading()
print('the current heading yaw2 is', yaw2)
print(30-yaw2)
drive_base.turn(-yaw2 + 25)
#used to be turn 72
yaw3=prime_hub.imu.heading()
print('the current heading yaw3 is', yaw3)
leftattach.run_angle(1000,-50)
#passing dinosaur
drive_base.straight(-760)
drive_base.turn(60)
drive_base.settings(1000)
drive_base.straight(-1000)
#HOME

# drive_base.turn(20)
# drive_base.straight(-200)
# wait(500)
# leftattach.run_angle(1000,45)
# #park next to the fossil
# drive_base.straight(120)
# leftattach.run_angle(1000,-50)
# drive_base.straight(100)
# wait(500)
# drive_base.straight(-500)

# drive_base.turn(40)
# drive_base.straight(-150)
# wait(400)
# drive_base.straight(50)
# #ready to lift up the dino fossil
# leftattach.run_angle(250, -80)
# drive_base.turn(-50)
#i have fried rice syndrome i will be back tomorrow
# wait(500)
# drive_base.straight(-120)
# #Flag is out
# wait(500)
# drive_base.turn(-20)
# drive_base.straight(400)
# drive_base.turn(45)
# wait(500)
# drive_base.straight(-35)
# #ready to hit basket
# leftattach.run_angle(1000,150)
# yaw1=prime_hub.imu.heading()
# print('the current heading is', yaw1)
# # finishing hitting basket
# drive_base.turn(-12)
# wait(500)
# drive_base.straight(-420)
# #finish pushing the table UP
# wait(500)
# drive_base.straight(140)
# drive_base.turn(-50)
# drive_base.straight(895)
# wait(500)
# #arrived next to the dino bones
# drive_base.turn(55)
# drive_base.straight(-85)
# wait(10000)


# leftattach.run_angle(1000,-150)
# #fried rice have msg yummy msg
# #fried rice have msg yummy msg
# #fried rice have msg yummy msg
# #curve(+300, -1xx) is the correct direction to backout#
# #drive_base.curve(300,-120)# wait(500)
# # drive_base.straight(200)
# # wait(100)
# # drive_base.turn(-50)
# # drive_base.straight(800)



# # drive_base.settings(400,200,60,120)
# # drive_base.turn(65)

# # drive_base.settings(400)
# # drive_base.straight(100)
# # drive_base.straight(-30)
# # drive_base.turn(30)
# # leftattach.run_angle(1000,150)
# # wait(100)
# # # leftattach.run_angle(1000,-150)
# # drive_base.turn(-25)
# # drive_base.straight(-400)

# # drive_base.settings(500)
# # drive_base.straight(700)
# drive_base.straight(-500)