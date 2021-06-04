import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('output.avi', fourcc, 20, (640, 480))

i = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    cv2.imshow('frame',frame)
    #out.write(frame)
    # read image as grey scale
 
    # save image
    status = cv2.imwrite('/home/pi/recc/zpython_grey' + str(i) +'.png', frame)
     
    i = i + 1

    print("Image written to file-system : ",status)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
