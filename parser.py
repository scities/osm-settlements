#-*- coding: utf-8 -*-
"""parser.py

Script to parse the planet.osm file (or any .osm file) to get a list of all cities, towns,
villages in the worlds and their coordinates.
"""
import xml.etree.cElementTree as et
from gzip import GzipFile
from bz2 import BZ2File

__authors__ = """\n""".join(["Rémi Louf <remi.louf@scities>"])



## Feed a gzipped osm file
path = "data/africa-latest.osm.bz2"
types = ['city', 'town', 'village']



#
# Parse the OSM file
#
places = {}
with BZ2File(path) as xml_file:
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
                        name = unicode(child.attrib['v'])
                    if child.attrib['k'] == 'place':
                        place = unicode(child.attrib['v'])
            # If place type corresponds to desired ones, save
            if place in types:
                if place not in places:
                    places[place] = {}
                places[place][name] = {'lat':elem.attrib['lat'],
                                       'lon':elem.attrib['lon']} 
        if action=='end' and elem.tag=='node':
            elem.clear()

#
# Save the data
#
for place_type in places:
    with open("extr/%s.csv"%place_type, "w") as output:
        for name,coords in places[place_type].iteritems():
            output.write("%s\t%s\t%s\n"%(name.encode('utf8'),
                                        coords['lat'],
                                        coords['lon']))
