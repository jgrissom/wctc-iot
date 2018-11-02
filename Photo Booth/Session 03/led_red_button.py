# utilize gpio zero framework to interface gpio
# https://gpiozero.readthedocs.io
from gpiozero import LED, Button
# utilize signal framework
from signal import pause

# connect GPIO pin 12 to led
led_red = LED(12)
# connect GPIO pin 4 to button
button_red = Button(4)

# when button is pressed "toggle" the red led
button_red.when_pressed = led_red.toggle

# prevent program from ending immediately
pause()
