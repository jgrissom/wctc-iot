from picamera import PiCamera
from time import sleep
import datetime as dt
from PIL import Image

def countdown():
	img = Image.open("ready.png")
	o = camera.add_overlay(img.tobytes(), size=img.size)
	# layer = stacking order
	o.layer = 10
	sleep(1)
	camera.remove_overlay(o)
	for i in range(3, 0, -1):
		img = Image.open("%s.png" %i)
		o = camera.add_overlay(img.tobytes(), size=img.size)
		o.layer = 10
		sleep(1)
		camera.remove_overlay(o)
	# determine current date/time
	t = dt.datetime.now()
	# determine the number of seconds that have elapsed since midnight
	s = t.second + (t.minute * 60) + (t.hour * 60 * 60)
	# use the date/time to generate a unique file name for photos (1/1/2018~21223.png)
	camera.capture("/home/pi/Desktop/{0}~{1}.jpg".format(t.strftime("%Y-%m-%d"), s))
	sleep(2)

camera = PiCamera()

camera.start_preview()

countdown()

camera.stop_preview()
