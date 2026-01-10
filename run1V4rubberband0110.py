from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Set up all devices.
prime_hub = PrimeHub()
left = Motor(Port.A, Direction.CLOCKWISE)
right = Motor(Port.B, Direction.COUNTERCLOCKWISE)
leftattach = Motor(Port.E, Direction.COUNTERCLOCKWISE)
rightattach = Motor(Port.F, Direction.CLOCKWISE)
drive_base = DriveBase(right, left, 81.6, 101.7)

#left grey plate of the robot lines up with the third thin line/first thick line from the left

drive_base.settings(300)
# The main program starts here.
drive_base.use_gyro(True)
prime_hub.imu.reset_heading(0)

yaw=prime_hub.imu.heading()
print('tHiS sTeAk Is RaW', yaw)
print('tHIS iS dAIlY NeWs pREsEnTInG aLeXS BrAiNCeLl LOsS pEr SeCoNd, WhICh iS ', prime_hub.battery.voltage())
print('aLExs iQ LoSs iS  ', prime_hub.battery.current())
drive_base.settings(250)
drive_base.straight(650)#+20 morning of 1/10/26
drive_base.turn(50)
# going to hit red bar
drive_base.straight(-220)
# finish hitting red bar
drive_base.straight(170) #added 5 morning of 1/10/26
drive_base.turn(-50)
drive_base.straight(265)#-25 morning of 1/10/26
#ready to hit boulder
drive_base.settings(turn_rate=240)
drive_base.turn(-120)
#was -115
#finish hitting boulder and table
#reverse 40
yaw1=prime_hub.imu.heading()
print('tHiS sTeAk iS aLsO rAw', yaw1)
drive_base.straight(100)#subtracted 5 from morning of 1/10/26
drive_base.turn(30)
drive_base.straight(-380)
#should stopped at the blue line
# wait(500)
# drive_base.turn(-40)

# drive_base.settings(200)
# drive_base.straight(-210)
rightattach.run_angle(500,95)

drive_base.settings(1000)
drive_base.straight(-260)
drive_base.turn(15)
# drive_base.turn(-35)
