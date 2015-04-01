#-*- coding: utf-8 -*-
"""parser.py

Script to parse the planet.osm file (or any .osm file) to get a list of all cities, towns,
villages in the worlds and their coordinates.

If you want to understand how lxml's iterparse works, check Liza Daly's post at http://www.ibm.com/developerworks/xml/library/x-hiperfparse/
"""
import sys
from lxml import etree as et
from bz2 import BZ2File


__authors__ = """\n""".join(["Rémi Louf <remi.louf@scities>"])
__copyright__ = "2015, Scities"
__license__ = "GPL v2"



#
# Parameters
#
datapath = sys.arv[1] # Path to planet.osm passed as argument
path = str(datapath) + "/planet-latest.osm.bz2"
types = ['city', 'town', 'village']



#
# Parse the OSM file
#
places = {}
with BZ2File(path) as xml_file:
    parser = et.iterparse(xml_file, events=('end',))
    for events, elem in parser:

        if elem.tag == "tag":
            continue
        if elem.tag == "node":
            place = False 
            lat = elem.attrib['lat']
            lon = elem.attrib['lon']

            ## Check the nodes' attributes
            for child in elem.iterchildren(): 
                if child.tag == 'tag' and child.attrib != {}:
                    if child.attrib['k'] == 'name':
                        name = unicode(child.attrib['v'])
                    if child.attrib['k'] == 'place':
                        place = unicode(child.attrib['v'])
            if place in types:
                if place not in places:
                    places[place] = {}
                places[place][name] = {'lat':lat,
                                       'lon':lon} 
                

        ## Do some cleaning
        # Get rid of that element
        elem.clear()

        # Also eliminate now-empty references from the root node to node        
        while elem.getprevious() is not None:
            del elem.getparent()[0]

        # Garbage collect
        # gc.collect()



#
# Save the data
#
for place_type in places:
    with open("extr/%s.csv"%place_type, "w") as output:
        for name,coords in places[place_type].iteritems():
            output.write("%s\t%s\t%s\n"%(name.encode('utf8'),
                                        coords['lat'],
                                        coords['lon']))
