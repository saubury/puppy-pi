# Project Imports
import puppypi_config
import puppypi_util
import puppypi_aws
import puppypi_servo
import puppypi_video
import RPi.GPIO as GPIO
import time


def my_callback_yellow():  
    print "****************************"
    print "Event - yellow"
    print "****************************"
    puppypi_servo.servo_on()
    puppypi_video.process_livevideo()
    puppypi_servo.servo_off()
    time.sleep(2)

def my_callback_green():  
    print "****************************"
    print "Event - green"
    print "****************************"
    file_string='./tmp/demo-file'
    puppypi_aws.mainAWS(file_string)
    time.sleep(2)

def do_button():
    puppypi_util.printmsg("Button Press Mode")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(puppypi_config.gpio_button_green, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(puppypi_config.gpio_button_yellow, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    #GPIO.add_event_detect(puppypi_config.gpio_button_yellow, GPIO.RISING, callback=my_callback_yellow)  
    #GPIO.add_event_detect(puppypi_config.gpio_button_green, GPIO.RISING, callback=my_callback_green)  


    while True:
        time.sleep(0.2)

        if GPIO.input(puppypi_config.gpio_button_green) == False:
            print('Button Pressed Green')
            my_callback_green()
            time.sleep(0.2)

        if GPIO.input(puppypi_config.gpio_button_yellow) == False:
            print('Button Pressed Yellow')
            my_callback_yellow()
            time.sleep(0.2)

def do_button_debug():
    puppypi_util.printmsg("Debug Button Press Mode")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(puppypi_config.gpio_button_pcb, GPIO.IN)

    while True:
        input_state = GPIO.input(puppypi_config.gpio_button_pcb)
        if input_state == False:
            print('Button Pressed')
            time.sleep(0.2)


