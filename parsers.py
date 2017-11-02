#!/usr/bin/env python2.7

# -*- coding: utf-8 -*-

def passive(_list):
    name = _list["name"]
    name = name.encode("utf-8")
    description = _list["sanitizedDescription"]
    description = description.encode("utf-8")
    return {"name": name, "description": description}

def spells(spell_list):
    
