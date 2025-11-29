from pybricks.tools import wait

def move_straight(hub, drive_base, distance, speed):
    hub.imu.reset_heading(0)
    target_heading = 0

    Kp = 2
    if distance >= 0:
        speed = speed
    else:
        speed = -1 * speed

    loop_time = 10
    drive_base.reset()

    while abs(drive_base.distance()) < abs(distance):
        current_heading = hub.imu.heading()
        error = current_heading - target_heading
        correction = -Kp * error
        drive_base.drive(speed,correction)
        wait(loop_time)

    # read the heading after go straight
    heading = hub.imu.heading()
    # print('after straight, the heading is:', heading)

def turn_exact(hub, drive_base, left, right, target_degree):
    # read the heading after go straight
    hub.imu.reset_heading(0)
    # print('after straight, the heading is:', heading)

    # turn 90 defree
    target_turn = target_degree

    heading = hub.imu.heading()
    # print('before turn, the heading is:', heading)
    drive_base.turn(target_turn)
    heading = hub.imu.heading()
    # print('after turn, the heading is:', heading)

    while abs(heading - target_turn) > 0.05:
        if heading - target_turn > 0.05:
            left.run(20)
            right.run(-20)
            heading = hub.imu.heading()
        if target_turn - heading > 0.05:
            left.run(-20)
            right.run(20)
            heading = hub.imu.heading()
    heading = hub.imu.heading()
    # print('after correction, the heading is:', heading)

    # stop turning
    left.stop()
    right.stop()
