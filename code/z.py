import cv2
import time

cap = cv2.VideoCapture(0)
frameCount=0
start_time = time.time()
capture_duration = 10
while(int(time.time() -start_time) < capture_duration):
        ret, frame = cap.read()
        frameCount = frameCount+1
print(frameCount)
