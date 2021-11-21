from import_gpio import GPIO
import time


class Led:

    def __init__(self, pin = 2):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.on = False
        self.light_off()

    def light_on(self):
        if not self.on:
            GPIO.output(self.pin, True)
            self.on = True

    def light_off(self):
        if self.on:
            GPIO.output(self.pin, False)
            self.on = False

    # frequency in hertz
    # time_period - time to blink
    def light_blink(self, frequency, time_period):
        for i in range(time_period*frequency):
            self.light_on()
            time.sleep(1/frequency/2)
            self.light_off()
            time.sleep(1/frequency/2)


if __name__ == "__main__":
    led = Led()
    led.light_blink(1, 5)
    GPIO.cleanup()
    print("test is finished")
