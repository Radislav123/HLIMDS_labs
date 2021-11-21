import platform
import random


if platform.system() == "Windows":
    class Sensor:
        class Measurement:
            def __init__(self, *args, **kwargs):
                pass

            @staticmethod
            def raw_distance():
                return random.randrange(20)

            @staticmethod
            def distance_metric(distance):
                return distance


    sensor = Sensor()
else:
    import hcsr04sensor.sensor as sensor
