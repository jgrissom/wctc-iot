# utilize gpio zero framework to interface gpio
# https://gpiozero.readthedocs.io
from gpiozero import LED, Button
# utilize signal framework
from signal import pause
from random import randint
from time import sleep

# connect GPIO pin 4 to "yellow" button
button_yellow = Button(4)
# connect GPIO pin 25 to "blue" button
button_blue = Button(25)

# generate random number between 5 and 10
ctr = randint(5, 10)
my_list = []
color_names = ["YELLOW", "BLUE"]

for x in range(ctr):
	n = randint(0, 1)
	my_list.append(color_names[n])
	print(color_names[n])
	sleep(.5)
print("--------------------")

def yellow_released():
	print("YELLOW guessed, {} displayed".format(my_list[0]))
	my_list.pop()
	sleep(.2)
	if len(my_list) == 0:
		end()
def blue_released():
	print("BLUE guessed, {} displayed".format(my_list[0]))
	my_list.pop()
	sleep(.2)
	if len(my_list) == 0:
		end()
		
def end():
	button_yellow.when_released = None
	button_blue.when_released = None
	print("done")

# when button is released call function
button_yellow.when_released = yellow_released
# when button is released call function
button_blue.when_released = blue_released

# prevent program from ending immediately
pause()
