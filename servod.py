#!/usr/bin/python3

FIFO = '/dev/servoblaster'

# reader.py
import os
import string
from pathlib import Path
import RPi.GPIO as GPIO
import time


fifo_path = Path(FIFO)
try:
    if not os.path.exists(fifo_path):
        os.mkfifo(fifo_path)
        os.chmod(fifo_path, 0o666)
except IOError:
    print(f"Failed to create {fifo_path}.")
    exit(1)


def angle_to_percent (angle) :
    """Set function to calculate percent from angle
    """
    if angle > 270 or angle < 0 :
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/270 #Calcul ratio from angle to percent

    angle_as_percent = angle * ratio

    return start + angle_as_percent


def pulse_duration_to_percent(pulse):
    """Set function to calculate percent from pulse
    """
    pulse = pulse / 100.
    full_cycle_duration = 20.
    percent = pulse / full_cycle_duration * 100.
    return percent


GPIO.setmode(GPIO.BOARD) # Use Board numerotation mode
GPIO.setwarnings(False) # Disable warnings

#Use pin 22 for PWM signal
pwm_gpio = 22
frequence = 50
GPIO.setup(pwm_gpio, GPIO.OUT)
pwm = GPIO.PWM(pwm_gpio, frequence)
pwm.start(pulse_duration_to_percent(0.))


while True:
    data = fifo_path.read_text() # blocks until data becomes available
    data = data.strip()

    pulse = int(data.split('=')[-1])
    pwm.ChangeDutyCycle(pulse_duration_to_percent(pulse))
