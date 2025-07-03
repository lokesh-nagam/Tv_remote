import requests

endpoint = "https://api.datamuse.com/words?ml=i%20am%20student"

response = requests.get(endpoint)

data = response.json()

if response.status_code == 200:
    for item in data:
        getting_tags = item.get("tags")
        first_one = getting_tags[0]
        print(first_one)

