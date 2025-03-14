from board import LED
import time 

led_red = LED(1)
led_green = LED(2)
led_blue = LED(3)
led_builtin = LED(4)

while (True):
   
    # Turn on LEDs
    led_red.on()
    led_builtin.on()
    led_green.on()
    led_blue.on()

    # Wait 0.25 seconds
    time.sleep_ms(250)
    
    # Turn off LEDs
    led_red.off()
    led_builtin.off()
    led_green.off()
    led_blue.off()

    # Wait 0.25 seconds
    time.sleep_ms(250)