#!/usr/bin/env python2.7

# -*- coding: utf-8 -*-

import requests

class champion(object): # To store one champion
    def __init__(self, name=None, _id=None, spells=None, stats=None):
        self.name = name
        self.id = _id
        self.spells = spells # Dictionary
        self.stats = stats # Dictionary

    def get_name(self):
        return name

    def get_id(self):
        return _id

    def get_spells(self):
        return spells

    def get_stats(self):
        return stats

class spell(object): # To store spells
    def __init__(self, key, name, cooldown, sanitized_tooltip,):
        self.key = key.encode("utf-8")
        self.name = name.encode("utf-8")
        self.cooldown = cooldown # list
        self.sanitized_tooltip = sanitized_tooltip.encode("utf-8")


class item(object): # To store one item
    def __init__(self):
        pass

class mastery(object): # To store one mastery
    pass

class rune(object): # To store one rune
    pass

class player(object): # Player class derp de derp
    pass
