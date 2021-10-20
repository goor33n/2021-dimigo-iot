import picamera
import time

path = '/home/pi/src4/06_multimedia'

camera = picamera.PiCamera()

try:
  camera.resolution = (640, 480)
  camera.start_preview()
  time.sleep(3)
  camera.rotation = 180 

  while True:
    now_str = time.strftime("%Y%m%d_%H%M%S")
      
    cmd = input("photo:1, video:2, exit:9 > ")

    if cmd == '1':
      camera.capture('%s/photo_%s.jpg' % (path, now_str)) # 사진 촬영
      print('사진 촬영')

    elif cmd == '2':
      camera.start_recording('%s/video_%s.h264' % (path, now_str)) # 동영상 촬영
      input('press enter to stop recoding..')
      camera.stop_recording() # 동영상 촬영
      print('동영상 촬영')

    elif cmd == '9':
      break
    else:
      print("incorrect command")

finally:
  camera.stop_preview