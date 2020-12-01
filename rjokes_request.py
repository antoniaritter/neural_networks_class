# Nov 16 2020 
# requests from r/jokes 

import requests 
import json

data = requests.get("https://www.reddit.com/r/jokes/.json", headers = {'User-agent': 'your bot 0.1'}) 
dataj = data.json()
#print(json.dumps(dataj, indent=4))

sub = dataj.get("data").get("children")
#print(len(sub)) # there are 27 jokes 

params = dataj.get("data").get("children")[0].get("data").keys()
for i in params: 
    print(i)
# joke tag variable = "link_flair_css_class" 

#with open('rjokes1.json', 'w') as outfile:
#    json.dump(dataj, outfile, indent=4) 