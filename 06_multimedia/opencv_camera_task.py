import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
  print('Camera open failed')
  exit()

while True:
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  edge = cv2.Canny(frame, 50, 100)
  if not ret:
    break

  cv2.imshow('frame', frame)
  cv2.imshow('gray', gray)
  cv2.imshow('edge', edge)

  if cv2.waitKey(10) == 13:
    break

cap.release()
cv2.destroyAllWindows()