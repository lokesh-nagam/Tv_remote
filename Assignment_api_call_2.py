import requests

endpoint ="https://api.datamuse.com/words?rel_jjb=ocean" 

response = requests.get(endpoint)

data = response.json()

if response.status_code == 200 :
    for item in data:
        words = item.get("word")
        score = item.get("score")
        if score > 950:
            print(words) 
    
    