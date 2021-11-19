import platform


if platform.system() == "Windows":
    class Sensor:
        pass


    sensor = Sensor()
else:
    import hcsr04sensor.sensor as sensor
