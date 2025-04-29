import RPi.GPIO as GPIO
import time

BUTTON = 17
LED = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        state = GPIO.input(BUTTON)
        if state:
            print("off")
            GPIO.output(LED, GPIO.LOW)  # Tắt đèn khi nút không được nhấn
        else:
            print("on")
            GPIO.output(LED, GPIO.HIGH)  # Bật đèn khi nhấn nút
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()  # Dọn dẹp các thiết lập GPIO khi kết thúc chương trình