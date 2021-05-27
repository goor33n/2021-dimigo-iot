import RPi.GPIO as GPIO
import time

SWITCH_PIN = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUT_UP)
# GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUT_DOWN)

try:
  while True:
    val = GPIO.input(SWITCH_PIN)
    print(val)
    time.sleep(0.1)
finally:
  GPIO.cleanup()
  print("Clean up and exit")