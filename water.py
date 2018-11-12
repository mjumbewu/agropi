import RPi.GPIO as GPIO
import time

# Set up the GPIO pin numbering mode. There are basically two ways to refer to
# each GPIO pin: by Raspberry Pi number scheme (GPIO.BOARD) or by Broadcom
# numbering scheme (GPIO.BCM). We're going to use the BOARD because it's easier
# to remember which pin is which.
GPIO.setmode(GPIO.BOARD)

# Define the pin that we have out moisture sensor connected to. Setup that pin
# to receive input.
sensor_pin = 11
GPIO.setup(sensor_pin, GPIO.IN)

# Keep an eye on the pin. Report its status.
while True:
    if GPIO.input(sensor_pin):
        print("Dry")
    else:
        print("Wet")
    time.sleep(1)
