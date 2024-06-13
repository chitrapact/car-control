import RPi.GPIO as GPIO
import time

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define the GPIO pins for the motor driver
MOTOR1_IN1 = 17
MOTOR1_IN2 = 27
MOTOR2_IN3 = 22
MOTOR2_IN4 = 23

# Setup the GPIO pins as output
GPIO.setup(MOTOR1_IN1, GPIO.OUT)
GPIO.setup(MOTOR1_IN2, GPIO.OUT)
GPIO.setup(MOTOR2_IN3, GPIO.OUT)
GPIO.setup(MOTOR2_IN4, GPIO.OUT)


def stop_motors():
    """Stop both motors."""
    GPIO.output(MOTOR1_IN1, GPIO.LOW)
    GPIO.output(MOTOR1_IN2, GPIO.LOW)
    GPIO.output(MOTOR2_IN3, GPIO.LOW)
    GPIO.output(MOTOR2_IN4, GPIO.LOW)


def move_forward():
    """Move the car forward."""
    GPIO.output(MOTOR1_IN1, GPIO.HIGH)
    GPIO.output(MOTOR1_IN2, GPIO.LOW)
    GPIO.output(MOTOR2_IN3, GPIO.HIGH)
    GPIO.output(MOTOR2_IN4, GPIO.LOW)


def move_backward():
    """Move the car backward."""
    GPIO.output(MOTOR1_IN1, GPIO.LOW)
    GPIO.output(MOTOR1_IN2, GPIO.HIGH)
    GPIO.output(MOTOR2_IN3, GPIO.LOW)
    GPIO.output(MOTOR2_IN4, GPIO.HIGH)


def turn_left():
    """Turn the car left."""
    GPIO.output(MOTOR1_IN1, GPIO.LOW)
    GPIO.output(MOTOR1_IN2, GPIO.HIGH)
    GPIO.output(MOTOR2_IN3, GPIO.HIGH)
    GPIO.output(MOTOR2_IN4, GPIO.LOW)


def turn_right():
    """Turn the car right."""
    GPIO.output(MOTOR1_IN1, GPIO.HIGH)
    GPIO.output(MOTOR1_IN2, GPIO.LOW)
    GPIO.output(MOTOR2_IN3, GPIO.LOW)
    GPIO.output(MOTOR2_IN4, GPIO.HIGH)


# Example sequence to move the car
try:
    while True:
        print("Moving forward")
        move_forward()
        time.sleep(2)

        print("Stopping")
        stop_motors()
        time.sleep(1)

        print("Turning left")
        turn_left()
        time.sleep(2)

        print("Stopping")
        stop_motors()
        time.sleep(1)

        print("Moving backward")
        move_backward()
        time.sleep(2)

        print("Stopping")
        stop_motors()
        time.sleep(1)

        print("Turning right")
        turn_right()
        time.sleep(2)

        print("Stopping")
        stop_motors()
        time.sleep(1)

except KeyboardInterrupt:
    # Cleanup GPIO settings before exiting
    GPIO.cleanup()
