import urllib.request
import sys
import random
import wordlist
if(len(sys.argv) == 1):
	word = wordlist.wordlist[random.randrange(500, 9995,100)]	
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
				if(len(defArr) == 1):
					for defi in sense['definition']:
						count = count + 1
						print('>  ' + defi)
				else:
					count =  count + 1
					print('>  ' + defi)
		except:
			pass
