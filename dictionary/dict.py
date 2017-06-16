import urllib.request
import sys
import random
import codecs
import os
import json
import wordlist

if(len(sys.argv) == 1):
	word = wordlist.wordlist[random.randrange(0, len(wordlist.wordlist), 2)]
else:
	word = sys.argv[1];

reader = codecs.getreader('utf-8')

print(word)
url = "http://api.wordnik.com/v4/word.json/"+word.lower()+"/definitions?limit=3&includeRelated=true&useCanonical=false&includeTags=false&api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5"
count = 0;
related = []
found = True
try : 
	with urllib.request.urlopen(url) as resp:
		found = False
		jsonObj = json.load(reader(resp))
		for res in jsonObj:
			print("> " + res["text"])
			found = True
			for rel in res["relatedWords"]:
				related.append(rel)
		if not len(related) == 0 :
			print("Related words : " + str(related))
except Exception as e:
	print("Some error occured : " + str(e))

if not found:
	print("Not found.")

if found and not len(sys.argv) == 1:
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

print("--------------------------------------------------")	
