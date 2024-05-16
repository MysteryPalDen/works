import time

def default(Arm):
    Arm.Arm_serial_servo_write6(90, 90, 0, 10, 90, 90, 1000)
    time.sleep(1)

def nod(i, Arm):
    Arm.Arm_serial_servo_write6(90, 90, 90, 0, 90, 90, 1000)
    time.sleep(1)
    for u in range(i):
        Arm.Arm_serial_servo_write6(90, 90, 90, 45, 90, 90, 500)
        time.sleep(0.5)
        Arm.Arm_serial_servo_write6(90, 90, 90, 0, 90, 90, 500)
        time.sleep(0.5)
    default(Arm)
    
def grab(Arm, x, angl):
    Arm.Arm_serial_servo_write6(angl, 10, 30, 70, 90, 0, 1000)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(angl, 10, 30, 70, 90, 170, 1000)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(angl, 90, 90, 0, 90, 170, 1000)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(x, 90, 90, 0, 90, 170, 1000)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(x, 10, 30, 70, 90, 170, 1000)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(x, 10, 30, 70, 90, 0, 1000)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(90, 90, 0, 10, 90, 90, 1000)
    time.sleep(1)
    default(Arm)