import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(22,50)

servo = GPIO.PWM(22,50)

servo.start(0)
print("Waiting for 1 second")
time.sleep(1)

print("Rotating at inervals of 12 degrees")
duty = 2
while duty <= 17:
    servo.ChangeDutyCycle(duty)
    time.sleep(1)
    duty = duty + 1

print("Turning back to 0 degrees")
servo.ChangeDutyCycle(2)
time.sleep(1)
servo.ChangeDutyCycle(0)

servo.stop()
GPIO.cleanup()
print("Everything's cleaned up")