# utilize gpio zero framework to interface gpio
# https://gpiozero.readthedocs.io
from gpiozero import LED
# utilize signal framework
from signal import pause

# connect GPIO pin 12 to led
led_red = LED(12)
# turn led "on"
led_red.on()

# prevent program from ending immediately
pause()
