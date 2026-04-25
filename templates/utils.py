from pybricks.tools import wait, StopWatch
def turn_exact(hub, drive_base, left, right, target_degree):
       left.stop()
       right.stop()
       # wait(100)
      
       # read the heading after go straight
       hub.imu.reset_heading(0)
       # print('after straight, the heading is:', heading)


       initial_heading = hub.imu.heading()
       target_heading = initial_heading + target_degree
       # turn 90 degree
       # target_turn = target_degree


      
       print('before turn, the heading is:', initial_heading)
       drive_base.turn(target_degree)
       current_heading = hub.imu.heading()
       print('after turn, the heading is:', current_heading)


       while abs(current_heading - target_heading) > 0.05:
           if current_heading - target_heading > 0.05:
               left.run(20)
               right.run(-20)
               current_heading = hub.imu.heading()
           if target_heading - current_heading > 0.05:
               left.run(-20)
               right.run(20)
               current_heading = hub.imu.heading()
       current_heading = hub.imu.heading()
       print('after correction, the heading is:', current_heading)


       # stop turning
       left.stop()
       right.stop()
       # wait(100)


def turn_pid(hub, drive_base, left, right, target_degree,tolerance=0.2):
    hub.imu.reset_heading(0)
    drive_base.settings(turn_rate=1000)
    drive_base.turn(target_degree)
    last_error=0
    while True:
            error = target_degree - hub.imu.heading()
            derivative = error - last_error
            last_error = error
            if abs(error) <= tolerance:
                drive_base.stop()
                break
            left.run(25*error+100*derivative)            right.run(-25*error-100*derivative)      
            wait(20)

def safe_straight(drive_base,distance, max_time_ms=None):
    
    # Start a backup timer
    timer = StopWatch()
    
    # Start driving, but do not pause the code
    drive_base.straight(distance, wait=False)
    
    # Keep checking as long as the robot is still driving
    while not drive_base.done():
        
        # 1. Did it get physically blocked?
        if drive_base.stalled():
            print("Robot stalled! Skipping to next move.")
            drive_base.stop()
            break
            
        # 2. Did it take too long? (Optional timeout check)
        if max_time_ms is not None and timer.time() > max_time_ms:
            print("Time limit reached! Skipping to next move.")
            drive_base.stop()
            break
            
        # A tiny wait helps Pybricks process motor limits smoothly
        wait(10)

def safe_motor_turn(motor, speed, angle, max_time_ms=None):
    timer = StopWatch()
    # Start turning the motor
    motor.run_angle(speed, angle, wait=False)   
    # Wait while it's turning and isn't physically stuck
    while not motor.done() and not motor.stalled():
        # Check if it has taken longer than our maximum time
        if max_time_ms is not None and timer.time() > max_time_ms:
            break # Shatter the loop!
            
    # Stop the motor safely
    motor.stop()

