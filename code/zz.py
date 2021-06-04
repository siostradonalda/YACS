from threading import Thread
import cv2
import os
import datetime
import drivers
from pathlib import Path
from datetime import datetime
import threading
import can
from threading import Timer
from w1thermsensor import W1ThermSensor, Sensor 

sens_temp_in = W1ThermSensor(Sensor.DS18B20, "0000095e76cc")
sens_temp_out = W1ThermSensor(Sensor.DS18B20, "3c01d0759247")
sens_temp_vent = W1ThermSensor(Sensor.DS18B20, "")

def t1loop():
    print('sasa')

t1 = threading.Thread(target=t1loop, args=())
t1.deamon = True
t1.start()

os.system('sudo ip link add dev vcan0 type vcan')
os.system('sudo ifconfig vcan0 up')
bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=500000)

mylcd = drivers.Lcd()

def lib_canconfig(cantype):
    if cantype=="vcan":
        os.system('sudo ip link add dev vcan0 type vcan')
        os.system('sudo ifconfig vcan0 up')
        bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=500000)
    if cantype=="lscan":
        os.system('sudo ip link set can0 up type can bitrate 125000') 
        bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=125000)
    if cantype=="hscan":
        os.system('sudo ip link set can0 up type can bitrate 500000')
        bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)

#lib_canconfig("vcan")

lmanip = 0
rmanip = 0

def getCanMsg():
    msg = bus.recv(1.0)
    for msg in bus:
        if msg.arbitration_id == 0x2A0:
            lmanip = msg.data[1]
            rmanip = msg.data[3] 
            print(lmanip)

timer1 = Timer(1, getCanMsg)
timer1.start()

path = '/home/pi/FTP/RECORDS/'
catname = str(datetime.now())
os.mkdir(path+catname)
aviname = catname+'.avi'

avipath = path+catname+'/'+ aviname
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
        self.codec = cv2.VideoWriter_fourcc('X','V','I','D')
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
        temperature_in = sens_temp_in.get_temperature()
        temperature_out = sens_temp_out.get_temperature()
        temperature_vent = sens_temp_vent.get_temperature()

#        mylcd.lcd_display_string("%s %s %s" % (round(temperature_in, 1), round(temperature_out, 1), round(temperature_out, 1)), 1)
        print("%s %s %s" % (round(temperature_in, 1), round(temperature_out, 1), round(temperature_out, 1)), 1)
#        mylcd.lcd_display_string("%s  %s  %s" % (str(lmanip)), (str(datetime.now().strftime("%H:%M"))), (str(rmanip)), 2)
        try:
            webcam_videowriter.show_frame()
            webcam_videowriter.save_frame()
        except AttributeError:
            pass
