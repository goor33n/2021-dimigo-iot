import picamera
import time

path = '/home/pi/src4/06_multimedia'

camera = picamera.PiCamera()

try:
  camera.resolution = (640, 480)
  camera.start_preview()
  time.sleep(3)
  camera.rotation = 180 

  # camera.capture('%s/photo.jpg' % path) # 사진 촬영

  camera.start_recording('%s/video.h264' % path) # 동영상 촬영
  time.sleep(10) # 동영상 촬영
  camera.stop_recording() # 동영상 촬영

finally:
  camera.stop_preview