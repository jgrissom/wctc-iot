import requests
import json
import jwt
import datetime

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

	# display exp date/time
	print("Token expires (epoch): {0}".format(exp_epoch))
	# display current date/time
	print("Today (epoch): {0}".format(current_epoch))
	# subtract the current date/time from the exp date/time
	# if the difference is positive the token is not yet expired
	diff = exp_epoch - current_epoch
	if diff > 0:
		# days = seconds / (sec/min) / (min/hr) / (hr/day)
		days = diff / 60 / 60 / 24
		#print("Token is valid for: {0} days".format(int(days)))
		# TODO: have students write this the following
		# hours = ???
		hours = (days - int(days)) * 24
		# minutes = ???
		minutes = (hours - int(hours)) * 60
		# seconds = ???
		seconds = (minutes - int(minutes)) * 60
		print("Token is valid for: {0} days, {1} hours, {2} minutes, {3} seconds.".format(int(days), int(hours), int(minutes), int(seconds)))
	else:
		print("Token is expired")

except:
	print("An error occurred")
