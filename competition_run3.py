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

rightattach.run_angle(300, -90)
drive_base.straight(-480)
wait(500)
drive_base.straight(175)
# getting brush to home
rightattach.run_angle(1000, 160)
rightattach.run_angle(400, -90)
drive_base.straight(-130)
drive_base.turn(45)
drive_base.settings(1000)
drive_base.straight(-500)
wait(100)
drive_base.turn(-90)
# delivering flag
leftattach.run_angle(400, 95)
leftattach.run_angle(400, -151)
wait(500)
drive_base.settings(400)
# going to do mission 2
drive_base.straight(-250)
drive_base.straight(100)
drive_base.straight(-100)
leftattach.run_angle(400, 90)
drive_base.settings(300)
drive_base.straight(200)
drive_base.turn(60)
drive_base.settings(800)
# going home
drive_base.straight(900)