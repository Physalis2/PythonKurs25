from board import LED
import time 

led_builtin = LED(4)

while (True):
   
    # Turn on LED
    led_builtin.on()

    # Wait 0.25 seconds
    time.sleep_ms(250)
    
    # Turn off LED
    led_builtin.off()

    # Wait 0.25 seconds
    time.sleep_ms(250)