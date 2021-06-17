# PIR 센서는 움직임을 감지하는 센서이다.
import RPi.GPIO as GPIO
import time

PIR_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)  # 움직임을 입력 받아야 하므로 IN

time.sleep(5)
print('PIR Ready...')

try:
  while True:
    val = GPIO.input(PIR_PIN)  # 센서의 값을 val에 넣어준다.
    # 움직임 감지
    if val == GPIO.HIGH:  # val == 1, val == True과 같음
      print('움직임 감지')
    else:
      print('움직임 없음')

    time.sleep(0.1)
finally:
  GPIO.cleanup()
  print('Clean up and Exit')