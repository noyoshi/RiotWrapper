#!/usr/bin/env python2.7

# -*- coding: utf-8 -*-

import requests

class model(object):

    '''
    Everything from the riot games API has a unique ID field and a type
    This type specifies which kind of object it is, ie spell, item, champion,
    player, etc
    '''

    def __init__(self, _type=None, _id=None):
        self.type = _type
        self.id = _id

    def set_type(self, t):
        self.type = t

    def set_id(self, _id):
        self.id = _id

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

# ------------ Inherited from model -------------------

class champion(model): # To store one champion
    def __init__(self, name=None, _id=None, spells=None, passive = None, stats=None):
        self.name = name
        self.spells = spells
        self.passive = passive
        self.stats = stats # Dictionary

    def get_name(self):
        return self.name

    def get_spells(self):
        return self.spells

    def get_passive(self):
        return self.passive

    def get_stats(self):
        return self.stats

    def set_name(self, name):
        self.name = name # string

    def set_spells(self, spells):
        self.spells = spells # dictionary

    def set_passive(self, passive):
        self.passive = passive

    def set_stats(self, stats):
        self.stats = stats # dictionary

    def __str__(self):
        return self.name + " " + str(self.id)

class spell(model): # To store spells
    def __init__(self, key, name, cooldown, sanitized_tooltip,):
        self.key = key.encode("utf-8")
        self.name = name.encode("utf-8")
        self.cooldown = cooldown # list
        self.tooltip = sanitized_tooltip.encode("utf-8")

    def set_key(self,key):
        self.key = key.encode("utf-8")

    def set_name(self, name):
        self.name = name.encode("utf-8")

    def set_cooldown(self, cd):
        self.cooldown = cd.encode("utf-8")

    def set_tooltip(self, tt):
        self.tootip = tt.encode("utf-8")

    def get_key(self):
        return self.key

    def get_name(self):
        return self.name

    def get_cooldown(self):
        return self.cooldown

    def get_tooltip(self):
        return self.tooltip

class item(model): # To store one item
    def __init__(self):
        pass

class mastery(model): # To store one mastery
    pass

class rune(model): # To store one rune
    pass

class player(model): # Player class derp de derp
    pass
