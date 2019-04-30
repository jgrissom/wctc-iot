import requests
import json
import getpass

valid_token = False
# loop until there is a valid token
while not valid_token:
	# input username / password (getpass hides the input)
	username = input("Username: ")
	password = getpass.getpass("Password: ")

	# url for your API
	url = 'https://modas.azurewebsites.net/api/token/'
	# request header will format data as json
	headers = { 'Content-Type': 'application/json'}
	# the request payload is the username and password
	payload = { 'username': username, 'password': password}
	#print(json.dumps(payload))
	# http post request 
	r = requests.post(url, headers=headers, data=json.dumps(payload))

	# http status code
	print(r.status_code)
	#print(r.text)

	# asssuming status code is 200, we should have a token
	if r.status_code == 200:
		f = open("token.json", "w")
		f.write(r.text)
		f.close()
		print("token created")
		valid_token = True
	elif r.status_code == 401:
		# 401 - Unautorized
		print("login failed, bad credentials")
	else:
		# login failed, but not due to bad credentials
		print("login failed, ")
