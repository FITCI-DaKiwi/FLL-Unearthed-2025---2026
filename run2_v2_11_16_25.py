from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor,ColorSensor
from pybricks.robotics import DriveBase
from pybricks.tools import wait
#the initial position is the right hand robot's gray tile on the 11th light square
# Set up all devices.
prime_hub = PrimeHub()
left = Motor(Port.A, Direction.CLOCKWISE)
right = Motor(Port.B, Direction.COUNTERCLOCKWISE)
leftattach = Motor(Port.E, Direction.COUNTERCLOCKWISE)
rightattach = Motor(Port.F, Direction.CLOCKWISE)
drive_base = DriveBase(right, left, 81.6, 101.7)
color_sensor = ColorSensor(Port.C)
reflection=color_sensor.reflection()

# the main code starts here
drive_base.settings(400)
# MAKE ARM UNDER HORIZONTAL OR ESLE
drive_base.use_gyro(True)
yaw=prime_hub.imu.heading()
print('the initial heading is', yaw)
print('tHIS iS dAIlY NeWs pREsEnTInG aLeXS BrAiNCeLl LOsS pEr SeCoNd, WhICh iS ', prime_hub.battery.voltage())
print('aLExs iQ LoSs iS  ', prime_hub.battery.current())
rightattach.run_angle(500,-95)
# the old first straight from run2_10_31_25 is 660 and the new is 
drive_base.straight(590)
#rightattach.run_angle(100,-400)
#now beginning to wack wack wack the silo for free food
rightattach.run_angle(850,105)
rightattach.run_angle(850,-105)
rightattach.run_angle(850,105)
rightattach.run_angle(850,-105)
rightattach.run_angle(850,105)
rightattach.run_angle(850,-80)
#fried rice have msg yummy msg
#after hitting silo
drive_base.straight(190)
#it was turn 70. now is 70
drive_base.turn(-80)
drive_base.straight(600)
wait(500)
drive_base.settings(100)
drive_base.curve(130,93)
wait(400)
drive_base.settings(400)
yaw1=prime_hub.imu.heading()
print('the current heading yaw1 is', yaw1)
drive_base.straight(-155)
drive_base.turn(-17)
rightattach.run_angle(500, -90)
wait(300)
rightattach.run_angle(500, 130)
wait(250)
drive_base.straight(100)
#finished hitting the basket
drive_base.turn(-44)
leftattach.run_angle(1000,150)
wait(300)
drive_base.straight(-385)
drive_base.straight(295)
#finished "what's on sale" mission #9 (hitting the merchant table)
yaw2=prime_hub.imu.heading()
print('the current heading yaw2 is', yaw2)
print(30-yaw2)
drive_base.turn(-yaw2 + 10)
#used to be turn 72
yaw3=prime_hub.imu.heading()
print('the current heading yaw3 is', yaw3)
#was -45

leftattach.run_angle(1000,-50)
#ready to move to fossile
drive_base.straight(-700)
#6*7=42 7-6=1 42-1=41 67=41
wait(500)
leftattach.run_angle(1000,50)
drive_base.turn(40)
# #ready to lift up the dino fossil
leftattach.run_angle(250, -80)
wait(500)
drive_base.straight(100)
# #Flag is out
drive_base.turn(20)
drive_base.straight(-400)
drive_base.turn(-45)
drive_base.straight(-350)
while True:
    drive_base.drive(200,0)
    print('1st step')
    reflection = color_sensor.reflection()   # get reflection value, which is a number
    print(reflection)

    if reflection <= 15: # because this is about the reflection percentage of the average black color
        drive_base.settings(straight_speed = 600)
        drive_base.stop()
        wait(1000)
        drive_base.stop()
        drive_base.turn(120)
        break 
# breaks the loop so that it wont happen over and over again

while True:
    drive_base.drive(200,0)
    print('1st step')
    reflection = color_sensor.reflection()   
    print(reflection)

    if reflection <= 15: 
        drive_base.settings(straight_speed = 600)
        drive_base.stop
        break