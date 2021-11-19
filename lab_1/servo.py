from import_gpio import GPIO
import time


class Servo:

    def __init__(self, pin = 3):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50)
        self.pwm.start(0)

    def change_angle(self, angle):
        duty = angle/18 + 2
        GPIO.output(self.pin, True)
        self.pwm.ChangeDutyCycle(duty)
        GPIO.output(self.pin, False)
        self.pwm.ChangeDutyCycle(0)


if __name__ == "__main__":
    test_angles = [0, 45, 90, 180, 360]
    servo = Servo()

    for test_angle in test_angles:
        print(f"angle - {test_angle}")
        servo.change_angle(test_angle)
        time.sleep(1)
    GPIO.cleanup()
    print("test is finished")
