from flask import Flask
import RPi.GPIO as GPIO

RLED_PIN = 4
BLED_PIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(RLED_PIN, GPIO.OUT)
GPIO.setup(BLED_PIN, GPIO.OUT)

# Flask 객체 생성
# __name__은 파일명
app = Flask(__name__)

# 라우팅을 위한 뷰 함수
@app.route("/")
def hello():
  return '''
    <p>Hello, Flask</p>
    <a href="/led/red/on">RED LED ON</a>
    <a href="/led/red/off">RED LED OFF</a>
    <br>
    <a href="/led/blue/on">BLUE LED ON</a>
    <a href="/led/blue/off">BLUE LED OFF</a>
  '''

@app.route("/led/<cr>/<op>")
def led_op(cr, op):
  if cr == "red":
    if op == "on":
      GPIO.output(RLED_PIN, GPIO.HIGH)
      return '''
        <p>RED LED ON</p>
        <a href="/">Go Home</a>
      '''
    elif op == "off":
      GPIO.output(RLED_PIN, GPIO.LOW)
      return '''
        <p>RED LED OFF</p>
        <a href="/">Go Home</a>
      '''
  elif cr == "blue":
    if op == "on":
      GPIO.output(BLED_PIN, GPIO.HIGH)
      return '''
        <p>BLUE LED ON</p>
        <a href="/">Go Home</a>
      '''
    elif op == "off":
      GPIO.output(BLED_PIN, GPIO.LOW)
      return '''
        <p>BLUE LED OFF</p>
        <a href="/">Go Home</a>
      '''


# 터미널에서 직접 실행시킨 경우
if __name__ == "__main__":
  try:
    app.run(host="0.0.0.0")
  finally:
    GPIO.cleanup()