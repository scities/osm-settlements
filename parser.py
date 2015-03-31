# -*- coding: utf-8 -*-
"""parser.py

Script to parse the planet.osm file (or any .osm file) to get a list of all cities, towns,
villages in the worlds and their coordinates.
"""
import xml.etree.cElementTree as et
from gzip import GzipFile

__authors__ = """\n""".join(["Rémi Louf <remi.louf@scities>"])

## Feed a gzipped osm file
path = "data/brussels_belgium.osm.gz"

#
# Parse the OSM file
#
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
                        name = unicode(child.attrib['v'],
                                        'utf-8')
                    if child.attrib['k'] == 'place':
                        place = unicode(child.attrib['v'],
                                        'utf-8')
            if place:
                if place not in places:
                    places[place] = {}
                places[place][name] = {'lat':elem.attrib['lat'],
                                       'lon':elem.attrib['lon']} 


#
# Save the data
#
for place_type in places:
    with open("extr/%s.csv"%place_type, "w") as output:
        for name,coords in places[place_type].iteritems():
            output.write("%s\t%s\t%s\n"%(name,
                                        coords['lat'],
                                        coords['lon']))
