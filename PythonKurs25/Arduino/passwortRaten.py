from board import LED
import time 

led_red = LED(1)
led_green = LED(2)
led_blue = LED(3)
led_builtin = LED(4)

led_blue.on()
led_green.on()
led_red.on()
passwort = input("Passwort festlegen:")
led_blue.off()
led_green.off()
led_red.off()
    
while (True):
    led_blue.on()
    raten = input("Passwort eigeben")
    led_blue.off()
    if raten == passwort:
        led_green.on()
        time.sleep_ms(250)
        led_green.off()
        time.sleep_ms(250)
        led_green.on()
        time.sleep_ms(250)
        led_green.off()
        time.sleep_ms(250)
        led_green.on()
        time.sleep_ms(250)
        led_green.off()
        time.sleep_ms(250)
    else:
        led_red.on()
        time.sleep_ms(250)
        led_red.off()
        time.sleep_ms(250)
        led_red.on()
        time.sleep_ms(250)
        led_red.off()
        time.sleep_ms(250)
        led_red.on()
        time.sleep_ms(250)
        led_red.off()
        time.sleep_ms(250)