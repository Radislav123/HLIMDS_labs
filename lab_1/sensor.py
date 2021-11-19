from import_sensor import sensor
from import_gpio import GPIO
import time


class Sensor:

    def __init__(self, trig_pin = 4, echo_pin = 17):
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        GPIO.setmode(GPIO.BCM)

    def get_distance(self):
        value = sensor.Measurement(self.trig_pin, self.echo_pin)
        raw_distance = value.raw_distance()
        distance_cm = value.distance_metric(raw_distance)
        return distance_cm


if __name__ == "__main__":
    my_sensor = Sensor()
    for i in range(5):
        print(f"distance is {my_sensor.get_distance()} cm")
        time.sleep(1)
    GPIO.cleanup()
    print("test is finished")
