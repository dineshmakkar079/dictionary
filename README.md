<h1>About</h1>
This is a simple python script along with a local dictionary consisting of approx. 1500 words specifically for GRE like exams 
This can help you build your vocabulary with words which are not so common.

<h1>Suggestion</h1>
For linux users : <br>
1. Make a command alias to python3 /path/to/dict.py such as 'alias dict="python3 /path/to/dict.py" ' <br>
2. Add this command to ~/.bashrc file in the end (so that every time a terminal is launched this script gets executed). <br>
&nbsp &nbspFor example if aliased command is 'dict' , just write 'dict'(without single quotes) in last line of ~/.bashrc file.

<h1>Usage</h1>
If you inserted alias in ~/.bashrc file then it will automatically gets executes on launching terminal. 
<ul>
<li>
<h3>If you made command alias (assuming 'dict' is the alias) </h3>
Use it as : <br> Just type this on terminal 
<pre>
1. dict  -  fetches some random word from local dictionary and shows its meaning
2. dict some_word  -  fetches word's meaning and adds to local dictionary if it's not there already. (Thus keeps building dictionary on encounter with new word.)
</pre>
</li>
<li>
<h3>If you didn't make command alias</h3>
<pre>
Same as the above but just replace 'dict' by 'python3 /path/to/dict.py'
</pre>
</li>
</ul>

<h2>Demo</h2>
This is what it looks like
<img src="https://raw.githubusercontent.com/dineshmakkar079/dictionary/master/sample.png">

<strong>Note : </strong> For better resutls avoid editing wordlist.py file
<br><br>
Star the repo if it helped you.

<h1>Author</h1>
<h3>Dinesh Makkar</h3>
Pre-final year Undergrad<br>
IIT Guwahati.
