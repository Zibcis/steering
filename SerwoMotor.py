from Serwo_Parametrs import *
import RPi.GPIO as GPIO
import time
class SerwoMotor:

    def __init__(self, servo_pin, pwm_frequency):
        self.pwm_frequency = pwm_frequency
        self.pwm_frequency = GPIO.PWM(self.pwm_frequency)
        self.servo_pin = servo_pin

    def configure(self, servo_pin, pwm_frequency):
        self.pwm_frequency = pwm_frequency
        self.pwm_frequency = GPIO.PWM(self.pwm_frequency)
        self.servo_pin = servo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servo_pin, GPIO.OUT)
        pwm = GPIO.PWM(self.servo_pin, self.pwm_frequency)
        pwm.start(start_angle)
        return pwm

    def change_angle(self, pwm, ext_angle) -> None:
        if ext_angle >= left_angle_limit and ext_angle <= right_angle_limit:
            pwm.ChangeDutyCycle(ext_angle)
            time.sleep(time_sleep_change_angle)

    def stop(self):
        GPIO.cleanup()
