from SerwoMotor import SerwoMotor
from SerwoEncoder import SerwoEncoder
from Serwo_Parametrs import *
import time

S1 = SerwoMotor.SerwoMotor
E1 = SerwoEncoder.SerwoEncoder
pwm = S1.configure(S1, servo_pin, pwm_frequency)


while True:
    input_angle = float(input())
    S1.change_direction(S1, pwm, input_angle)
    time.sleep(time_sleep_read_angle)
    read_angle = E1.getAngle()
    print("angle = ", read_angle)

