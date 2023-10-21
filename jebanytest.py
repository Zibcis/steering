import smbus
import time

servo_pin = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)
pwm = GPIO.PWM(servo_pin,50) # 50 Hz (20 ms PWM period)
bus = smbus.SMBus(0)
address = 0x36

print(bus.read_i2c_block_data(address,0x0E,10))
pwm.start(3.5)
time.sleep(0.5)
print(bus.read_i2c_block_data(address,0x0E,10))
