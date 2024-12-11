import RPi.GPIO as GPIO
import time

# Motor driver pins
PWMA = 18  # Left motor speed (PWM)
AIN1 = 23  # Left motor direction 1
AIN2 = 24  # Left motor direction 2

PWMB = 19  # Right motor speed (PWM)
BIN1 = 27  # Right motor direction 1
BIN2 = 22  # Right motor direction 2

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup([PWMA, AIN1, AIN2, PWMB, BIN1, BIN2], GPIO.OUT)

# PWM setup
left_pwm = GPIO.PWM(PWMA, 100)  # 100Hz frequency
right_pwm = GPIO.PWM(PWMB, 100)
left_pwm.start(0)
right_pwm.start(0)

def move_robot(command):
    if command == "FORWARD":
        GPIO.output(AIN1, GPIO.HIGH)
        GPIO.output(AIN2, GPIO.LOW)
        GPIO.output(BIN1, GPIO.HIGH)
        GPIO.output(BIN2, GPIO.LOW)
        left_pwm.ChangeDutyCycle(50)
        right_pwm.ChangeDutyCycle(50)
    elif command == "BACKWARD":
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        left_pwm.ChangeDutyCycle(50)
        right_pwm.ChangeDutyCycle(50)
    elif command == "STOP":
        left_pwm.ChangeDutyCycle(0)
        right_pwm.ChangeDutyCycle(0)
    elif command == "LEFT":
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
        GPIO.output(BIN1, GPIO.HIGH)
        GPIO.output(BIN2, GPIO.LOW)
        left_pwm.ChangeDutyCycle(30)
        right_pwm.ChangeDutyCycle(30)
    elif command == "RIGHT":
        GPIO.output(AIN1, GPIO.HIGH)
        GPIO.output(AIN2, GPIO.LOW)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.HIGH)
        left_pwm.ChangeDutyCycle(30)
        right_pwm.ChangeDutyCycle(30)

def cleanup():
    left_pwm.stop()
    right_pwm.stop()
    GPIO.cleanup()

