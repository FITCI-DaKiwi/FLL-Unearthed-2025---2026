#!/usr/bin/env python3
"""
Simple Pybricks Gyro Robot for Beginners
A simplified version for learning the basics of gyro-controlled movement.

Hardware Setup:
- LEGO Mindstorms Robot Inventor (51515)
- Left motor on Port A
- Right motor on Port B
- Built-in gyro sensor (no additional sensor needed)
"""

from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.tools import wait

# Initialize the robot
hub = InventorHub()
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

# Robot settings
SPEED = 300  # Motor speed
TURN_SPEED = 200  # Slower speed for turning

def reset_gyro():
    """Reset the gyro sensor to 0 degrees."""
    print("🔄 Resetting gyro...")
    hub.imu.reset_heading(0)
    wait(1000)
    print("✅ Gyro reset complete!")

def get_heading():
    """Get current heading from gyro."""
    return hub.imu.heading()

def move_forward(distance_cm):
    """Move forward a specific distance in centimeters."""
    print(f"🚶 Moving forward {distance_cm}cm...")
    
    # Simple forward movement
    left_motor.run(SPEED)
    right_motor.run(SPEED)
    
    # Wait for the distance (rough calculation)
    wait_time = distance_cm * 50  # Adjust this number for your robot
    wait(wait_time)
    
    # Stop
    left_motor.stop()
    right_motor.stop()
    print("✅ Forward movement complete!")

def move_backward(distance_cm):
    """Move backward a specific distance in centimeters."""
    print(f"🚶 Moving backward {distance_cm}cm...")
    
    left_motor.run(-SPEED)
    right_motor.run(-SPEED)
    
    wait_time = distance_cm * 50
    wait(wait_time)
    
    left_motor.stop()
    right_motor.stop()
    print("✅ Backward movement complete!")

def turn_left(degrees):
    """Turn left by a specific number of degrees."""
    print(f"🔄 Turning left {degrees}°...")
    
    # Get starting heading
    start_heading = get_heading()
    target_heading = start_heading - degrees
    
    # Turn left
    left_motor.run(-TURN_SPEED)
    right_motor.run(TURN_SPEED)
    
    # Keep turning until we reach the target
    while abs(get_heading() - target_heading) > 5:
        wait(10)
    
    # Stop
    left_motor.stop()
    right_motor.stop()
    print(f"✅ Turned left {degrees}°")

def turn_right(degrees):
    """Turn right by a specific number of degrees."""
    print(f"🔄 Turning right {degrees}°...")
    
    start_heading = get_heading()
    target_heading = start_heading + degrees
    
    # Turn right
    left_motor.run(TURN_SPEED)
    right_motor.run(-TURN_SPEED)
    
    # Keep turning until we reach the target
    while abs(get_heading() - target_heading) > 5:
        wait(10)
    
    # Stop
    left_motor.stop()
    right_motor.stop()
    print(f"✅ Turned right {degrees}°")

def stop_robot():
    """Stop the robot immediately."""
    print("🛑 Stopping robot...")
    left_motor.stop()
    right_motor.stop()

def show_heading():
    """Show current heading."""
    heading = get_heading()
    print(f"📊 Current heading: {heading:.1f}°")

# Main program
print("🤖 Simple Gyro Robot Starting...")
print("=" * 40)

# Reset gyro at the start
reset_gyro()

try:
    # Example movements - edit these for your robot!
    
    print("\n📝 Example 1: Move forward 20cm")
    move_forward(20)
    wait(1000)
    
    print("\n📝 Example 2: Turn right 90 degrees")
    turn_right(90)
    wait(1000)
    
    print("\n📝 Example 3: Move forward 20cm")
    move_forward(20)
    wait(1000)
    
    print("\n📝 Example 4: Turn left 90 degrees")
    turn_left(90)
    wait(1000)
    
    print("\n📝 Example 5: Move backward 20cm")
    move_backward(20)
    wait(1000)
    
    print("\n📝 Example 6: Show final heading")
    show_heading()
    
    print("\n✅ All movements completed!")

except Exception as e:
    print(f"❌ Error: {e}")
    stop_robot()

finally:
    stop_robot()
    print("🏁 Program finished!")
