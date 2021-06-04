import cv2
import numpy as np
import glob
 
size = (640, 480)
out = cv2.VideoWriter('/home/pi/FTP/2021-05-02 10:17:19.043345.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
for filename in glob.glob('/home/pi/FTP/records/2021-05-02 10:17:19.043345/*.jpg'):
    img = cv2.imread(filename)
    out.write(img) 
out.release()
