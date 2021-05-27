import RPi.GPIO as GPIO
import time

SWITCH_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_PIN, GPIO.IN,pull_up_down=GPIO.PUD_UP) # 내부 pull up 저항 사용하기 , pull_up_down=GPIO.PUD_DOWN

try:
  while True:
    val = GPIO.input(SWITCH_PIN)
    print(val)
    time.sleep(0.1)

finally:
  GPIO.cleanup()
  print("Clean up and exit")
