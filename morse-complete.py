from gpiozero import Button, OutputDevice
import time

morse = [ 
	{ "char": "A", "code": [ 0, 1 ] }, 
	{ "char": "B", "code": [ 1, 0, 0, 0 ] }, 
	{ "char": "C", "code": [ 1, 0, 1, 0 ] }, 
	{ "char": "D", "code": [ 1, 0, 0 ] }, 
	{ "char": "E", "code": [ 0 ] }, 
	{ "char": "F", "code": [ 0, 0, 1, 0 ] }, 
	{ "char": "G", "code": [ 1, 1, 0 ] }, 
	{ "char": "H", "code": [ 0, 0, 0, 0 ] }, 
	{ "char": "I", "code": [ 0, 0 ] }, 
	{ "char": "J", "code": [ 0, 1, 1, 1 ] }, 
	{ "char": "K", "code": [ 1, 0, 1 ] }, 
	{ "char": "L", "code": [ 0, 1, 0, 0 ] }, 
	{ "char": "M", "code": [ 1, 1 ] },
	{ "char": "N", "code": [ 1, 0 ] },
	{ "char": "O", "code": [ 1, 1, 1 ] }, 
	{ "char": "P", "code": [ 0, 1, 1, 0 ] }, 
	{ "char": "Q", "code": [ 1, 1, 0, 1 ] }, 
	{ "char": "R", "code": [ 0, 1, 0 ] }, 
	{ "char": "S", "code": [ 0, 0, 0 ] }, 
	{ "char": "T", "code": [ 1 ] }, 
	{ "char": "U", "code": [ 0, 0, 1 ] }, 
	{ "char": "V", "code": [ 0, 0, 0, 1 ] }, 
	{ "char": "W", "code": [ 0, 1, 1 ] }, 
	{ "char": "X", "code": [ 1, 0, 0, 1 ] }, 
	{ "char": "Y", "code": [ 1, 0, 1, 1 ] }, 
	{ "char": "Z", "code": [ 1, 1, 0, 0 ] },
	{ "char": "1", "code": [ 0, 1, 1, 1, 1 ] },
	{ "char": "2", "code": [ 0, 0, 1, 1, 1 ] },
	{ "char": "3", "code": [ 0, 0, 0, 1, 1 ] },
	{ "char": "4", "code": [ 0, 0, 0, 0, 1 ] },
	{ "char": "5", "code": [ 0, 0, 0, 0, 0 ] },
	{ "char": "6", "code": [ 1, 0, 0, 0, 0 ] },
	{ "char": "7", "code": [ 1, 1, 0, 0, 0 ] },
	{ "char": "8", "code": [ 1, 1, 1, 0, 0 ] },
	{ "char": "9", "code": [ 1, 1, 1, 1, 0 ] },
	{ "char": "0", "code": [ 1, 1, 1, 1, 1 ] }
]

def press():
	output.on()
	signal["start"] = time.time()

def release():
	output.off()
	signal["end"] = time.time()
	signals.append(1 if signal["end"] - signal["start"] > .33 else 0)
	
def decode():
	del signal["end"]
	
	for m in morse:
		if signals == m["code"]:
			print(m["char"])
	signals.clear()

button = Button(24)
output = OutputDevice(25)

signal = {}
signals = []

button.when_pressed = press
button.when_released = release

while (True):
	if "end" in signal and button.is_pressed == False:
		if time.time() - signal["end"] > 1:
			decode()
	time.sleep(.1)
