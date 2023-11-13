import smbus
import RPi.GPIO as GPIO
from Serwo_Parametrs import *
from biny import *
class SerwoEncoder:

    def __init__(self, servo_pin) -> None:
        self.servo_pin = servo_pin
        GPIO.setmode(GPIO.BCM)
        self.bus = smbus.SMBus(1)
        self.first_angle = raw_angle(self.bus.read_i2c_block_data(device_address, read_register_angle, num_bytes_to_read))
    def getAngle(self):
        angle = raw_angle(self.bus.read_i2c_block_data(device_address, read_register_angle, num_bytes_to_read))
        calculated_angle = angle - self.first_angle
        return calculated_angle
