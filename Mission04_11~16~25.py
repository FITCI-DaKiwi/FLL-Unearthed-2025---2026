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

def gyro_turn(target_angle, speed=200):
    # Reset gyro
    hub.imu.reset_heading(0)
    
    while True:
        # Try whichever one your hub supports
        try:
            current_angle = hub.imu.heading()
        except:
            current_angle = hub.imu.angle()
        
        # Check if we've turned far enough
        if abs(current_angle) >= abs(target_angle):
            break
        
        if target_angle > 0:
            left.run(speed)
            right.run(-speed)
        else:
            left.run(-speed)
            right.run(speed)
    
    # Stop
    left.stop()
    right.stop()
    wait(200)



# drive_base.settings(straight_speed = 190)
# drive_base.straight(80)
# left_side.run_angle(60, -100)
# right_side.run_angle(350, -100)
# left_side.run_angle(100, 30)
# drive_base.straight(-100)
# IF UR SEEING THIS THEN "HI"
drive_base.settings(straight_speed=300)
drive_base.straight(-810)
drive_base.straight(100)
wait(500)
gyro_turn(85)
left_side.run_angle(500, 93)
right_side.run_angle(500, 155)
drive_base.settings(straight_speed=70)
drive_base.straight(138)
right_side.run_angle(140,-77)
left_side.run_angle(140,-10)
