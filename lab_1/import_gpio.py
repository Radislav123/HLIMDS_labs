import platform


if platform.system() == "Windows":
    from RPiSim.GPIO import GPIO


    class PWM:
        def __init__(self, *args, **kwargs):
            pass

        def start(self, *args, **kwargs):
            pass

        class ChangeDutyCycle:
            def __init__(self, *args, **kwargs):
                pass


    GPIO.PWM = PWM
else:
    import RPi.GPIO as GPIO
