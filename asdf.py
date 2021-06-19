import RPi.GPIO as GPIO
import time
import Adafruit_DHT
from datetime import datetime

BUZZER_PIN = 12
PIR_PIN = 9
LED_PIN = 14
SWITCH_PIN = 10
DHT_PIN = 11
#               A  B  C  D  E  F  G
SEGMENT_PINS = [2, 3, 4, 5, 6, 7, 8]
DIGIT_PINS = [10, 11, 12 , 13]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
dhtSensor = Adafruit_DHT.DHT11

# PWM 인스턴스 생성
# 주파수 설정 (C4: 262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10)   # duty cycle (0~100)

moveCount = 0
moveDetect = 0

hour1 = 0
hour2 = 0
minute1 = 0
minute2 = 0

for segment in SEGMENT_PINS:
  GPIO.setup(segment, GPIO.OUT)
  GPIO.output(segment, GPIO.LOW)

for digit in DIGIT_PINS:
  GPIO.setup(digit, GPIO.OUT)
  GPIO.output(digit, GPIO.HIGH)

data = [[1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9

def display(digit, number):  # 자릿수, 숫자
  # 해당하는 자릿수의 핀만 LOW로 설정
  for i in range(len(DIGIT_PINS)):
    if i + 1 == digit:
      GPIO.output(DIGIT_PINS[i], GPIO.LOW)
    else:
      GPIO.output(DIGIT_PINS[i], GPIO.HIGH)

  # 숫자 출력
  for i in range(len(SEGMENT_PINS)):  # 0~6
    GPIO.output(SEGMENT_PINS[i], data[number][i])
  time.sleep(0.001)






time.sleep(5)   # PIR 센서가 동작하기 위해 일정시간 대기해야 함.
print('System Ready...')


# def timedisplay():
#   while moveDetect == 1:
#     pirVal = GPIO.input(PIR_PIN)
#     display(1, hour1)
#     display(2, hour2)
#     display(3, minute1)
#     display(4, minute2)

try:
  while True:
    now = datetime.now() # 현재 시간을 now에 대입
    
    if now.hour >= 10:
      hour1 = now.hour//10
      hour2 = now.hour%10
    else:
      hour1 = 0
      hour2 = now.hour
    
    if now.minute >= 10:
      minute1 = now.minute//10
      minute2 = now.minute%10
    else:
      minute1 = 0
      minute2 = now.minute


    
    pirVal = GPIO.input(PIR_PIN)  # PIR 센서의 값을 pirVal에 넣어준다.
    switchVal = GPIO.input(SWITCH_PIN) # 버튼 값을 switchVal에 넣어준다.

    # 움직임 감지
    if pirVal == GPIO.HIGH:
      print('움직임 감지')
      moveCount = 0   # 움직임이 감지되면 moveCount를 0으로 초기화.
    # 움직임 없음
    else:
      print('움직임 없음')
      moveCount += 0.1  # 움직임이 없으면 moveCount를 1씩 증가.
      print(moveCount)
    time.sleep(0.1)
      

    if switchVal == 1:  # 버튼을 누르면 경보음을 끄고 LED를 끈다.
      moveDetect = 0

    if moveCount > 5:  # 움직임이 5초간 없으면 moveDetect를 '1' 로 한다
      moveDetect = 1


    if moveDetect == 1:  # 경보음이 울리고 LED가 켜진다.
      GPIO.output(LED_PIN, GPIO.HIGH) # LED ON
      pwm.ChangeDutyCycle(50)         # Sound ON
      while moveDetect == 1:
        pirVal = GPIO.input(PIR_PIN)
        if pirVal == GPIO.HIGH:
          break
        display(1, hour1)
        display(2, hour2)
        display(3, minute1)
        display(4, minute2)
      # timedisplay()
      time.sleep(1)

    elif moveDetect == 0: # 경보음과 LED가 꺼진다.
      pwm.ChangeDutyCycle(1)
      GPIO.output(LED_PIN, GPIO.LOW)

    h = 0
    t = 0

    # h, t = Adafruit_DHT.read_retry(dhtSensor, DHT_PIN)
    # if h is not None and t is not None:
    #   print('Temperature=%.1f*, Humidity=%.1f%' % (t, h))
    # else:
    #   print('Read Error')
    # if t > 28:
    #   GPIO.output(LED_PIN, GPIO.HIGH)


    

finally:
  GPIO.cleanup()
  print('System Down')