#!/usr/bin/env python3
"""
Pybricks Gyro-Controlled Robot Template
A comprehensive template for a robot that can walk and turn using gyro control.

This template provides:
- Basic movement functions (forward, backward, turn left, turn right)
- Gyro-based precise turning
- Distance-based movement
- Error handling and safety features
- Easy-to-understand structure for beginners

Hardware Requirements:
- LEGO Mindstorms Robot Inventor (51515) or EV3 with Pybricks firmware
- Gyro sensor
- Two motors for movement (left and right wheels)
- Optional: Color sensor for line following
"""

from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Direction, Port, Stop
from pybricks.tools import wait
import math

class GyroRobot:
    """
    A robot class that uses gyro sensor for precise movement and turning.
    """
    
    def __init__(self):
        """
        Initialize the robot with motors and sensors.
        Adjust the ports according to your robot setup.
        """
        # Initialize the hub
        self.hub = InventorHub()
        
        # Initialize motors (adjust ports as needed)
        self.left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.B, Direction.CLOCKWISE)
        
        # Initialize gyro sensor (adjust port as needed)
        self.gyro = self.hub.imu  # Built-in gyro on Inventor Hub
        
        # Optional: Color sensor for advanced features
        # self.color_sensor = ColorSensor(Port.C)
        
        # Robot parameters (adjust these for your robot)
        self.wheel_diameter = 56  # mm (adjust for your wheels)
        self.wheel_distance = 120  # mm (distance between wheels)
        self.motor_speed = 300  # degrees per second
        
        # Calibration
        self.calibrate_gyro()
        
        print("🤖 Gyro Robot initialized successfully!")
    
    def calibrate_gyro(self):
        """
        Calibrate the gyro sensor for accurate readings.
        Keep the robot still during calibration.
        """
        print("🔄 Calibrating gyro sensor...")
        print("   Please keep the robot still for 2 seconds...")
        
        # Wait for gyro to stabilize
        wait(2000)
        
        # Reset gyro heading to 0
        self.gyro.reset_heading(0)
        
        print("✅ Gyro calibration complete!")
    
    def get_heading(self):
        """
        Get the current heading from the gyro sensor.
        
        Returns:
            float: Current heading in degrees (0-360)
        """
        return self.gyro.heading()
    
    def move_forward(self, distance_mm, speed=None):
        """
        Move the robot forward by a specific distance using gyro correction.
        
        Args:
            distance_mm (float): Distance to move in millimeters
            speed (int): Motor speed in degrees per second (optional)
        """
        if speed is None:
            speed = self.motor_speed
            
        print(f"🚶 Moving forward {distance_mm}mm at speed {speed}...")
        
        # Calculate how many degrees the wheels need to turn
        wheel_circumference = math.pi * self.wheel_diameter
        degrees_to_turn = (distance_mm / wheel_circumference) * 360
        
        # Get starting heading for correction
        start_heading = self.get_heading()
        
        # Reset motor encoders
        self.left_motor.reset_angle(0)
        self.right_motor.reset_angle(0)
        
        # Move forward with gyro correction
        while abs(self.left_motor.angle()) < abs(degrees_to_turn):
            # Calculate heading error
            current_heading = self.get_heading()
            heading_error = self.normalize_angle(current_heading - start_heading)
            
            # Apply correction (adjust Kp for more/less correction)
            Kp = 2.0  # Proportional gain for correction
            correction = heading_error * Kp
            
            # Apply speeds with correction
            left_speed = speed - correction
            right_speed = speed + correction
            
            # Ensure speeds are within limits
            left_speed = max(-speed, min(speed, left_speed))
            right_speed = max(-speed, min(speed, right_speed))
            
            # Run motors
            self.left_motor.run(left_speed)
            self.right_motor.run(right_speed)
            
            wait(10)  # Small delay for control loop
        
        # Stop motors
        self.left_motor.stop()
        self.right_motor.stop()
        
        print(f"✅ Moved forward {distance_mm}mm")
    
    def move_backward(self, distance_mm, speed=None):
        """
        Move the robot backward by a specific distance.
        
        Args:
            distance_mm (float): Distance to move in millimeters
            speed (int): Motor speed in degrees per second (optional)
        """
        print(f"🚶 Moving backward {distance_mm}mm...")
        self.move_forward(-distance_mm, speed)
    
    def turn_to_heading(self, target_heading, speed=None):
        """
        Turn the robot to a specific heading using gyro control.
        
        Args:
            target_heading (float): Target heading in degrees (0-360)
            speed (int): Motor speed in degrees per second (optional)
        """
        if speed is None:
            speed = self.motor_speed // 2  # Slower for turning
            
        print(f"🔄 Turning to heading {target_heading}°...")
        
        # Calculate the shortest turn direction
        current_heading = self.get_heading()
        heading_error = self.normalize_angle(target_heading - current_heading)
        
        # Determine turn direction
        if heading_error > 0:
            turn_direction = 1  # Turn right
        else:
            turn_direction = -1  # Turn left
        
        # Turn until we reach the target heading
        while abs(heading_error) > 2:  # 2 degree tolerance
            current_heading = self.get_heading()
            heading_error = self.normalize_angle(target_heading - current_heading)
            
            # Calculate turn speed (slower as we approach target)
            turn_speed = min(speed, abs(heading_error) * 3)
            
            # Apply turn speed
            if turn_direction > 0:
                self.left_motor.run(turn_speed)
                self.right_motor.run(-turn_speed)
            else:
                self.left_motor.run(-turn_speed)
                self.right_motor.run(turn_speed)
            
            wait(10)
        
        # Stop motors
        self.left_motor.stop()
        self.right_motor.stop()
        
        print(f"✅ Turned to heading {target_heading}°")
    
    def turn_left(self, degrees):
        """
        Turn the robot left by a specific number of degrees.
        
        Args:
            degrees (float): Degrees to turn left
        """
        current_heading = self.get_heading()
        target_heading = self.normalize_angle(current_heading - degrees)
        self.turn_to_heading(target_heading)
    
    def turn_right(self, degrees):
        """
        Turn the robot right by a specific number of degrees.
        
        Args:
            degrees (float): Degrees to turn right
        """
        current_heading = self.get_heading()
        target_heading = self.normalize_angle(current_heading + degrees)
        self.turn_to_heading(target_heading)
    
    def normalize_angle(self, angle):
        """
        Normalize an angle to be between -180 and 180 degrees.
        
        Args:
            angle (float): Angle in degrees
            
        Returns:
            float: Normalized angle between -180 and 180
        """
        while angle > 180:
            angle -= 360
        while angle < -180:
            angle += 360
        return angle
    
    def stop(self):
        """
        Stop the robot immediately.
        """
        print("🛑 Stopping robot...")
        self.left_motor.stop()
        self.right_motor.stop()
    
    def emergency_stop(self):
        """
        Emergency stop with brake.
        """
        print("🚨 EMERGENCY STOP!")
        self.left_motor.stop(Stop.BRAKE)
        self.right_motor.stop(Stop.BRAKE)
    
    def get_status(self):
        """
        Get current robot status information.
        
        Returns:
            dict: Dictionary with robot status
        """
        return {
            'heading': self.get_heading(),
            'left_motor_angle': self.left_motor.angle(),
            'right_motor_angle': self.right_motor.angle(),
            'battery_voltage': self.hub.battery.voltage()
        }
    
    def print_status(self):
        """
        Print current robot status to console.
        """
        status = self.get_status()
        print(f"📊 Robot Status:")
        print(f"   Heading: {status['heading']:.1f}°")
        print(f"   Left Motor: {status['left_motor_angle']:.1f}°")
        print(f"   Right Motor: {status['right_motor_angle']:.1f}°")
        print(f"   Battery: {status['battery_voltage']:.1f}V")


def demo_movements():
    """
    Demo function showing basic robot movements.
    Run this to test your robot's basic functions.
    """
    print("🎯 Starting Gyro Robot Demo...")
    
    # Initialize robot
    robot = GyroRobot()
    
    try:
        # Demo 1: Basic forward movement
        print("\n📝 Demo 1: Moving forward 200mm")
        robot.move_forward(200)
        wait(1000)
        
        # Demo 2: Turn right 90 degrees
        print("\n📝 Demo 2: Turning right 90°")
        robot.turn_right(90)
        wait(1000)
        
        # Demo 3: Move forward again
        print("\n📝 Demo 3: Moving forward 200mm")
        robot.move_forward(200)
        wait(1000)
        
        # Demo 4: Turn left 90 degrees
        print("\n📝 Demo 4: Turning left 90°")
        robot.turn_left(90)
        wait(1000)
        
        # Demo 5: Move backward
        print("\n📝 Demo 5: Moving backward 200mm")
        robot.move_backward(200)
        wait(1000)
        
        # Demo 6: Turn to specific heading
        print("\n📝 Demo 6: Turning to heading 180°")
        robot.turn_to_heading(180)
        wait(1000)
        
        # Demo 7: Print status
        print("\n📝 Demo 7: Current status")
        robot.print_status()
        
        print("\n✅ Demo completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during demo: {e}")
        robot.emergency_stop()
    
    finally:
        robot.stop()
        print("🏁 Demo finished. Robot stopped.")


def create_square_pattern():
    """
    Create a square pattern using gyro-controlled movements.
    """
    print("🔲 Creating Square Pattern...")
    
    robot = GyroRobot()
    
    try:
        for i in range(4):
            print(f"\n📝 Square side {i+1}/4")
            
            # Move forward
            robot.move_forward(300)
            wait(500)
            
            # Turn right 90 degrees
            robot.turn_right(90)
            wait(500)
        
        print("✅ Square pattern completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        robot.emergency_stop()
    
    finally:
        robot.stop()


def create_circle_pattern():
    """
    Create a circular pattern using continuous turning.
    """
    print("⭕ Creating Circle Pattern...")
    
    robot = GyroRobot()
    
    try:
        # Start turning
        robot.left_motor.run(200)
        robot.right_motor.run(100)
        
        # Turn for a full circle (360 degrees)
        start_heading = robot.get_heading()
        while abs(robot.normalize_angle(robot.get_heading() - start_heading)) < 350:
            wait(10)
        
        robot.stop()
        print("✅ Circle pattern completed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        robot.emergency_stop()
    
    finally:
        robot.stop()


# Main execution
if __name__ == "__main__":
    print("🤖 Pybricks Gyro Robot Template")
    print("=" * 50)
    print("Choose a demo to run:")
    print("1. Basic movements demo")
    print("2. Square pattern")
    print("3. Circle pattern")
    print("4. Custom movements (edit the code)")
    
    # Uncomment the demo you want to run:
    
    # Demo 1: Basic movements
    demo_movements()
    
    # Demo 2: Square pattern
    # create_square_pattern()
    
    # Demo 3: Circle pattern
    # create_circle_pattern()
    
    print("\n🎉 Template execution complete!")
    print("💡 Edit the code to create your own movements!")
