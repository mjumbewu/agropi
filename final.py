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

# Keep an eye on the pin. We can detect when the signal from the pin goes low
# (GPIO.FALLING), high (GPIO.RISING), or either one (GPIO.BOTH). Only detect the
# change if it's consistent for more than 300ms.
GPIO.add_event_detect(sensor_pin, GPIO.BOTH, bouncetime=300)

# When there is a change in the sensor state, perform some action.
def handle_sensor_change(pin):
    while sensor.is_dry(pin):
        pulse(pin=relay_pin, duration=5)
        time.sleep(10)

GPIO.add_event_callback(sensor_pin, handle_sensor_change)
