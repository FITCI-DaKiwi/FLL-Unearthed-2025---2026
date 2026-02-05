from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
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

# Wheel diameter: 81.6mm, Axle track: 101.7mm
drive_base = DriveBase(left, right, 81.6, 101.7)
drive_base.use_gyro(True)

# PID Constants - You may need to tweak these based on robot weight
KP_DRIVE = 1.5
KP_TURN = 1.2
KI = 0.01  # Small "nudge" for long-distance accuracy

# --- 2. MISSION LIBRARY FUNCTIONS ---

def drive_straight_pid(distance_mm, speed, target_angle):
    """Drives straight at a specific heading using PID."""
    drive_base.reset()
    integral = 0
    while abs(drive_base.distance()) < distance_mm:
        error = target_angle - prime_hub.imu.heading()
        integral += error
        correction = (error * KP_DRIVE) + (integral * KI)
        
        drive_base.drive(speed, correction)
        wait(10)
    drive_base.stop()

# --- THE VOLTAGE CHECK --- Not necessary but could be useful
def check_battery():
    voltage = prime_hub.battery.voltage()
    print("Battery Voltage:", voltage, "mV")
    
    if voltage < 7000:
        prime_hub.light.on(Color.RED)
        print("67 MUSTARD: Change battery now!")
        # Wait for user to acknowledge so they don't miss the warning
        while not any(prime_hub.buttons.pressed()):
            wait(10)
    elif voltage < 7500:
        prime_hub.light.on(Color.ORANGE)
        print("LOCK IN: Battery low. Precision may be tortured.")
    else:
        prime_hub.light.on(Color.GREEN)

# --- THE TURN FUNCTION ---
def turn_to_angle_pro(target_angle, precision=1.5, timeout=2000):
    timer = StopWatch()
    timer.reset()
    
    # Loop runs until the angle is within precision OR time runs out
    while abs(target_angle - prime_hub.imu.heading()) > precision:
        if timer.time() > timeout:
            print("TIMEOUT REACHED")
            break
            
        error = target_angle - prime_hub.imu.heading()
        turn_speed = error * 1.8 # The 'Kp' multiplier
        
        # Minimum speed to ensure the robot actually moves against friction
        if 0 < turn_speed < 15: turn_speed = 15
        if -15 < turn_speed < 0: turn_speed = -15
        
        drive_base.drive(0, turn_speed)
        wait(10)
    
    # Lock the motors at the final angle
    drive_base.stop(Stop.HOLD)

def drive_curve_pid(distance_mm, speed, start_angle, end_angle):
    """Drives in a smooth curve from one angle to another."""
    drive_base.reset()
    total_change = end_angle - start_angle
    
    while abs(drive_base.distance()) < distance_mm:
        progress = abs(drive_base.distance()) / distance_mm
        current_target = start_angle + (total_change * progress)
        
        error = current_target - prime_hub.imu.heading()
        correction = error * KP_DRIVE
        
        drive_base.drive(speed, correction)
        wait(10)
    drive_base.stop()

# --- 3. MAIN PROGRAM ---
# This is where you write your mission!

# Always print stats at the start to check battery health
print('vOltAgE', prime_hub.battery.voltage())
print('mA iS', prime_hub.battery.current())

# Reset gyro before starting
prime_hub.imu.reset_heading(0)

# EXAMPLE MISSION:
# 1. Drive forward 300mm
drive_straight_pid(300, 200, 0)

# 2. Curve right to a 90-degree heading
drive_curve_pid(400, 150, 0, 90)

# 3. Use an attachment (non-blocking) while driving straight
leftattach.run_angle(500, 180, wait=False) 
drive_straight_pid(200, 100, 90)
