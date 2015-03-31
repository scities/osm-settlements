# -*- coding: utf-8 -*-
"""parser.py

Script to parse the planet.osm file (or any .osm file) to get a list of all cities, towns,
villages in the worlds and their coordinates.
"""
import xml.etree.cElementTree as et


__authors__ = """\n""".join(["Rémi Louf <remi.louf@scities>"])


path = "map.osm"

places = {}
parser = et.iterparse(path)
for action, elem in parser:
    if elem.tag=="way":
        elem.clear()
    if elem.tag=="relation":
        elem.clear()
    if elem.tag=="node":
        place = False 
        for child in elem: 
            if child.tag == 'tag' and child.attrib != {}:
                if child.attrib['k'] == 'name':
                    name = child.attrib['v']
                if child.attrib['k'] == 'place':
                    place = child.attrib['v']
        if place:
            if place not in places:
                places[place] = {}
            places[place][name] = {'lat':elem.attrib['lat'],
                                   'lon':elem.attrib['lon']}

print places
