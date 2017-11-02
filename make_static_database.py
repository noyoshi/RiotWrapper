#!/usr/bin/env python2.7

# -*- coding: utf-8 -*-

import GET_TOKEN as _token
import requests
import classes
import parsers

API_KEY = _token.GET_KEY()

headers = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": API_KEY,
    "Accept-Language": "en-US,en;q=0.8",
    "tags": "all"
}
#WARNING: THIS REQUEST IS LIMITED TO 10/HR WITH THE DEV KEY
region = "na1"
ext = "lol/static-data/v3/champions?locale=en_US&tags=all&dataById=false"
url = "https://{region}.api.riotgames.com/{ext}".format(region=region, ext=ext)
data = requests.get(url, headers=headers)
json_data = data.json()["data"]
champ_names = []
for champ in json_data:
    if champ.encode("utf-8") == "MonkeyKind": # Why is he still called this smh
        champ = "Wukong"
    champ_names.append(champ.encode("utf-8"))
# champ_names.sort() # Sort champ names alphabetically

database = {}

for name in champ_names:
    # Initializes the database, each key maps to a champion name,
    # Each value maps to a champion object
    champ_pass = json_data[name]["passive"]
    champ_pass = parsers.passive(champ_pass)
    database[name] = classes.champion(name, json_data[name]["id"],
            json_data[name]["spells"], champ_pass,
             json_data[name]["stats"])
            # spells is a list of spells, not including passive
            # id is thier champ id number
for thing in database:
    thing = database[thing]
    print thing
    print thing.get_id()
    print thing.get_passive()
    for x in thing.get_passive():
        print x
        print type(x)

# DATABASE WORK... NOW TO ADD INFO

for champ in database:
    temp_champ = database[champ]
    champ_id = temp_champ.get_id()
