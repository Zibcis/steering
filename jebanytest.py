import smbus
import time

bus = smbus.SMBus(0)
address = 0x36

print(bus.read_byte_data(address,1))
