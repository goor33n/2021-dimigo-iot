import RPi.GPIO as GPIO

LED_PIN = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try: 
  while True:
    val = input("\n\n--------------------------\n|                        |\n| 0: OFF, 1: ON, 9: EXIT |\n|                        |\n--------------------------\n> ")
    #val = input("0:off, 1:on, 9: exit")
    if val == '0':
      GPIO.output(LED_PIN, GPIO.LOW)
      print('LED OFF')
    elif val == '1':
      GPIO.output(LED_PIN, GPIO.HIGH)
      print('LED ON')
    elif val == '9':
      break

finally:
  GPIO.cleanup()
  print("Clean up and exit")
