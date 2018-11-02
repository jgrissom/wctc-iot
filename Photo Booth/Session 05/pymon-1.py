# utilize pygame framework
import pygame
# utilize gpio zero framework to interface gpio
from gpiozero import LED, Button
# utilize time framework
from time import sleep
# utilize random framework
import random

# connect GPIO pin 12 to led
led_red = LED(12)
# connect GPIO pin 4 to button
button_yellow = Button(4)
# connect GPIO pin 12 to led
led_green = LED(19)
# connect GPIO pin 4 to button
button_blue = Button(25)

# define colors using RGB values
black = [60, 60, 60]
blue = [0, 0, 255]
yellow = [255, 255, 0]

displayed = []
names = ["BLUE", "YELLOW"]

def main():
	led_red.on()
	# generate random number between 5 and 10
	ctr = random.randint(5,10)
	colors = [blue, yellow]
	# start by displaying colors
	for x in range(ctr):
		# generate random number between 0 and 1 (0 = BLUE, 1 = YELLOW)
		n = random.randint(0, 1)
		displayed.append(names[n])
		fill_background(colors[n])
		sleep(.75)
		fill_background(black)
		sleep(.5)
	led_red.off()
	led_green.on()
	#print(displayed)
		
	# when button is released call function
	button_blue.when_released = blue_released
	# when button is released call function
	button_yellow.when_released = yellow_released
	
	# create program loop
	running = True
	while len(displayed) > 0 and running:
		# event handling gets all events from queue
		for event in pygame.event.get():
			if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
				running = False
			# if "b" is released
			elif event.type == pygame.KEYUP and event.key == pygame.K_b:
				blue_released()
			# if "y" is released
			elif event.type == pygame.KEYUP and event.key == pygame.K_y:
				yellow_released()
		sleep(.2)
	destroy()

def blue_released():
	print("You guessed BLUE, the correct response is {0}.".format(displayed[0]))
	displayed.pop(0)
	sleep(.2)
	
def yellow_released():
	print("You guessed YELLOW, the correct response is {0}.".format(displayed[0]))
	displayed.pop(0)
	sleep(.2)

def destroy():
	print("cleanup")
	pygame.quit()

def fill_background(color):
	screen.fill(color)
	pygame.display.update()

try:
	# initialize pygame
	pygame.init()
	pygame.display.set_caption("Memory")
	screen = pygame.display.set_mode((400, 400))
	fill_background(black)
	main()
except KeyboardInterrupt: # end when ctrl-c is pressed
	destroy()
