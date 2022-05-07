#!/usr/bin/python3

import requests

url = "http://173.230.134.127"

response = requests.get(url)
seq_url = response.url

seq_response = requests.get(seq_url)

message = []

while seq_response.text != '~':
	bit = seq_response.text
	message.append(bit)
	seq_response = requests.get(seq_url)

print("".join(message))
