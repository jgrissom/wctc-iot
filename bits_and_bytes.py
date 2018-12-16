#https://www.ascii-code.com
from gpiozero import Button, LED
from signal import pause

# set button and led pins
pins = (
{ "btn": 15, "led": 18 },
{ "btn": 17, "led": 27 },
{ "btn": 23, "led": 24 },
{ "btn": 10, "led": 9 },
{ "btn": 8, "led": 11 },
{ "btn": 6, "led": 12 },
{ "btn": 13, "led": 19 },
{ "btn": 20, "led": 21 }
)

# when a button is pressed
def toggle_led(btn):
	for i in range(len(pins)):
		if pins[i]["btn"] == btn.pin.number:
			# toggle led on/off
			leds[i].toggle()
			# set bit to 0/1
			bits[i] = 1 if leds[i].is_lit else 0
			break
	display_bits()

# display the collection of bits
def display_bits():
	s = ''.join(map(str, bits))
	print(s)
	#print(s + " " + str(int(s,2)) + " " + chr(int(s,2)))

buttons = []
leds = []
bits = []

# create arrays of buttons, leds, and bits
for i in range(len(pins)):
	buttons.append(Button(pins[i]["btn"]))
	leds.append(LED(pins[i]["led"]))
	bits.append(0)
	buttons[i].when_released = toggle_led
display_bits()

pause()
