from import_gpio import GPIO
import time


class Led:

    # pin - 3 == BCM2
    def __init__(self, pin = 3):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def light_on(self):
        GPIO.output(self.pin, True)

    def light_off(self):
        GPIO.output(self.pin, False)

    # frequency in hertz
    # time_period - time to blink
    def light_blink(self, frequency, time_period):
        for i in range(time_period*frequency):
            self.light_on()
            time.sleep(1/frequency/2)
            self.light_off()
            time.sleep(1/frequency/2)


# todo: test it
if __name__ == "__main__":
    led = Led

    led.light_blink(1, 5)
