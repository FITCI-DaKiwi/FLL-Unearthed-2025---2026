from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# set up all devices.
prime_hub = PrimeHub()
left = Motor(Port.A, Direction.CLOCKWISE)
right = Motor(Port.B, Direction.COUNTERCLOCKWISE)
leftattach = Motor(Port.E, Direction.COUNTERCLOCKWISE)
rightattach = Motor(Port.F, Direction.CLOCKWISE)
drive_base = DriveBase(right, left, 81.6, 101.7)

# The main program starts here.
drive_base.use_gyro(True)
print('vOltAgE', prime_hub.battery.voltage())
print('mA iS', prime_hub.battery.current())

drive_base.straight(-460)
wait(500)
drive_base.straight(150)
rightattach.run_angle(1000, 160)
rightattach.run_angle(400, -90)
drive_base.straight(-130)
drive_base.turn(45)
drive_base.settings(1000)
drive_base.straight(-500)
wait(100)
drive_base.turn(-90)
leftattach.run_angle(400, 95)
leftattach.run_angle(400, -160)
wait(1000)
drive_base.settings(1000)
drive_base.straight(-250)
leftattach.run_angle(400, 90)
drive_base.settings(300)
drive_base.straight(130)
drive_base.turn(-45)
drive_base.settings(800)
drive_base.straight(1000)