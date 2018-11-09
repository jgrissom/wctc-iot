from gpiozero import LED, Button
import pygame
from picamera import PiCamera
from time import sleep
import datetime as dt
from PIL import Image

def main():
	running = True
	while running:
		# event handling, gets all events from the queue
		for event in pygame.event.get():
			# if the event is of type QUIT or Esc key is pressed
			if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
				running = False
	destroy()

def countdown():
	camera.start_preview()

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
	# determine the number of seconds that have elapsed since  midnight
	s = t.second + (t.minute * 60) + (t.hour * 60 * 60)
	# use date/time to generate unique file name
	camera.capture("/home/pi/Desktop/{0}~{1}.jpg".format(t.strftime("%Y-%m-%d"), s))
	sleep(2)
	
	camera.stop_preview()

def load_img(n):
	img = pygame.image.load('{0}.png'.format(n))
	screen.blit(img, (0, 0))
	pygame.display.update()
	
def destroy():
	print("cleanup")
	pygame.quit()
	
try:
	# initialize pygame
	pygame.init()
	screen = pygame.display.set_mode((1280, 800))
	pygame.mouse.set_visible(False)
	pygame.display.toggle_fullscreen()
	load_img("start")
	camera = PiCamera()
	# connect GPIO pin 4 to "yellow" button
	button_yellow = Button(4)
	button_yellow.when_released = countdown
	main()
except KeyboardInterrupt: # end when ctrl-c is pressed
	destroy()
