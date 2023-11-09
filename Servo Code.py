import pi_servo_hat
import time

test = pi_servo_hat.PiServoHat()
test.restart()
test.move_servo_position(0,90)
print(doingthings)
time.sleep(1)