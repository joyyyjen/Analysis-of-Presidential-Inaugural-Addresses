# Analysis of Presidential Inaugural Addresses

Homework 2 for LING 490 Special Topics

This program reads the txt file in the same directory and outputs corresponding analysis
It's a python program. (Idealy python3)

using toolkits and libraries collection, nltk, string
### 0. Required Downloads
In order to run the program, please have nltk download the following packages
> nltk.download('punkt')
> nltk.download('stopwords')
> nltk.download('averaged_perceptron_tagger')

### 1. How to run?
If you are using Mac, open Terminal
Run ./__init__.py

### 2. Double check the python path in your environment
mine is in /usr/local/bin/python3
After executed, if you received this error: "No such file or directory"
try changing the first line #!/usr/local/bin/python3 to #!/usr/bin/python3

### 3. How does it work?
-  There are two python3 files necessary, ana.py and __init__.py
- ana.py contains function such as toClearToken, TTR, sent_count, WordLength, freqWord and etc.
- ana.py also contain functions for Stylometry Indeces (STC,Ranking,Q,MATTR)


NOTE:
The analysis question and answers is in the Stat_Analysis2.html file. 
It's a jupyter notebook step by step coding and response. 
This include PART 1 ESL Corpus Response
