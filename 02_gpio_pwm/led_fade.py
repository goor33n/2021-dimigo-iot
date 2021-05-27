import RPi.GPIO as GPIO
import time

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# PWM 인스턴스 생성, 주파수 설정 (50)
# 1초에 50번 사이클이 돌게 하겠다
pwm = GPIO.PWM(LED_PIN, 50)
pwm.start(0)   # PWM 시작, duty cycle (0~100) 

try:
  for j in range(3):  # 3번 반복 range(0, 3, 1)
    # 서서히 켜짐 (0~100)
    for i in range(0, 101, 5):  # range(start, end, step) => 0부터 100까지 5칸씩
      pwm.ChangeDutyCycle(i)
      time.sleep(0.1)
    # 서서히 꺼짐 (100~0)
    for i in range(100, -1, -5):
      pwm.ChangeDutyCycle(i)
      time.sleep(0.1)

finally:
  pwm.stop()   # PWM 종료
  GPIO.cleanup()
  print("Clean up and exit")
