import RPi.GPIO as GPIO

RED_PIN = 4
RED_SWITCH_PIN = 14

YELLOW_PIN = 5
YELLOW_SWITCH_PIN = 15

GREEN_PIN = 6
GREEN_SWITCH_PIN = 16

GPIO.setmode(GPIO.BCM)

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)

GPIO.setup(RED_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(YELLOW_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(GREEN_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

try:
  while True:
    redVal = GPIO.input(RED_SWITCH_PIN) # 누르지 않은 경우 0, 눌렀을 때는 1
    yellowVal = GPIO.input(YELLOW_SWITCH_PIN) 
    greenVal = GPIO.input(GREEN_SWITCH_PIN) 
    GPIO.output(RED_PIN, redVal)    # GPIO.HIGH (1), GPIO.LOW (0)
    GPIO.output(YELLOW_PIN, yellowVal)    
    GPIO.output(GREEN_PIN, greenVal)    
    
finally:
  GPIO.cleanup()
  print("Clean up and exit")
