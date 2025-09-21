from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
left=Motor(Port.A, Direction.CLOCKWISE)
right=Motor(Port.B, Direction.COUNTERCLOCKWISE)
front=Motor(Port.E, Direction.CLOCKWISE)
top=Motor(Port.F, Direction.COUNTERCLOCKWISE)
drive_base=DriveBase(left, right, 90, 90)
heading=0
#drive_base.use_gyro(True)
drive_base.turn(5)
drive_base.straight(250)
drive_base.use_gyro(True)
drive_base.straight(230)
#beginning to wack wack wack the mountain
front.run_angle(600, 85)
front.run_angle(1000, -85)
front.run_angle(10000, 85)
front.run_angle(1000, -85)
#drive_base.turn(2)
front.run_angle(10000, 85)
front.run_angle(1000, -85)
drive_base.turn(4)
front.run_angle(10000, 85)
front.run_angle(1000, -85)
drive_base.turn(6)

drive_base.use_gyro(False)


#doning wack wack wack the mountain
#beginning rock levering
drive_base.turn(5)
drive_base.straight(95)
drive_base.use_gyro(True)
drive_base.straight(150)
drive_base.use_gyro(False)
front.run_angle(600, 67)
drive_base.straight(95)
drive_base.turn(62)
# after hit boulders
front.run_angle(600,-67)
drive_base.straight(135)
drive_base.turn(230)
drive_base.straight(-450)