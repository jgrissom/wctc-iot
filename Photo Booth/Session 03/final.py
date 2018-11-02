# utilize gpio zero framework to interface gpio
# https://gpiozero.readthedocs.io
from gpiozero import LED, Button
# utilize signal framework
from signal import pause

# connect GPIO pin 12 to led
led_red = LED(12)
# connect GPIO pin 4 to button
button_red = Button(4)
# connect GPIO pin 19 to led
led_green = LED(19)
# connect GPIO pin 25 to button
button_green = Button(25)

# when button is pressed turn green led on
button_green.when_pressed = led_green.on
# when button is released turn green led off
button_green.when_released = led_green.off


# when button is pressed "toggle" the red led
button_red.when_pressed = led_red.toggle

# prevent program from ending immediately
pause()
