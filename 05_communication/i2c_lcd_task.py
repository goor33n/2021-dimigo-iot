from lcd import drivers
import time
import datetime

display = drivers.Lcd()

try:
  print("Writing to display")
  while True:
    now = datetime.datetime.now()
    display.lcd_display_string(now.strftime("%x %X"), 1)
    time.sleep(0.001)
finally:
  print("cleaning up!")
  display.lcd_clear()
    