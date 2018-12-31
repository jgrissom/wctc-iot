import datetime
from gpiozero import Button
from time import sleep

def log():
	# get current date / time
	t = datetime.datetime.now()
	# format date in json format for RESTful API
	t_json = "{0}-{1}-{2}T{3}:{4}:{5}".format(t.strftime("%Y"), t.strftime("%m"), t.strftime("%d"), t.strftime("%H"), t.strftime("%M"), t.strftime("%S"))
	print(t_json)
	
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
