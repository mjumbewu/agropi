import RPi.GPIO as GPIO
import relay
import sensor
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

# Define the pin that we have our water pump relay connected to. Setup that pin
# to send output.
relay_pin = 12
GPIO.setup(relay_pin, GPIO.OUT)

#  Create a function to hold the behavior of pulsing the water pump.
def pulse(pin, duration):
    relay.switch_on(pin)
    time.sleep(duration)
    relay.switch_off(pin)

# Alternate turning the pump on an off.
while True:
    if sensor.is_dry(sensor_pin):
        pulse(pin=relay_pin, duration=5)
        time.sleep(10)
    time.sleep(1)
