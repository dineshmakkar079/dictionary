import urllib.request
import sys
import random
import os
import io
import wordlist

word=""
if(len(sys.argv) == 1):
	word = wordlist.wordlist[random.randrange(500, len(wordlist.wordlist), 10)]	
else:
	word = sys.argv[1];

print(word);
url = "http://api.pearson.com/v2/dictionaries/entries?headword=" + word
import json
count = 0;
with urllib.request.urlopen(url) as resp:
	jsonObj = json.loads(resp.read().decode('utf-8'))
	resultArr = jsonObj["results"]
	for el in resultArr:
		try :
			for sense in el['senses']:
				defArr = sense['definition']
				if count < 3 :
					if len(defArr) == 1 :
						print('>  ' + defArr[0])
						count = count + 1
					else:
						print('>  ' + defArr)
						count = count + 1
		except:
			pass

if not count == 0:
	if not word in wordlist.wordlist:
		with open(os.path.dirname(os.path.realpath(__file__))+ os.sep + 'wordlist.py','r+') as wri : 
			wri.seek(0,2);
			wri.seek(wri.tell()-1,0);
			wri.write(',"' + word + '"]')
		print("* New word added to dictionary.")