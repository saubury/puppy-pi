# Project Imports
import puppypi_config
import puppypi_util
import puppypi_aws
import RPi.GPIO as GPIO
import time


def do_button():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(puppypi_config.gpio_button, GPIO.IN)

    puppypi_util.printmsg("Button Press Mode")
    file_string='./tmp/demo-file'

    while True:
        input_state = GPIO.input(2)
        if input_state == False:
            print('Button Pressed')
            puppypi_aws.mainAWS(file_string)
            time.sleep(0.2)


