# OSM Settlements

Parse the OSM planet.osm to get a list of settlements with their coordinates. We define settlements as the nodes tagged as a 'city', a 'town' or a 'village'. See the [OSM Wiki](http://wiki.openstreetmap.org/wiki/Key:place) for more information about the *place* tag. 

## Dependencies

* Python 2.7
* lxml

## Use

### Parse the planet.osm

Open your console, go to the directory where you cloned the repository and type

```
make 
```

This will download the current planet.osm file, parse it to find all nodes
marked as a city, a town or a village and their coordinates, and save as a csv
file.

Once the data extracted and **transfered to another folder** type 

```
make clean
``` 

to delete **all** data (goes back to the initial state).

### Parse other osm files

If for a reason or another you do not want to parse an extract of the planet.osm
(or if you already have the planet.osm on your computer), go to the directory where you cloned the repository and type

```
python parse.py /path/to/extract.osm.bz2
```

## How long does it take?

Testing, will let you know as soon as it is done parsing :) 

## License and author

Author: Rémi Louf <remi.louf@sciti.es>  
Website: www.sciti.es  
License: GPL v2
