import RPi.GPIO as GPIO
import time

RED_LED = 17
YEL_LED = 27
GRE_LED = 22

GPIO.setmode(GPIO.BCM)  # GPIO.BCM or GPIO.BOARD
GPIO.setup(RED_LED, GPIO.OUT)  # GPIO.OUT or GPIO.IN
GPIO.setup(YEL_LED, GPIO.OUT)  # GPIO.OUT or GPIO.IN
GPIO.setup(GRE_LED, GPIO.OUT)  # GPIO.OUT or GPIO.IN

# def blink(red, yellow, green):
    

GPIO.output(RED_LED, GPIO.HIGH) # LED_RED 1
print("RED LED ON")
time.sleep(2)
GPIO.output(RED_LED, GPIO.LOW) # LED_RED 0
print("RED LED OFF")
GPIO.output(YEL_LED, GPIO.HIGH) # LED_YELLOW 1
print("YELLOW LED ON")
time.sleep(2)
GPIO.output(YEL_LED, GPIO.LOW) # LED_YELLOW 0
print("YELLOW LED OFF")
GPIO.output(GRE_LED, GPIO.HIGH) # LED_GREEN 1
print("GREEN LED ON")
time.sleep(2)
GPIO.output(GRE_LED, GPIO.LOW) # LED_GREEN 0
print("GREEN LED OFF")

GPIO.cleanup()  # GPIO 핀 상태 초기화
