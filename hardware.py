from time import sleep
import RPi.GPIO as GPIO

def Rotate(pin, angle):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    servo = GPIO.PWM(pin, 50)
    servo.start(0)

    GPIO.output(servo, True)
    servo.ChangeDutyCycle(angle / 18 + 2)
    time.sleep(3)
    GPIO.output(servo, False)

    servo.ChangeDutyCycle(0)
    servo.stop()
    GPIO.cleanup()