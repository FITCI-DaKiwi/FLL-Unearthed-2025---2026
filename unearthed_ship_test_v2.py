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


move_straight_v1(hub, drive_base, -320, 150)
print('tHIS iS tHe dAIlY NeWs pREsEnTInG aLeXS BrAiNCeLl LOsS pEr SeCoNd, WhICh iS ', hub.battery.voltage())
# # drive_base.use_gyro(False)
move_straight_v1(hub, drive_base, -150, 100)
# put flag down
left_side.run_angle(300, 80)
move_straight_v1(hub, drive_base, 10, 500)
move_straight_v1(hub, drive_base, 300, 500)
drive_base.curve(-430,44)
# turn_exact(hub, drive_base, right, left, 90)
move_straight_v1(hub, drive_base, -322, 333)
turn_exact(hub, drive_base, right, left, 70)
# move_straight_v1(hub, drive_base, -10, 433)
wait(1000)
right_side.run_angle(500, 120)
wait(1000)
move_straight_v1(hub, drive_base, 63.7, 257)
# right_side.run_angle(1000, -90)
# move_straight_v1(hub, drive_base, -100, 15) 