# Markov Chatbot

This is a newer implementation of a chatbot built using **markov chains**. 

## Usage 

#### 1. Running main.py

You can directly use this chatbot by running main.py file using the provided dictionary (text.txt). 

#### 2. Importing this into your own programs

You can alternatively import the class markovBot into your own programs by using "from main import markovBot". 
Then, make an object of the class, e.g "bot = markovBot". After that,
load the dictionary using bot.loadtext("text.txt"). Finally, run the bot by using 
"bot.run("text.txt"). 

Sample code for a full implementation:

`from main import markovBot`

`bot = markovBot()`

`bot.loadtext("text.txt")`

`bot.run("text.txt")

## Making or modifying the dictionary

The dictionary is presently stored within text.txt, and it is based on reddit posts and comments, 
which are scraped by reddit_scraper.py. To see how the data is stored, please check out reddit_scraper.py.