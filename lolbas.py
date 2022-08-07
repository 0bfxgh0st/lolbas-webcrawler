#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import sys
import os

def header():
	print ('\033[1;32m')
	print (r"""
.____    ________  .____   __________    _____    _________
|    |   \_____  \ |    |  \______   \  /  _  \  /   _____/
|    |    /   |   \|    |   |    |  _/ /  /_\  \ \_____  \ 
|    |___/    |    \    |___|    |   \/    |    \/        \
|_______ \_______  /_______ \______  /\____|__  /_______  /
        \/       \/        \/      \/         \/        \/ 

Living Off The Land Binaries, Scripts and Libraries
For more info on the project, click on the logo.

If you want to contribute, check out our contribution guide. Our criteria list sets out what we define as a LOLBin/Script/Lib.

MITRE ATT&CK® and ATT&CK® are registered trademarks of The MITRE Corporation. You can see the current ATT&CK® mapping of this project on the ATT&CK® Navigator.

If you are looking for UNIX binaries, please visit gtfobins.github.io.
	""")
	print ('\033[0m')

def _request_lolbas_frontend_db_and_UI_():

	url = 'https://lolbas-project.github.io/'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	programs = soup.find_all('a', class_='bin-name', href=True)

	dict = {}

	for i in programs:
		print ( "[\033[32m+\033[0m] " + i.text)

		dict.update({i.text: i['href']})

	select_program = input("\n[(\033[32mL0LBAS\033[0m)]> ")
	print ("")
	value = dict[select_program]
	url = 'https://lolbas-project.github.io' + value
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	for i in soup.find_all(['p','b','li','h2','code']):

		print(i.text + '\n')


if len(sys.argv) == 2:

	header()
	print ('argument function not ready yet sorry')
	#_argv_()

else:

	try:
		header()
		_request_lolbas_frontend_db_and_UI_()

	except KeyboardInterrupt:

		print ("\n\n[\033[31m-\033[0m] Killing lolbas.py\n")
		sys.exit(1)
