from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()
right = Motor(Port.A, Direction.COUNTERCLOCKWISE)
left = Motor(Port.B, Direction.CLOCKWISE)
right_side = Motor(Port.E, Direction.CLOCKWISE)
left_side = Motor(Port.F, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(right, left, 62.4, 110)

from Move_Turn_Functions_Agnes import move_straight, turn_exact
heading = hub.imu.heading()
print('before start, the heading is:', heading)
# move forward
move_straight(hub,drive_base,1,150)
move_straight(hub,drive_base,-725,150)
# turn 90 degree
turn_exact(hub, drive_base, left, right, -90)
heading = hub.imu.heading()
print('before start, the heading is:', heading)
# move forward
move_straight(hub,drive_base,-10,50)
move_straight(hub,drive_base,127,50)
left.stop()
right.stop()

# do the mission
# right arm lift
right_side.run_angle(40,-64, wait=True)
# left arm lift
left_side.run_angle(140,-15, wait=True)
wait(2000)
# right arm up
right_side.run_angle(140, -40, wait=True)

# move back
# from Move_Turn_Functions_Agnes import move_straight, turn_exact
move_straight(hub,drive_base,-120,50)
left.stop()
right.stop()

# # lift left arm up
# left_side.run_angle(140,-70)
# # right_side.run_angle(140,-90)