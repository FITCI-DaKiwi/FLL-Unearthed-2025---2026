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
color_sensor = ColorSensor(Port.C)
reflection=color_sensor.reflection()
# the main code starts here
drive_base.settings(400)
# MAKE ARM UNDER HORIZONTAL OR ESLE
drive_base.use_gyro(True)
yaw=prime_hub.imu.heading()
print('tHIS iS dAIlY NeWs pREsEnTInG aLeXS BrAiNCeLl LOsS pEr SeCoNd, WhICh iS ', prime_hub.battery.voltage())
print('aLExs iQ LoSs iS  ', prime_hub.battery.current())


drive_base.turn(-65)
leftattach.run_angle(1000, -120)
drive_base.straight(-260)
wait(500)
#under dino now
leftattach.run_angle(200,40)
#curve(+300, -1xx) is the correct direction to backout#
# drive_base.curve(300,-120)# wait(500)
# drive_base.straight(200)
# wait(100)
drive_base.turn(25)
wait(500)
leftattach.run_angle(200,30)
wait(500)
drive_base.turn(-115)

# drive_base.straight(800)



# drive_base.settings(400,200,60,120)
# drive_base.turn(65)

# drive_base.settings(400)
# drive_base.straight(100)
# drive_base.straight(-30)
# drive_base.turn(30)
# leftattach.run_angle(1000,150)
# wait(100)
# # leftattach.run_angle(1000,-150)
# drive_base.turn(-25)
# drive_base.straight(-400)

