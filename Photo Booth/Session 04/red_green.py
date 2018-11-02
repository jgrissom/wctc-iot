# utilize gpio zero framework to interface gpio
# https://gpiozero.readthedocs.io
from gpiozero import LED, Button
# utilize pygame framework
import pygame
# utilize time framework
from time import sleep

# connect GPIO pin 12 to led
led_red = LED(12)
# connect GPIO pin 4 to button
button_red = Button(4)
# connect GPIO pin 19 to led
led_green = LED(19)
# connect GPIO pin 25 to button
button_green = Button(25)

# define colros using RGB values
red = [255, 0, 0]
green = [0, 255, 0]
black = [0, 0, 0]

def main():
	# when button is pressed call function
	button_green.when_pressed = show_green
	# when button is released call function
	button_green.when_released = hide_green
	# when button is pressed call function
	button_red.when_pressed = show_red
	# when button is released call function
	button_red.when_released = hide_red
	
	# create program loop
	running = True
	while running:		
		# event handling, gets all events from the queue
		for event in pygame.event.get():
			# if the event is of type QUIT or Esc key is pressed
			if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
				running = False
			# if "r" is pressed
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
				show_red()
			# if "r" is released
			elif event.type == pygame.KEYUP and event.key == pygame.K_r:
				hide_red()
			# if "g" is pressed
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
				show_green()
			# if "g" is released
			elif event.type == pygame.KEYUP and event.key == pygame.K_g:
				hide_green()
		# add a delay to slow down event loop
		sleep(.2)
	destroy()

def fill_background(fill_color):
	screen.fill(fill_color)
	pygame.display.update()

def show_green():
	fill_background(green)
	# blink (on time seconds, off time seconds, number of times to blink (None to run forever), run as background thread)
	led_green.blink(.25, .25, None, True)
	
def hide_green():
	fill_background(black)
	led_green.off()
	
def show_red():
	fill_background(red)
	led_red.on()

def hide_red():
	fill_background(black)
	led_red.off()

def destroy():
	print("cleanup")
	pygame.quit()

try:
	# initialize pygame
	pygame.init()
	pygame.display.set_caption("Red / Green")
	screen = pygame.display.set_mode((400,400))
	# screen.fill(black)
	# pygame.display.update()
	fill_background(black)
	main()
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
	destroy()
