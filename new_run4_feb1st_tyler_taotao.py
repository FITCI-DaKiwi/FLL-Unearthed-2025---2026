from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

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

drive_base.settings(400)
prime_hub.imu.reset_heading(0)
drive_base.straight(-510)
# doing mission 1
rightattach.run_angle(300, -130)
drive_base.straight(-60)
drive_base.straight(120)
drive_base.straight(-60)
rightattach.run_angle(400, 170)
wait(100)
rightattach.run_angle(400, -90)
drive_base.turn(40)
drive_base.straight(-340)
# SUPER ACCURATE TURN NEEDED!
drive_base.turn(-80)
wait(500)
drive_base.settings(800)
# doing mission 2
drive_base.settings(1000)
drive_base.straight(-300)
wait(500)
drive_base.straight(300)
drive_base.turn(75)
drive_base.straight(967)
# end of code