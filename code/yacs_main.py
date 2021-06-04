import cv2 
import os 
import datetime 
import drivers 
from pathlib import Path 
from datetime import datetime 
from threading import Thread 
import threading 
from threading import Timer

import can 
import time 
import numpy as np 
import tkinter as tk 
from PIL import Image, ImageTk 
from w1thermsensor import W1ThermSensor, Sensor
from videoWriter_lib import WebcamVideoWriter
import videoWriter_lib

sens_temp_in = W1ThermSensor(Sensor.DS18B20, "0000095e76cc")
sens_temp_out = W1ThermSensor(Sensor.DS18B20, "3c01d0759247")
sens_temp_vent = W1ThermSensor(Sensor.DS18B20, "")

mylcd = drivers.Lcd()

#Set up GUI
window = tk.Tk()  #Makes main window
window.wm_title("YACS")
window.config(background="#FFFFFF")

#Graphics window
imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
#cap = cv2.VideoCapture(0)

#Slider window (slider controls stage position)
sliderFrame = tk.Frame(window, width=600, height=100)
sliderFrame.grid(row = 600, column=0, padx=10, pady=2)

#show_frame()  #Display 2

os.system('sudo ip link set can0 up type can bitrate 125000')
#os.system('sudo ifconfig can0 up')
bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=125000)

lmanip = "0xFF"
rmanip = "0xFF"

temperature_in = 0xFF
temperature_out = 0xFF
temperature_vent = 0xFF

#class WebcamVideoWriter(object):
#    def __init__(self, src=0):
#        # Create a VideoCapture object
#        path = '/home/pi/FTP/RECORDS/'
#        catname = str(datetime.now())
#        os.mkdir(path+catname)
#        aviname = catname+'.avi'
#
#        avipath = path+catname+'/'+aviname
#        print(avipath)
#       print('FF')
#        self.capture = cv2.VideoCapture(src)

        # Default resolutions of the frame are obtained (system dependent)
#        self.frame_width = int(self.capture.get(3))
#        self.frame_height = int(self.capture.get(4))

        # Set up codec and output video settings
#       self.codec = cv2.VideoWriter_fourcc('M','J','P','G')
#        self.codec = cv2.VideoWriter_fourcc('X','V','I','D')
#        self.output_video = cv2.VideoWriter(avipath, self.codec, 14, (self.frame_width, self.frame_height))

        # Start the thread to read frames from the video stream
#        self.thread = Thread(target=self.update, args=())
#        self.thread.daemon = True
#        self.thread.start()
#3        lmain.after(5, self.show_tk_frame) 
#3    def update(self):
        # Read the next frame from the stream in a different thread
#        while True:
 #           if self.capture.isOpened():
  #              (self.status, self.frame) = self.capture.read()

 #   def show_tk_frame(self):
        # Display frames in main program
 #       if self.status:
  #          cv2.imshow('frame', self.frame)
    #        print('1')
   #         cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
 #           img = Image.fromarray(cv2image)
 #           imgtk = ImageTk.PhotoImage(image=img)
 #3           lmain.imgtk = imgtk
 #3           lmain.configure(image=imgtk)
 #           #time.sleep(0.2)
 #           lmain.after(5, self.show_tk_frame) 
            #_, frame = cap.read()
            #frame = cv2.flip(frame, 1)
 #   def show_frame(self):
  #3      if self.status:
            #cv2.setWindowProperty('frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEEN)
  #          cv2.imshow('frame', self.full_frame)
            #print('aa')
            #cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
            #img = Image.fromarray(cv2image)
            #imgtk = ImageTk.PhotoImage(image=img)
            #lmain.imgtk = imgtk
            #lmain.configure(image=imgtk)
            #lmain.after(10, self.show_frame) 

        # Press Q on keyboard to stop recording
#        key = cv2.waitKey(1)
#        if key == ord('q'):
#3            self.capture.release()
#            self.output_video.release()
#            cv2.destroyAllWindows()
#            timer_videoReg.do_run = False
#            exit(1)

#    def save_frame(self):
#        # Save obtained frame into video output file
#        self.output_video.write(self.frame)
#        time.sleep(0.2)

#       filename = path+catname+'/'+str(datetime.now())+'.jpg'
#       cv2.imwrite(filename, self.frame)

#webcam_videowriter = videoWriter_lib.WebcamVideoWriter()

def getVideo():
    if self.status:
        cv2.imshow('frame', selft.frame)

def getCanMsg():
    global lmanip
    global rmanip
    msg = bus.recv(1.0)
    for msg in bus:
        if msg.arbitration_id == 0x2A0:
            lmanip = msg.data[3]  
            rmanip = msg.data[1]
#            print(lmanip)

def updateTemp():
    global temperature_in
    global temperature_out
    global temperature_vent
    while 1:
        #time.sleep(1)
        temperature_in = sens_temp_in.get_temperature()
        temperature_out = sens_temp_out.get_temperature()
        temperature_vent = temperature_out #sens_temp_out.get_temperature()

def setLcd():
    global temperature_in
    global temperature_out
    global temperature_vent
    k = 0
    while 1:
#         print("2")
         #time.sleep(0.5)
         mylcd.lcd_display_string("%s %s %s" % (round(temperature_in, 1), round(temperature_out, 1), round(temperature_out, 1)), 1)
#         print("%s %s %s" % (round(temperature_in, 1), round(temperature_out, 1), round(temperature_out, 1)), 1)
         k = k + 1
         if k%2==1:
#             print('3')
             mylcd.lcd_display_string("%s  %s  %s" % (lmanip, str(datetime.now().strftime("%H %M")), rmanip), 2)
         else:
#             print('4 %s' % lmanip)
             mylcd.lcd_display_string("%s  %s  %s" % (lmanip, str(datetime.now().strftime("%H:%M")), rmanip), 2)

def updateVideo():

    while 1:
        if self.capture.isOpened():
            (self.status, self.frame) = self.capture.read()


def videoReg():
    while 1:
        try:
#           print('LLKLKL')
            #time.sleep(2)
           # webcam_videowriter.show_tk_frame()
           # webcam_videowriter.save_frame()
            getVideo()
        except AttributeError:
            pass
    

def lib_canconfig(cantype):
    if cantype=="vcan":
 #       print("5")
        os.system('sudo ip link add dev vcan0 type vcan')
        os.system('sudo ifconfig vcan0 up')
        bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=50000)
    if cantype=="lscan":
        os.system('sudo ip link set can0 up type can bitrate 125000') 
        bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=125000)
    if cantype=="hscan":
        os.system('sudo ip link set can0 up type can bitrate 500000')
        bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=50000)

def timer_init():
    # while True:
    lib_canconfig(cantype="lscan")

    #time.sleep(1)
    #time.sleep(1)
#    os.system('pkill -9 python3*')
#    time.sleep(1)
    try:
        os.system('sudo chmod 777 /sys/class/i2c-adapter/i2c-1/new_device')
        os.system('sudo echo pcf8563 0x51 > /sys/class/i2c-adapter/i2c-1/new_device')
        os.system('sudo hwclock -s')
    except AttributeError:
        pass
#    print(6)
    timer_getCanMsg.start()
    timer_setLcd.start()
#   timer_videoReg.start()
    timer_updateTemp.start()

#Path(aviname).touch(mode=0o777, exist_ok=True)
#touch(aviname)
#os.chmod(aviname, 777)

timer_getCanMsg = Timer(1, getCanMsg)
timer_setLcd = Timer(2, setLcd)
#timer_videoReg = Timer(3, videoReg)
timer_updateTemp = Timer(4, updateTemp)
timer_init = threading.Thread(group=None,target=timer_init(), name="timer_init", kwargs={}, daemon=True)
timer_init.start()

#window.mainloop()  #Starts GUI
if __name__ == '__main__':
    webcam_videowriter = videoWriter_lib.WebcamVideoWriter()
    while True:
        xx = True
        #time.sleep(1)
        try:
#            print("AAAAAAA")
            webcam_videowriter.show_frame()
            webcam_videowriter.save_frame()
        except AttributeError:
            pass

