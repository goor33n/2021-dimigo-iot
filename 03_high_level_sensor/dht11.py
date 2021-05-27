import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
DHT_PIN = 4

try:
  while True:
    h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
    if h is not None and t is not None:
      print(f'Temperature={t:.1f}*, Humidity={h:.1f}%')  # python 문법: 앞에 f를 쓰면 {}를 이용해 값을 표시할 수 있음.
    else:
      print('Read Error')
    time.sleep(0.1)
finally:
  print('bye')