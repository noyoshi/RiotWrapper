#!/usr/bin/env python2.7

# -*- coding: utf-8 -*-

import GET_TOKEN as _token
import requests
import classes

API_KEY = _token.GET_KEY()

headers = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": API_KEY,
    "Accept-Language": "en-US,en;q=0.8",
    "tags": "spells"
}
#WARNING: THIS REQUEST IS LIMITED TO 10/HR WITH THE DEV KEY
region = "na1"
ext = "lol/static-data/v3/champions?locale=en_US&tags=spells&dataById=false"
url = "https://{region}.api.riotgames.com/{ext}".format(region=region, ext=ext)
data = requests.get(url, headers=headers)
json_data = data.json()["data"]
champ_names = []
for champ in json_data:
    if champ == "MonkeyKind": # Why is he still called this smh
        champ = "Wukong"
    champ_names.append(champ.encode("utf-8"))
champ_names.sort() # Sort champ names alphabetically

database = {}

for name in champ_names:
    print json_data[name]["id"]
    database[name] = classes.champion(name, json_data[name]["id"],
            json_data[name]["spells"])
            # spells is a list of spells, not including passive
            # id is thier champ id numberfor t
for thing in database:
    print thing
