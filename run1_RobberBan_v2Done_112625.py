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

#left side of the robot lines up with the third thin line/first thick line from the left

drive_base.settings(300)
# The main program starts here.
drive_base.use_gyro(True)
prime_hub.imu.reset_heading(0)

yaw=prime_hub.imu.heading()
print(yaw)
print('tHIS iS dAIlY NeWs pREsEnTInG aLeXS BrAiNCeLl LOsS pEr SeCoNd, WhICh iS ', prime_hub.battery.voltage())
print('aLExs iQ LoSs iS  ', prime_hub.battery.current())
drive_base.settings(250)
drive_base.straight(630)
wait(500)
drive_base.turn(50)
wait(500)
# going to hit red bar
drive_base.straight(-217)
wait(500)
# finish hitting red bar
drive_base.straight(160)
drive_base.turn(-50)
drive_base.straight(325)
drive_base.turn(-115)
#finish hitting boulder and table
#reverse 40
yaw1=prime_hub.imu.heading()
print(yaw1)
drive_base.turn(62)
# was 60 and 135
drive_base.straight(-125)
wait(500)
drive_base.turn(-40)
# drive_base.turn(-5)
drive_base.settings(200)
drive_base.straight(-210)
rightattach.run_angle(500,85)
# drive_base.turn(7)
drive_base.settings(1000)
drive_base.straight(-290)

"""
wait(500)
drive_base.straight(160)
wait(500)
#facing the 2nd mission table
drive_base.turn(-30)
drive_base.straight(-10)
wait(500)
#turning the arm, using yellow fork to hit, raise it higher from -118 to -120
leftattach.run_angle(500,-125)
drive_base.straight(90)
#ready to hit the flip table
wait(100)
drive_base.turn(-32)
#after hitting the flip table
wait(100)
#turn from 42 to 32 02:37 pm
drive_base.turn(28)
wait(500)
#everything works fine until here. finish hitting the table and facing the 3 balls
wait(500)
leftattach.run_angle(500,125)
wait(500)
#used to be turn 20, now 25
drive_base.turn(29)
wait(500)
#new on 10/22 11:36am
drive_base.straight(235)
wait(500)
leftattach.run_angle(700,-180)
#ready to go home
#facing home
wait(500)
drive_base.straight(-30)
drive_base.settings(100)
drive_base.turn(60)
drive_base.settings(800)
drive_base.straight(-335)
drive_base.turn(50)
drive_base.straight(900)
"""