#! /usr/bin/env python

#define VAR 

# importing cv2 module
import cv2
import os
import time
import datetime
import drivers
import can
from datetime import datetime
#import W1ThermSensor
from w1thermsensor import W1ThermSensor, Sensor
from threading import Thread
from threading import Timer
import threading


#sens_temp_in = W1ThermSensor(Sensor.DS18B20, "0000095e76cc")
#sens_temp_out = W1ThermSensor(Sensor.DS18B20, "3c01d0759247")
#sens_temp_vent = W1ThermSensor(Sensor.DS18B20, "")

os.system('sudo ip link add dev vcan0 type vcan')
os.system('sudo ifconfig vcan0 up')
bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=50000)

#mylcd = drivers.Lcd()
i = 0
k = 0
lmanip = 0
rmanip = 0

def getCanMsg():
    msg = bus.recv(1.0)
    for msg in bus:
        if msg.arbitration_id == 0x2A0:
            lmanip = msg.data[1]
            rmanip = msg.data[3] 
            print(lmanip)

def lib_canconfig(cantype):
    if cantype=="vcan":
        print("ZZZZ")
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
    lib_canconfig(cantype="vcan")

    os.system('sudo chmod 777 /sys/class/i2c-adapter/i2c-1/new_device')
    time.sleep(1)
    os.system('sudo echo pcf8563 0x51 > /sys/class/i2c-adapter/i2c-1/new_device')
    time.sleep(1)
    os.system('sudo hwclock -r')
    print(1)
    timer_getCanMsg.start()
    timer_setLcd.start()

#os.system('sudo ip link add dev vcan0 type vcan')
#os.system('sudo ifconfig vcan0 up')
#bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=500000)

def setLcd():
    while 1:
         print("ASD")
         time.sleep(1)
    #    temperature_in = sens_temp_in.get_temperature()
    #    temperature_out = sens_temp_out.get_temperature()
    #    temperature_vent = sens_temp_vent.get_temperature()
    #    mylcd.lcd_display_string("%s %s %s" % (round(temperature_in, 1), round(temperature_out, 1), round(temperature_out, 1)), 1)
    #   print("%s %s %s" % (round(temperature_in, 1), round(temperature_out, 1), round(temperature_out, 1)), 1)
    #    if k%2==0:
    #        mylcd.lcd_display_string("1/5  %s  2/5" % (str(datetime.now().strftime("%H %M"))), 2)
     #   else:
     #       mylcd.lcd_display_string("1/5  %s  2/5" % (str(datetime.now().strftime("%H:%M"))), 2)

timer_getCanMsg = Timer(1, getCanMsg)
timer_setLcd = Timer(2, setLcd)
timer_init = threading.Thread(group=None,target=timer_init(), name="timer_init", kwargs={}, daemon=True)
timer_init.start()

while True:
   #print('aaaa')
   # time.sleep(1)
   k = k + 1
   # time.sleep(1)
