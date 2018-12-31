import requests
from gpiozero import Button
from time import sleep

def log():
	# request 1 event (replace with your own API)
	r = requests.get('https://modas.azurewebsites.net/api/event/1')
	print(r.status_code)
	print(r.text)
	
# init button
button = Button(8)
button.when_released = log

try:
	# program loop
	while True:
		sleep(.001)
# detect Ctlr+C
except KeyboardInterrupt:
	print("goodbye")
