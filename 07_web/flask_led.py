from flask import Flask
import RPi.GPIO as GPIO

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Flask 객체 생성
# __name__은 파일명
app = Flask(__name__)


# 라우팅을 위한 뷰 함수
@app.route("/")
def hello():
  return '''
    <p>Hello, Flask</p>
    <a href="/led/on">LED ON</a>
    <a href="/led/off">LED OFF</a>
  '''

@app.route("/led/<op>")
def led_op(op):
  if op == "on":
    GPIO.output(LED_PIN, GPIO.HIGH)
    return '''
      <p>LED ON</p>
      <a href="/">Go Home</a>
    '''
  elif op == "off":
    GPIO.output(LED_PIN, GPIO.LOW)
    return '''
      <p>LED OFF</p>
      <a href="/">Go Home</a>
    '''


# 터미널에서 직접 실행시킨 경우
if __name__ == "__main__":
  try:
    app.run(host="0.0.0.0")
  finally:
    GPIO.cleanup()