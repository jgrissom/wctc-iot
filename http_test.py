from gpiozero import Button
from time import sleep

def log():
	print("log")

# init button
button = Button(8)
button.when_released = log

try:
	# program loop
	while True:
		sleep(.001)
# detect Ctlr+C
except KeyboardInterrupt:
	if m.armed:
		m.disarm_system()
