all: parse
.PHONY: all initialise parse clean


## Create the required folders
initialise: 
	mkdir -p raw
	mkdir -p extr

## Download latest planet.osm and MD5 checksum
raw/planet-latest.osm.gz2: initialise
	curl -o raw/planet-latest.osm.bz2 http://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/planet/planet-latest.osm.bz2
	curl -o raw/planet-latest.osm.bz2.md5 http://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/planet/planet-latest.osm.bz2.md5
	md5sum -c raw/planet-latest.osm.bz2.md5 raw/planet-latest.osm.bz2

## Parse for settlements
parse: raw/planet-latest.osm.gz2
	python parser.py


# 
# Back to a clean slate
#
clean:
	rm -r raw
	rm -r extr
