import RPi.GPIO as GPIO


def is_dry(pin):
    sensor_state = GPIO.input(pin)
    if sensor_state == 1:
        print("Sensor is dry...")
        return True
    else:
        print("Sensor is not dry...")
        return False
