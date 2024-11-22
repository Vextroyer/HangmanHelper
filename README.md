Have you ever played the Hangman game? This script will help you win.

How to use the script?

	You need list of words, which is provided on index.json
	The current contents of index.json are a list of spanish words,
	but you can replace it with a list on your language.
	
	Suppose we want to predict wich word, or wich letters to
	say next, given that we know the following: __n_ia__a
	
	To do that we run:
		python predict.py __n_ia__a
	
	This will give us a list of words, which are possible
	candidates to match.
	And will also give us a list of letters with the proportion
	they represent on the candidates. Choose ideally the letters
	with the highest proportion.
	
	Good luck.
	
Legal notice about index.json:

	The index.json file used is copied from https://github.com/words/an-array-of-spanish-words
	
	(The MIT License)

	Copyright (c) 2016 Zeke Sikelianos <zeke@sikelianos.com>

	Permission is hereby granted, free of charge, to any person obtaining
	a copy of this software and associated documentation files (the
	'Software'), to deal in the Software without restriction, including
	without limitation the rights to use, copy, modify, merge, publish,
	distribute, sublicense, and/or sell copies of the Software, and to
	permit persons to whom the Software is furnished to do so, subject to
	the following conditions:

	The above copyright notice and this permission notice shall be
	included in all copies or substantial portions of the Software.
	
	