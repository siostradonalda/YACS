from threading import Thread
import cv2
import os
import datetime
from pathlib import Path
from datetime import datetime
import threading

def t1loop():
    print('sasa')

t1 = threading.Thread(target=t1loop, args=())
t1.deamon = True
t1.start()


path = '/home/pi/FTP/RECORDS/'
catname = str(datetime.now())
os.mkdir(path+catname)
aviname = catname+'.avi'

avipath = path+catname+'/'+aviname
print(avipath)

#Path(aviname).touch(mode=0o777, exist_ok=True)
#touch(aviname)
#os.chmod(aviname, 777)

def t1():
    print(1)

t1 = Thread(target=t1(), args=())
t1.daemon = True
t1.start()

class WebcamVideoWriter(object):
    def __init__(self, src=0):
        # Create a VideoCapture object
        self.capture = cv2.VideoCapture(src)

        # Default resolutions of the frame are obtained (system dependent)
        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4))

        # Set up codec and output video settings
        self.codec = cv2.VideoWriter_fourcc('M','J','P','G')
        self.output_video = cv2.VideoWriter(avipath, self.codec, 8, (self.frame_width, self.frame_height))

        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()
    def update(self):
        # Read the next frame from the stream in a different thread
        while True:
            if self.capture.isOpened():
                (self.status, self.frame) = self.capture.read()

    def show_frame(self):
        # Display frames in main program
        if self.status:
            cv2.imshow('frame', self.frame)

        # Press Q on keyboard to stop recording
        key = cv2.waitKey(1)
        if key == ord('q'):
            self.capture.release()
            self.output_video.release()
            cv2.destroyAllWindows()
            exit(1)

    def save_frame(self):
        # Save obtained frame into video output file
        self.output_video.write(self.frame)

#       filename = path+catname+'/'+str(datetime.now())+'.jpg'
#        cv2.imwrite(filename, self.frame)

if __name__ == '__main__':
    webcam_videowriter = WebcamVideoWriter()
    while True:
        try:
            webcam_videowriter.show_frame()
            webcam_videowriter.save_frame()
        except AttributeError:
            pass
