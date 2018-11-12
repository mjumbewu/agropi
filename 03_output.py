import RPi.GPIO as GPIO
import time

# Set up the GPIO pin numbering mode. There are basically two ways to refer to
# each GPIO pin: by Raspberry Pi number scheme (GPIO.BOARD) or by Broadcom
# numbering scheme (GPIO.BCM). We're going to use the BOARD because it's easier
# to remember which pin is which.
GPIO.setmode(GPIO.BOARD)

# Define the pin that we have our water pump relay connected to. Setup that pin
# to send output.
relay_pin = 12
GPIO.setup(relay_pin, GPIO.OUT)

# Alternate turning the pump on an off.
while True:
    print("Turning water on for 1 second...")
    GPIO.output(relay_pin, GPIO.HIGH)
    time.sleep(1)

    print("Turning water off for 2 seconds...")
    GPIO.output(relay_pin, GPIO.LOW)
    time.sleep(2)
