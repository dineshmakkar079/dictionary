import urllib.request
import sys
import random
import os
import wordlist

if(len(sys.argv) == 1):
	word = wordlist.wordlist[random.randrange(0, len(wordlist.wordlist), 2)]	
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

if count == 0:
	print("Not found.")

if not count == 0 and not len(sys.argv) == 1:
	if word not in wordlist.wordlist:
		with open(os.path.dirname(os.path.realpath(__file__))+ os.sep + 'wordlist.py','r+') as wri : 
			wri.seek(0,2);
			pos = wri.tell();
			wri.seek(pos-1,0)
			last_char = wri.read(1)
			if last_char == '\n': # remove new line character in the end
				wri.seek(pos-2,0)
			else:
				wri.seek(pos-1,0)
			wri.write(',"' + word + '"]')
		print("* New word added to dictionary.")
