import cv2
import time

import cv2 as cv
import time
camera_port =0
camera = cv.VideoCapture(camera_port, cv.CAP_DSHOW) # Added cv.CAP_DSHOW
return_value, image = camera.read()
cv.imwrite("image.png", image)
camera.release()
cv.destroyAllWindows
time.sleep(5)
import camreadycode

time.sleep(18)








