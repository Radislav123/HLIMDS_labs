from import_gpio import GPIO

# BCM4
SERVO_PIN = 7


GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo_pwm = GPIO
