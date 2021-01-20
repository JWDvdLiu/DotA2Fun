import requests
import json

r = requests.get("https://api.opendota.com/api/players/125581247/matches")

print(r.text)