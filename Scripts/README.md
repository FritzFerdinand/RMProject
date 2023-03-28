# Notes on script usage
 There are 2 ways to run the script: you could simply run all-in-one.sh, which reads all tweets directly
 from the Karora database. This is less work, but will take a long time every time you run it.
 Alternatively, you could first run tweet-generation-txt.sh. This writes each week of tweets
 to its own txt file. You can then run emoji.py in the same folder as the tweets. If you want there are 
 also scripts provided to only scan a single week directly, or print all tweets from one week to txt.
 Appropriate python scripts are provided as well to scan those tweets.

 For example, you could simply run sh all-in-one.sh s1234567 to automatically scan all 4 weeks directly
 from Karora. You could also run sh tweet-generation-txt.sh s1234567 and then emoji-all.py to first
 create 4 txt files (1 for each week) and then scan all those files using the python script. You could run
 txt-Mar20.sh to print all tweets from 23 to 30 March 2020 to a txt file. You can then use emoji-singular.py
 to scan that file (the python script takes the txt file as an argument, so for example python3 emoji-singular
 .py 23-30Mar2020.txt). emoji2.py is what the automatic scanner uses, so there is no need to run that. You
 will have to download it.

 !!NOTE: You will have to provide your P/S number as an argument to the script file in order to access 
 Karora. It will then ask for your password and authenticator 4 times: once for each week. If it takes
 a long time, don't be alarmed as there are quite a few tweets in the database.!!