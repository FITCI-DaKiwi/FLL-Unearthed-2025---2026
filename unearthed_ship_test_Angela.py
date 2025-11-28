from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right = Motor(Port.B, Direction.CLOCKWISE)
right_side = Motor(Port.E, Direction.CLOCKWISE)
left_side = Motor(Port.F, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(left, right, 62.4, 113)
heading=0

# the initial position is:
# back: 2nd thin line 
# side: dark black line
# dead fossilized chicken initial position is pointing up
drive_base.use_gyro(True)
drive_base.settings(250)
drive_base.straight(-375)
print('tHIS iS dAIlY NeWs pREsEnTInG aLeXS BrAiNCeLl LOsS pEr SeCoNd, WhICh iS ', hub.battery.voltage())
# drive_base.use_gyro(False)
drive_base.settings(straight_speed = 300)
drive_base.straight(-150)
## put flag down
# left_side.run_angle(300, 100)
drive_base.straight(10)
drive_base.straight(300)
left_side.run_angle(1000, 100)
drive_base.curve(radius = 200, angle = 33)
drive_base.turn(-40)
drive_base.straight(-800)
drive_base.turn(60)
