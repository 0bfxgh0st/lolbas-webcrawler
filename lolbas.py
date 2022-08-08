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

def _lolbas_and_UI_():

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

		print(i.text.replace('Execute','\033[1;32m[Execute]\033[0m').replace('AWL bypass','\033[1;32m[AWL bypass]\033[0m').replace('Copy','\033[1;32m[Copy]\033[0m').replace('Alternate data streams','\033[1;32m[Alternate data streams]\033[0m').replace('Encode','\033[1;32m[Encode]\033[0m').replace('Decode','\033[1;32m[Decode]\033[0m').replace('Credentials','\033[1;32m[Credentials]\033[0m').replace('Upload','\033[1;32m[Upload]\033[0m').replace('Compile','\033[1;32m[Compile]\033[0m').replace('Dump','\033[1;32m[Dump]\033[0m').replace('UAC bypass','\033[1;32m[UAC bypass]\033[0m').replace('Reconnaissance','\033[1;32m[Reconnaissance]\033[0m').replace('Paths:','\033[1;33mPaths:\033[0m').replace('Resources:','\033[1;33mResources:\033[0m').replace('Acknowledgements:','\033[1;33mAcknowledgements:\033[0m').replace('Detection:','\033[1;33mDetection:\033[0m') + '\n')
# Download cant be replaced

def _lolbas_and_argv_():

	url = 'https://lolbas-project.github.io/'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	programs = soup.find_all('a', class_='bin-name', href=True)

	dict = {}

	for i in programs:

		dict.update({i.text: i['href']})

	value = dict[sys.argv[1]]
	url = 'https://lolbas-project.github.io' + value
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')

	for i in soup.find_all(['p','b','li','h2','code']):

		print(i.text.replace('Execute','\033[1;32m[Execute]\033[0m').replace('AWL bypass','\033[1;32m[AWL bypass]\033[0m').replace('Copy','\033[1;32m[Copy]\033[0m').replace('Alternate data streams','\033[1;32m[Alternate data streams]\033[0m').replace('Encode','\033[1;32m[Encode]\033[0m').replace('Decode','\033[1;32m[Decode]\033[0m').replace('Credentials','\033[1;32m[Credentials]\033[0m').replace('Upload','\033[1;32m[Upload]\033[0m').replace('Compile','\033[1;32m[Compile]\033[0m').replace('Dump','\033[1;32m[Dump]\033[0m').replace('UAC bypass','\033[1;32m[UAC bypass]\033[0m').replace('Reconnaissance','\033[1;32m[Reconnaissance]\033[0m').replace('Paths:','\033[1;33mPaths:\033[0m').replace('Resources:','\033[1;33mResources:\033[0m').replace('Acknowledgements:','\033[1;33mAcknowledgements:\033[0m').replace('Detection:','\033[1;33mDetection:\033[0m') + '\n')
# Download cant be replaced

if len(sys.argv) == 2:

	header()
	_lolbas_and_argv_()

else:

	try:
		header()
		_lolbas_and_UI_()

	except KeyboardInterrupt:

		print ("\n\n[\033[31m-\033[0m] Killing lolbas.py\n")
		sys.exit(1)
