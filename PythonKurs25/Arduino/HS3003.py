import time
from hs3003 import HS3003
from machine import Pin, I2C

bus = I2C(1, scl=Pin(15), sda=Pin(14))
hts = HS3003(bus)

while True:
    rH   = hts.humidity()
    temp = hts.temperature()
    print ("rH: %.2f%% T: %.2fC" %(rH, temp))
    time.sleep_ms(100)