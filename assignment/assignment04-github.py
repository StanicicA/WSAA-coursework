
import requests
import json
from config import config as cfg

#Getting repo info

filename = "wsaa-code.json"
url = "https://api.github.com/users/astanicic/repos"

response = requests.get(url)
print (response.status_code)
repoJSON = response.json()
#print (response.json())

with  open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4)





