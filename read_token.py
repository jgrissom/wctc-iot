import requests
import json
import jwt

try:
	# attempt to open the file token.json for reading
	f = open("token.json", "r")
	# assuming the file can be opened, read the file into a variable
	o = json.loads(f.read())
	f.close()
	# display the token
	print(o["token"])
	# unencode the token (use verify false since we are not verifying issuer / audience)
	unencoded_token = jwt.decode(o["token"], verify = False)
	# display the payload
	print(unencoded_token)
	
except:
	# an error occurred, probably the file is missing
	print("An error occurred")
