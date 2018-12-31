from gpiozero import Button
from time import sleep

def log():
	# create a new event
	url = 'https://modas.azurewebsites.net/api/event/'
	headers = { 'Content-Type': 'application/json'}
	payload = { 'timestamp': '2019-01-21T10:22:33', 'flagged': False, 'locationId': 1 }
	print(payload)
	
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
