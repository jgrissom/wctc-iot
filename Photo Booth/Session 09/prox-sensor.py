from gpiozero import InputDevice, OutputDevice, LED
import time
import statistics

trigger = OutputDevice(24)
echo = InputDevice(6)

#red_led = LED(20)
#green_led = LED(13)

#def green_light():
#	green_led.on()
#	red_led.off()

#def red_light():
#	red_led.on()
#	green_led.off()

def get_distance():
	# trigger emits a short burst of sound
	trigger.value = True
	time.sleep(0.0001)
	trigger.value = False

	# echo listens for echos from objects in front of it
	# the sound is created at a frequncy between 30kHz and 50KHz
	# well above detection range by the human ear
	while echo.value == False:
		start = time.time()
		
	while echo.value == True:
		end = time.time()

	sig_time = end - start

	# distance in cm
	distance = sig_time / 0.000058
	return distance

distances = []
# increase array size for more acurracy (slower response)
array_size = 6
#alarm_distance = 120
while True:
	distances.insert(0, get_distance())
	
	if len(distances) > array_size:
		distances.pop()
	med = statistics.median(distances)
	print("{:.2f}".format(med))
	#if len(distances) == array_size:
	#	if med < alarm_distance:
	#		red_light()
	#	else:
	#		green_light()
	time.sleep(.2)
