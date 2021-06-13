import RPi.GPIO as GPIO
import time
import Adafruit_DHT

BUZZER_PIN = 12
PIR_PIN = 4
LED_PIN = 1
SWITCH_PIN = 2
DHT_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
dhtSensor = Adafruit_DHT.DHT11

time.sleep(5)   # PIR 센서가 동작하기 위해 일정시간 대기해야 함.
print('System Ready...')

# PWM 인스턴스 생성
# 주파수 설정 (C4: 262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(50)   # duty cycle (0~100)

moveCount = 0
moveDetect = 0


try:
  while True:
    pirVal = GPIO.input(PIR_PIN)  # PIR 센서의 값을 pirVal에 넣어준다.
    switchVal = GPIO.input(SWITCH_PIN) # 버튼 값을 switchVal에 넣어준다.

    # 움직임 감지
    if pirVal == GPIO.HIGH:
      print('움직임 감지')
      moveCount = 0   # 움직임이 감지되면 moveCount를 0으로 초기화.
    # 움직임 없음
    else:
      print('움직임 없음')
      moveCount += 0.1  # 움직임이 없으면 moveCount를 0.1씩 증가.
      time.sleep(0.1)
      

    if switchVal == 1:  # 버튼을 누르면 경보음을 끄고 LED를 끈다.
      moveDetect = 0

    if moveCount > 15:  # 움직임이 15초간 없으면 moveDetect를 '1' 로 한다
      moveDetect = 1


    if moveDetect == 1:  # 경보음이 울리고 LED가 켜진다.
      GPIO.output(LED_PIN, 1)
      pwm.ChangeDutyCycle(392)
      time.sleep(1)
      GPIO.output(LED_PIN, 1)
      pwm.ChangeDutyCycle(1)
      time.sleep(1)
    elif moveDetect == 0: # 경보음과 LED가 꺼진다.
      pwm.ChangeDutyCycle(1)


    h, t = Adafruit_DHT.read_retry(dhtSensor, DHT_PIN)
    if h is not None and t is not None:
      print('Temperature=%.1f*, Humidity=%.1f%' % (t, h))
    else:
      print('Read Error')

finally:
  GPIO.cleanup()
  print('System Down')