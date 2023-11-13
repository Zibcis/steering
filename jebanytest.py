import smbus
import time
import biny

bus = smbus.SMBus(0)
address = 0x36
while True:
    print(raw_angle(bus.read_i2c_block_data(address,0x0E,2)))
    time.sleep(0.5)
