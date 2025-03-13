"""
  IMU Capture
  This example uses the on-board IMU to start reading acceleration and gyroscope
  data from on-board IMU and prints it to the Serial Monitor for one second
  when the significant motion is detected.
  You can also use the Serial Plotter to graph the data.
  The circuit:
  - Arduino Nano 33 BLE or Arduino Nano 33 BLE Sense Rev2 board.
  Created by Don Coleman, Sandeep Mistry
  Modified by Dominic Pajak, Sandeep Mistry
  This example code is in the public domain.
"""

import time
import bmi270#, bmm150
from machine import Pin, I2C

bus = I2C(1, scl=Pin(15), sda=Pin(14))
bmi = bmi270.BMI270(bus)
# bmm = bmm150.BMM150(bus)

accelerationThreshold = 2.5 # threshold of significant in G's
numSamples = 119
samplesRead = numSamples
n = 0

print("aX,aY,aZ,gX,gY,gZ")

while n<8: #(True):
    # wait for significant motion
    while samplesRead == numSamples: 
        # read the acceleration data
        [aX, aY, aZ] = bmi.accel()
        # sum up the absolutes
        aSum = abs(aX) + abs(aY) + abs(aZ)
        # check if it's above the threshold
        if aSum >= accelerationThreshold:
            # reset the sample read count
            samplesRead = 0
            break
    # check if the all the required samples have been read since the last time the significant motion was detected
    while samplesRead < numSamples:
        # check if both new acceleration and gyroscope data is available
        #if bmi.accelAvailable() & bmi.gyroAvailable():
            # read the acceleration and gyroscope data
            #[aX, aY, aZ] = bmi.accel()
            #[gX, gY, gZ] = bmi.gyro()
        samplesRead += 1

            # print the data in CSV format
        print('{:>8.3f}, {:>8.3f}, {:>8.3f},'.format(*bmi.accel()),'{:>8.3f}, {:>8.3f}, {:>8.3f}'.format(*bmi.gyro()))
            #time.sleep_ms(500)

        if samplesRead == numSamples: 
                # add an empty line if it's the last sample
            print("")
            n += 1
