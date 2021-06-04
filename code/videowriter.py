from threading import Thread
import cv2
import time
import datetime
from datetime import datetime
import os
from pathlib import Path

string_date1 = '/home/pi/FTP/RECORDS/'
cat_name = str(datetime.now())
string_date = '/home/pi/FTP/RECORDS/'+cat_name
os.mkdir(string_date)
os.chmod(string_date, 777)
Path(string_date+'111.avi').touch(mode=0o777, exist_ok=True)
os.chmod(string_date+'111.avi', 777)

class WebcamVideoWriter(object):
    def __init__(self, src=0):
        # Create a VideoCapture object
        self.capture = cv2.VideoCapture(src)

        # Default resolutions of the frame are obtained (system dependent)
        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4))

        # Set up codec and output video settings
        self.codec = cv2.VideoWriter_fourcc('M','J','P','G')
        self.output_video = cv2.VideoWriter(string_date+'111.avi', self.codec, 15, (self.frame_width, self.frame_height))

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
 
        filename = string_date+'/'+str(datetime.now())+'.jpg'
        cv2.imwrite(filename, self.frame)

if __name__ == '__main__':
    webcam_videowriter = WebcamVideoWriter()
    while True:
        try:
            webcam_videowriter.show_frame()
            webcam_videowriter.save_frame()
        except AttributeError:
            pass
