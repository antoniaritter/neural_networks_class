# Nov 17 2020
# exploring a dataset from WBeddow (rjokes2 (small) or 3 (big).json)

import requests 
import json
from collections import defaultdict
import re 

jokecats = defaultdict(list) # tag : [joke, joke, ...]
tags = ["Long", "Walks into a bar", "Religion", "Blonde", "Politics", "Knock-Knock Joke", "Dirty"]
#tags = ["Blonde"] 
jokecount = defaultdict(int) 

with open('rjokes3.json', 'r') as file:   # in standard data format 
    jokedic = defaultdict(int)
    total = 0
    for line in file: 
        total += 1
        dic = json.loads(line) 
        tag = dic.get("link_flair_text") 
        title = dic.get("title") 
        joke = dic.get("selftext")
        if (re.search("\[deleted\]|\[removed\]", joke)==None) and (tag in tags):
            jokecats[tag].append(title + " " + joke) 
            jokecount[tag] = jokecount[tag]+1 

print("Total =", total)
for key in jokecount.keys():
    print(key, jokecount[key])

for tag in tags: 
    jokefile = open("Reddit_" + tag + ".txt", "w") 
    jokefileshort = open("Reddit_" + tag + "_short.txt", "w")
    jokefiletest = open("Reddit_" + tag + "_test.txt", "w")
    i = 0
    for joke in jokecats[tag]: 
        joke = re.sub("\n", " ", joke)
        jokefile.write(joke + "\n")
        if i<200:
            jokefileshort.write(joke + "\n")
            i+=1
        elif 199<i<300:
            jokefiletest.write(joke + "\n")
            i+=1

    jokefile.close()
    jokefileshort.close()
    jokefiletest.close()
    

