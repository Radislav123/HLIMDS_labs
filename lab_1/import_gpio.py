import platform


if platform.system() == "Windows":
    from RPiSim.GPIO import GPIO
else:
    import RPi.GPIO as GPIO
