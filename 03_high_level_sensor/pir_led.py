# PIR 센서를 이용하여 움직임이 감지되면 LED를 켠다.
import RPi.GPIO as GPIO
import time

PIR_PIN = 4
LED_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)  # PIR센서 - 움직임을 입력 받아야 하므로 IN
GPIO.setup(LED_PIN, GPIO.OUT) # LED

time.sleep(5)   # PIR 센서가 동작하기 위해 일정시간 대기해야 함.
print('PIR Ready...')

try:
  while True:
    val = GPIO.input(PIR_PIN)  # 센서의 값을 val에 넣어준다.
    # 움직임 감지
    if val == GPIO.HIGH:  # val == 1, val == True과 같음
      print('움직임 감지')
      GPIO.output(LED_PIN, GPIO.HIGH)  # LED ON
    # 움직임 없음
    else:
      print('움직임 없음')
      GPIO.output(LED_PIN, GPIO.LOW)   # LED OFF

      time.sleep(0.1)
finally:
  GPIO.cleanup()
  print('Clean up and Exit')