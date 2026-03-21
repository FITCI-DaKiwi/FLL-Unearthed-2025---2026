from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait
from A99_Turn_Exact_Funtion_V2 import turn_exact
from A99_Drive_to_Sign import drive_to_sign


hub = PrimeHub()
right = Motor(Port.A, Direction.COUNTERCLOCKWISE)
left = Motor(Port.B, Direction.CLOCKWISE)
right_side = Motor(Port.E, Direction.CLOCKWISE)
left_side = Motor(Port.F, Direction.COUNTERCLOCKWISE)
drive_base = DriveBase(right, left, 62.4, 100.9)

# from turn_exact_function import turn_exact
voltage = hub.battery.voltage()
print("Battery voltage:", voltage, "mV")

drive_base.use_gyro(True)
drive_base.straight(480)
right_side.run_angle(100,-100)
drive_base.straight(-200)
drive_base.straight(100)
right_side.run_angle(100,100)
drive_base.settings(1000,1000,500)
drive_base.curve(-125,-180)
drive_base.straight(-1500)