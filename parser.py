#-*- coding: utf-8 -*-
"""parser.py

Script to parse the planet.osm file (or any .osm file) to get a list of all cities, towns,
villages in the worlds and their coordinates.
"""
import sys
import os

try:
    from lxml import etree as et
except ImportError:
   raise ImportError("The lxml python module needs to be installed to run"
                     "the parser ('sudo pip install lxml').")

try:
    from bz2file import BZ2File
except ImportError:
    raise ImportError("The bz2file python module needs to be installed to run"
                      "the parser ('sudo pip install bz2file').")




__authors__ = """\n""".join(["Rémi Louf <remi.louf@scities>"])
__copyright__ = "2015, Scities"
__license__ = "GPL v2"



#
# Sanity checks
#

## Check if path to .osm file has been passed as an argument
if not len(sys.argv) > 1:
    raise IOError("Please pass the path to the OSM data as an argument")
else:
    data_path = sys.argv[1] 
    if not os.path.isfile(data_path):
        raise IOError("OSM data cannot be found at the indicated path.")

## Check destination folder, create it if needed 
if not len(sys.argv) > 2:
    extr_path = "extr"
else:
    extr_path = sys.argv[2]

if not os.path.isdir(extr_path):
    os.path.mkdir(extr_path)




#
# Parameters
#
types = ['city', 'town', 'village']




#
# Parse the OSM file
#
places = {}
with BZ2File(data_path) as xml_file:
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




#
# Save the data
#
for place_type in places:
    with open(str(extr_path)+"/%s.csv"%place_type, "w") as output:
        for name,coords in places[place_type].iteritems():
            output.write("%s\t%s\t%s\n"%(name.encode('utf8'),
                                        coords['lat'],
                                        coords['lon']))
