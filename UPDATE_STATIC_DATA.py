#!/usr/bin/env python2.7

# -*- coding: utf-8 -*-

# This will update the static database, with the most recent codes for
# champions, items, masteries, runes, etc

import GET_TOKEN as _token
import requests

API_KEY = _token.GET_KEY()

headers = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": API_KEY,
    "Accept-Language": "en-US,en;q=0.8",
    "tags": "spells"
    # "dataById" : "false"
}
#WARNING: THIS REQUEST IS LIMITED TO 10/HR WITH THE DEV KEY
region = "na1"
ext = "lol/static-data/v3/champions?locale=en_US&tags=spells&dataById=false"
url = "https://{region}.api.riotgames.com/{ext}".format(region=region, ext=ext)
data = requests.get(url, headers=headers)
json_data = data.json()
champ_names = []
for champion in json_data:
    if champion == "MonkeyKind": # Why is he still called this smh
        champion = "Wukong"
    champ_names.append(champion)
champ_namess.sort() # Sort champ names alphabetically



print data.json()

#IMPORTANT: data.json() is a dictionary with keys mapping to the names of the champions

# spell_dict = data.json()
# katarina = spell_dict["Katarina"]
# in katarina:
# spells, title, id, key, name
# spells, title, name return a unicode string
# .encode("utf-8") fixes this ^

# test_url = "https://na1.api.riotgames.com/lol/static-data/v3/champions/44?locale=en_US&tags=spells"
# test_data = requests.get(test_url)
# print test_data
# region = "na1"
# ext = "lol/static-data/v3/champions/44?locale=en_US&tags=spells"
# url = "https://{region}.api.riotgames.com/{ext}".format(region=region, ext=ext)
# data = requests.get(url, headers=headers)
# print data.json()

# THis shit up here works... dont fuck with the headers
