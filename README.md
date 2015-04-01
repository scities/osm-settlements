# OSM Locations

Parse the OSM planet.osm to get a list of cities with their coordinates.

## State of affairs

Asia, Europe and US take too much space in memory at the moment. There must be
something I am doing wrong in terms of memory management...

1. Read ElementTree documentation (iterparse)
    http://www.ibm.com/developerworks/xml/library/x-hiperfparse/
    http://stackoverflow.com/questions/12160418/why-is-lxml-etree-iterparse-eating-up-all-my-memory
    http://effbot.org/zone/element-iterparse.htm#incremental-parsing
    https://github.com/eilisa2007/eilisa2007.github.com/blob/master/_posts/2012-07-04-parsing-xml-efficiently-with-python.md
2. Send to cluster
3. Use osmosis + GADM country polygons to serve individual countries to the
   parser.
