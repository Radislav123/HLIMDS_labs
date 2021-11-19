from import_gpio import GPIO
import time


class Servo:

    # pin - 5 == BCM3
    def __init__(self, pin = 5):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        # todo: check attribute ("50")
        self.pwm = GPIO.PWM(self.pin, 50)
        # todo: check attribute ('0')
        self.pwm.start(0)

    def change_angle(self, angle):
        duty = angle/18 + 2
        GPIO.output(self.pin, True)
        self.pwm.ChangeDutyCycle(duty)
        # todo: check "sleep"
        time.sleep(1)
        GPIO.output(self.pin, False)
        # todo: check this
        self.pwm.ChangeDutyCycle(0)


# todo: test it
if __name__ == "__main__":
    test_angles = [0, 45, 90, 180, 360]
    servo = Servo()

    for test_angle in test_angles:
        print(f"angle - {test_angle}")
        servo.change_angle(test_angle)
        # todo: check "sleep"
        time.sleep(1)
    GPIO.cleanup()
