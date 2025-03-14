import time
from hs3003 import HS3003
from machine import Pin, I2C

bus = I2C(1, scl=Pin(15), sda=Pin(14))
hts = HS3003(bus)
count = -1
print ("Nr. rH in %  Temp in °C")

while count < 900:
    rH   = hts.humidity()
    temp = hts.temperature()
    count += 1
    print ("%3d %5.2f %5.2f" %(count, rH, temp))
    time.sleep_ms(200)