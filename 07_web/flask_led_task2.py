from flask import Flask, render_template
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
  return render_template("led2.html")

@app.route("/led/<cr>/<op>")
def led_op(cr, op):
  if cr == "red":
    if op == "on":
      GPIO.output(RLED_PIN, GPIO.HIGH)
      return "RED LED ON"
    elif op == "off":
      GPIO.output(RLED_PIN, GPIO.LOW)
      return "RED LED OFF"

  elif cr == "blue":
    if op == "on":
      GPIO.output(BLED_PIN, GPIO.HIGH)
      return "BLUE LED ON"
    elif op == "off":
      GPIO.output(BLED_PIN, GPIO.LOW)
      return "BLUE LED OFF"
    
  else:
    return "Error"


# 터미널에서 직접 실행시킨 경우
if __name__ == "__main__":
  try:
    app.run(host="0.0.0.0")
  finally:
    GPIO.cleanup()