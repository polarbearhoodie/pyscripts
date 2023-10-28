import time
import cv2

cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 7680)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 4320)

while True:
	result, image = cap.read()
	t = time.localtime()
	utc_str = str(int(time.mktime(t)))
	cv2.imwrite("photos/{}.jpg".format(utc_str), image)
	time.sleep(6)


