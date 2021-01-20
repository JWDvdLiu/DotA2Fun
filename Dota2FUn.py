import json
import time
import requests


# hero_name_file = open('G:\DAVID\DotA2Fun\heroes.json')
# heroNames = json.load(hero_name_file)
# hero_name_file.close

# for hero in heroNames:
#    print(hero['localized_name'])

r = requests.get("https://api.opendota.com/api/matches/5314309908")


