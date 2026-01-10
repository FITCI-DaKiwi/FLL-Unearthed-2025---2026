from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from dakiwi_lib import move_straight, move_straight_v1, turn_exact

hub = PrimeHub()
left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B, Direction.CLOCKWISE)
right_side = Motor(Port.E, Direction.CLOCKWISE)
left_side = Motor(Port.F, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(left, right, 62.4, 113)
# heading=0

# the initial position is:
# back: 3rd thin line 
# side: dark black line
# dead fossilized chicken initial position is pointing up
# drive_base.use_gyro(True)

heading = hub.imu.heading()
print('before start, the heading is:', heading)

drive_base.use_gyro(True)
# move_straight_v1(hub, drive_base, -330, 150)
drive_base.settings(straight_speed = 300)
drive_base.straight(-367)
print('tHIS iS tHe dAIlY NeWs pREsEnTInG aLeXS BrAiNCeLl LOsS pEr SeCoNd, WhICh iS ', hub.battery.voltage())
# move_straight_v1(hub, drive_base, -150, 100)
drive_base.settings(straight_speed = 100)
drive_base.straight(-120)
# put flag down
left_side.run_angle(130, 70)
# move_straight_v1(hub, drive_base, 10, 500)
drive_base.settings(straight_speed = 300)
drive_base.straight(10)
# move_straight_v1(hub, drive_base, 300, 500)
drive_base.straight(300)
# where we leave mission 12
drive_base.curve(-230,44) 
# drive_base.use_gyro(True)
drive_base.straight(-285)
drive_base.turn(48)
drive_base.straight(-725)
drive_base.turn(42)
# pull the pan
drive_base.settings(straight_speed = 103)
drive_base.straight(130)
drive_base.settings(straight_speed = 73)
drive_base.straight(-20)
drive_base.straight(20)
# drive_base.straight(-20)
# drive_base.straight(20)
# wiggle
drive_base.turn(10)
drive_base.turn(-10)
# drive_base.turn(10)
# drive_base.turn(-10)

# drive_base.straight(-20)
# drive_base.straight(20)
drive_base.settings(straight_speed = 300)
drive_base.straight(-200)
drive_base.curve(-300,60)
# homebase time! lets try not to lose a precision token plz
drive_base.settings(straight_speed = 1000)
drive_base.straight(-200)

# the five lucky words for this mission 🍀
# canidates:
# 1. banana 🍌 NO
# 2. discovery 💡 NO
# 3. hoodie 👚 MAYBE
# 4. unicorn 🦄 YES!!!
# 5. maple leaf 🍁
# 6. cookie 🍪 YES!!!
# 7. cheese & crackers 🧀 HELL NAH
# 8. french fries 🍟 YES!!!
# 9. putty 😁 MAYBE
# 10. gummy bear 🧸