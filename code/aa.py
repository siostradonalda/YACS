#! /usr/bin/env python

# importing cv2 module
import cv2
import os
import time
import datetime
import drivers
from datetime import datetime
#import W1ThermSensor
from w1thermsensor import W1ThermSensor, Sensor

#sens_temp_in = W1ThermSensor(Sensor.DS18B20, "0000095e76cc")
#sens_temp_out = W1ThermSensor(Sensor.DS18B20, "3c01d0759247")
#sens_temp_vent = W1ThermSensor(Sensor.DS18B20, "")

i = 0

#mylcd = drivers.Lcd()

# Create a new VideoCapture object
cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('output.avi', fourcc, 20, (640, 480))

string_date ='/media/pi/CD_ROM1/RECORDS/'

if os.path.exists(string_date):
    string_date = string_date
else:
    string_date = '/home/pi/FTP/RECORDS/'


string_date = string_date+str(datetime.now())
os.mkdir(string_date)

i = 0

while True:
    #lib_canconfig('vcan')
   # temperature_in = sens_temp_in.get_temperature()
   # temperature_out = sens_temp_out.get_temperature()
   # temperature_vent = sens_temp_vent.get_temperature()

    ret, img = cam.read()

#   if i==100:

    filename = string_date+'/'+str(datetime.now())+'.jpg'

    cv2.imshow('Preview', img)

    # Using cv2.imwrite() method saving the image
    cv2.imwrite(filename, img)

    print(string_date+str(i))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#    mylcd.lcd_display_string("%s %s %s" % (round(temperature_in, 1), round(temperature_out, 1), round(temperature_out, 1)), 1)
#    mylcd.lcd_display_string("1/5  %s  2/5" % (str(datetime.now().strftime("%H:%M"))), 2)
  

 #   time.sleep(1)
cam.release()
out.release()
cv2.destroyAllWindows()

