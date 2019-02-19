from gpiozero import Button, LED, Buzzer
from signal import pause
import time

def start():
	led.on()
	buzzer.on()
	print(time.time())

def end():
	led.off()
	buzzer.off()
	print(time.time())

button = Button(14)
led = LED(16)
buzzer = Buzzer(25)

button.when_pressed = start
button.when_released = end

pause()
