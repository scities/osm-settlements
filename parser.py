# -*- coding: utf-8 -*-
"""parser.py

Script to parse the planet.osm file (or any .osm file) to get a list of all cities, towns,
villages in the worlds and their coordinates.
"""
import xml.etree.cElementTree as et
from gzip import GzipFile

__authors__ = """\n""".join(["Rémi Louf <remi.louf@scities>"])

## Feed a gzipped osm file
path = "map.osm.gz"

places = {}
with open(path, "r") as c_file, GzipFile(fileobj=c_file) as xml_file:
    parser = et.iterparse(xml_file)
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
