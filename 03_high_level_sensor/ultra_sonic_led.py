# 초음파 센서를 이용하여 일정 거리 가까워지면 LED를 켠다.
import RPi.GPIO as GPIO
import time

TRIGGER_PIN = 4
ECHO_PIN = 14
LED_PIN = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
  while True:
    # 10us 동안 HIGH 출력
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)  # 10us (1us ->  0.000001s)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)

    # ECHO PIN -> HIGH로 되는 시간 (start time)
    while GPIO.input(ECHO_PIN) == 0:
      pass
    start = time.time()  # 시작 시간

    while GPIO.input(ECHO_PIN) == 1:
      pass
    stop = time.time()  # 종료 시간

    duration_time = stop - start
    distance = 17160 * duration_time
    
    print('Distance : %.1fcm' % distance)
    
    if distance <= 20:
      GPIO.output(LED_PIN, GPIO.HIGH)
      print('LED ON')
    else:
      GPIO.output(LED_PIN, GPIO.LOW)
      print('LED OFF')
    
    time.sleep(0.1)
finally:
  GPIO.cleanup()
  print('Clean up and exit')