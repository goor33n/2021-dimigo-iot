import RPi.GPIO as GPIO

SERVO_MOTOR_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_MOTOR_PIN, GPIO.OUT)

# servo motor 제어에 필요한 frequency: 50Hz
pwm = GPIO.PWM(SERVO_MOTOR_PIN, 50)
pwm.start(7.5) # 7.5 (0도)

# 1: 0도, 2: -90도, 3: 90도, 9: exit
try:
  while True:
    val = input('1: 0도, 2: -90도, 3: 90도, 9: exit\n> ')
    if val == '1':
      pwm.ChangeDutyCycle(7.5)
    elif val == '2':
      # pwm.ChangeDutyCycle(5)
      pwm.ChangeDutyCycle(2.5)
    elif val == '3':
      # pwm.ChangeDutyCycle(10)
      pwm.ChangeDutyCycle(10)
    elif val == '9':
      break
finally:
  pwm.stop()
  GPIO.cleanup()
  print("Clean up and Exit")
