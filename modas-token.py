import requests
import jwt
import datetime
import json
import random
import datetime
from gpiozero import MotionSensor, LED, Button
from time import sleep

class Modas:
	def __init__(self):
		# TODO: init PiCamera

		# TODO: set camera resolution

		# init green, red LEDs
		self.green = LED(24)
		self.red = LED(23)
		# init button
		self.button = Button(8)
		# init PIR
		self.pir = MotionSensor(25)
		
		# when button  is released, toggle system arm / disarm
		self.button.when_released = self.toggle
		
		# system is disarmed by default
		self.armed = False
		self.disarm_system()
		
	def init_alert(self):
		self.green.off()
		self.red.blink(on_time=.25, off_time=.25, n=None, background=True)
		print("motion detected")
		# TODO: Take photo
		
		# get current date / time
		t = datetime.datetime.now()
		# format date for log file name
		t_log = "{0}-{1}-{2}.log".format(t.strftime("%Y"), t.strftime("%m"), t.strftime("%d"))
		# format date in json format for RESTful API
		t_json = "{0}-{1}-{2}T{3}:{4}:{5}".format(t.strftime("%Y"), t.strftime("%m"), t.strftime("%d"), t.strftime("%H"), t.strftime("%M"), t.strftime("%S"))
	
		# generate random location
		loc_id = random.randint(1, 3)
		
		# first check for token
		token = self.Token()
		if token != None:
			# post event to web api
			url = 'https://modas-fall-19-jsg.azurewebsites.net/api/event/'
			headers = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token }
			payload = { 'timestamp': t_json, 'flagged': False, 'locationId': loc_id }
			# post the event
			r = requests.post(url, headers=headers, data=json.dumps(payload))
			print(r.status_code)
			print(r.json())
		
			# log alert to file
			f = open(t_log, "a")
			f.write("{0},False,{1},{2}\n".format(t_json, loc_id, r.status_code))		
			f.close()
		
		# delay
		sleep(2)
		
	def Token(self):
		try:
			# attempt to open the file token.json for reading
			f = open("token.json", "r")
			# assuming the file can be opened, read the file into a variable
			# convert the string into json
			encoded_token = json.loads(f.read())
			f.close()
			# using jwt package decode the token
			# all we are looking for is the token expiration (exp)
			unencoded_token = jwt.decode(encoded_token["token"], verify = False)

			# save the exp date (remember it is in Unix timestamp format)
			exp_epoch = int(unencoded_token["exp"])

			# get current date/time
			today = datetime.datetime.now()
			# convert current date/time to UNIX timestamp (Epoch)
			current_epoch = int(today.timestamp())

			# subtract the current date/time from the exp date/time
			# if the difference is positive the token is not yet expired
			diff = exp_epoch - current_epoch
			if diff > 0:
				return encoded_token["token"]
			else:
				print("Token is expired")
				return None
		except:
			print("An error occurred")
			return None
			
	def reset(self):
		self.red.off()
		self.green.on()
		
	def toggle(self):
		self.armed = not self.armed
		if self.armed:
			self.arm_system()
		else:
			self.disarm_system()
			
	def arm_system(self):
		print("System armed in 3 seconds")
		self.red.off()
		# TODO: enable camera

		# 3 second delay
		self.green.blink(on_time=.25, off_time=.25, n=6, background=False)
		# enable PIR
		self.pir.when_motion = self.init_alert
		self.pir.when_no_motion = self.reset
		self.green.on()
		print("System armed")
		
	def disarm_system(self):
		# disable PIR
		self.pir.when_motion = None
		self.pir.when_no_motion = None
		# TODO: disable camera

		self.red.on()
		self.green.off()
		print("System disarmed")
		

m = Modas()

try:
	# program loop
    while True:
        sleep(.001)
# detect Ctlr+C
except KeyboardInterrupt:
	if m.armed:
		m.disarm_system()
