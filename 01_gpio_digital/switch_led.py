import RPi.GPIO as GPIO

LED_PIN = 5
SWITCH_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 내부 pull down 저항

try:
  while True:
    val = GPIO.input(SWITCH_PIN) # 누르지 않은 경우 0, 눌렀을 때는 1
    print(val)
    GPIO.output(LED_PIN, val)    # GPIO.HIGH (1), GPIO.LOW (0)
finally:
  GPIO.cleanup()
  print("Clean up and exit")
