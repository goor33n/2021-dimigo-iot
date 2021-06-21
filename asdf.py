import RPi.GPIO as GPIO
import time
from datetime import datetime

BUZZER_PIN = 20
PIR_PIN = 9
LED_PIN = 21
SWITCH_PIN = 16
#               A  B  C  D  E  F  G
SEGMENT_PINS = [2, 3, 4, 5, 6, 7, 8]
DIGIT_PINS = [10, 11, 12 , 13]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

# 부저 주파수 설정
pwm = GPIO.PWM(BUZZER_PIN, 430)

moveCount = 0   # 움직임이 감지되지 않을 때 카운트하는 변수
moveDetect = 0  # 움직임 감지가 되면 0, 안되면 1

# 디스플레이에 표시할 각 시간값 변수
hour1 = 0
hour2 = 0
minute1 = 0
minute2 = 0

# 4 digit FND 핀 설정
for segment in SEGMENT_PINS:
  GPIO.setup(segment, GPIO.OUT)
  GPIO.output(segment, GPIO.LOW)
for digit in DIGIT_PINS:
  GPIO.setup(digit, GPIO.OUT)
  GPIO.output(digit, GPIO.HIGH)

# 숫자에 따라 디스플레이에 표시할 LED 설정
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

# 디스플레이에 숫자를 표시하기 위한 함수
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

switchCount = 0  # 버튼이 눌린 시간을 카운트하는 변수


time.sleep(5)   # PIR 센서가 동작하기 위해 일정시간 대기해야 함.
print('System Ready...')


try:
  while True:
    now = datetime.now() # 현재 시간을 now에 대입
    
    # 현재 시간을 디스플레이에 표시할 수로 각각 분리하여 저장
    if now.hour >= 10:     # 시간 단위가 10이 넘으면, 현재시간의 십의자리와 일의자리를 각각 hour1, hour2에 대입.
      hour1 = now.hour//10  
      hour2 = now.hour%10
    else:                  # 시간 단위가 9 이하면, hour1은 0, hour2에 현재시간 대입.
      hour1 = 0
      hour2 = now.hour
    if now.minute >= 10 :  # 분 단위가 10이 넘으면, 현재 분의 십의자리와 일의자리를 각각 minute1, minute2에 대입
      minute1 = now.minute//10
      minute2 = now.minute%10
    else:                  # 분 단위가 9 이하면, minute1은 0, minute2에 현재 분 대입.
      minute1 = 0
      minute2 = now.minute

    # 센서 입력
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

    # 움직임이 5초간 없으면 moveDetect를 '1'로 한다
    if moveCount > 5:
      moveDetect = 1

    # 버튼을 2초간 누르면 moveDetect를 '1'로 한다.
    if switchVal == 1:
      switchCount += 0.1  # 버튼이 눌렸을 때 0.1초마다 switchCount를 0.1씩 증가.
      if switchCount >= 2: # 버튼을 2초간 누를 때
        moveDetect = 1     # moveDetect를 '1'로 한다 -> 경보음을 울린다.
        switchVal = 0

    # 버튼을 2초 이상 눌리지 않았을 때, switchCount를 초기화.
    if switchVal == 0:
      switchCount = 0




    # 경보 실행 코드
    if moveDetect == 1:  # 경보음이 울리고 LED가 켜진다.
      GPIO.output(LED_PIN, GPIO.HIGH) # LED ON
      pwm.start(20)      # Sound ON
      time.sleep(2) # 버튼을 눌러 경보음이 울렸을 때, 바로 꺼지는 것을 막기 위한 코드.
      while moveDetect == 1:
        if switchVal == 1:  # 버튼을 눌렀을 때 경보 실행 코드를 종료시킨다.
          moveCount = 0
          moveDetect = 0
        # 디스플레이에 현재 시간 표시
        display(1, hour1)
        display(2, hour2)
        display(3, minute1)
        display(4, minute2)
        switchVal = GPIO.input(SWITCH_PIN)
    elif moveDetect == 0: # 경보음과 LED가 꺼진다.
      pwm.start(0)  # Sound OFF
      GPIO.output(LED_PIN, GPIO.LOW) # LED OFF

finally:
  GPIO.cleanup()
  print('System Down')