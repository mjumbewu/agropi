import RPi.GPIO as GPIO


def switch_on(pin):
    print("Switching relay on...")
    GPIO.output(pin, GPIO.HIGH)


def switch_off(pin):
    print("Switching relay off...")
    GPIO.output(pin, GPIO.LOW)
