import quo
from random import randint

list_num = randint(0,4)
print(list_num)

'''
393
237
1000
1000
1000
print(len(quo.inspirational_quotes))
print(len(quo.motivational_quotes))
print(len(quo.education_quotes))
print(len(quo.success_quotes))
print(len(quo.attitude_quotes))
'''

if list_num == 0:
	quote_num = randint(0,131)
	print(quo.inspirational_quotes[quote_num])
elif list_num == 1:
	quote_num = randint(0,120)
	print(quo.motivational_quotes[quote_num])
elif list_num == 2:
	quote_num = randint(0,152)
	print(quo.education_quotes[quote_num])
elif list_num == 3:
	quote_num = randint(0,174)
	print(quo.success_quotes[quote_num])
else :
	quote_num = randint(0,79)
	print(quo.attitude_quotes[quote_num])

'''st = '''

''';

lis = st.split('"');
l = len(lis);
newl = []
for i in range(l):
	if i%2 : 
		newl.append(lis[i])
with open('quo.py','a+') as f:
	f.write(str(newl))

# quotes = []; list = $("a"); l = list.length; for(var i=0;i<l;i++){ if(/b-qt qt_.*oncl_q/.test(list[i].getAttribute("class"))) { quotes.push(list[i].innerText)}} console.log(quotes.length); console.log(quotes);

'''