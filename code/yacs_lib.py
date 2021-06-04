import os
import can

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
   
lib_canconfig("vcan")

bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=500000)
for msg in bus:
    print(msg)
