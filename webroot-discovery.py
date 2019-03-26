import glob
import sys
import re
from termcolor import colored
import urllib.request
import requests

regexlist = []
urlList = []

if len(sys.argv) >= 3:
	wwwrootpath = sys.argv[1]
	siteurl = sys.argv[2]
	filetype = "*." + sys.argv[3]

else:
	print('Missing argument variables. wwwroot siteurl filetype(e.g. jsp, aspx, php)')
	exit()

filepaths = glob.iglob((wwwrootpath +"/**/"+ filetype), recursive=True)

for filename in filepaths:
	print (siteurl + (filename.replace(sys.argv[1], "")))

yesorno = input('Send to proxy? y/n')
#filepath above becomes empty for some reason
filepaths2 = glob.iglob((wwwrootpath +"/**/"+ filetype), recursive=True)

print(yesorno)
if yesorno == 'y':
	for filename in filepaths2:
		print(filename)
		proxies = {
			  "http": "http://127.0.0.1:8080",
			  "https": "http://127.0.0.1:8080",
			}

		requests.get((siteurl + (filename.replace(sys.argv[1], ""))), proxies=proxies)
