all: parse
.PHONY: all initialise parse clean

# Change the following line if you want the planet.osm
# to be downloaded in another folder
DATADIR = $(shell pwd)/raw



#
# Where the action happens
#

## Create the required folders
initialise: 
	mkdir -p $(DATADIR)
	mkdir -p extr

## Download latest planet.osm and MD5 checksum
raw/planet-latest.osm.gz2: initialise
	curl -o $(DATADIR)/planet-latest.osm.bz2 http://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/planet/planet-latest.osm.bz2
	curl -o $(DATADIR)/planet-latest.osm.bz2.md5 http://ftp5.gwdg.de/pub/misc/openstreetmap/planet.openstreetmap.org/planet/planet-latest.osm.bz2.md5
	md5sum -c $(DATADIR)/planet-latest.osm.bz2.md5 $(DATADIR)/planet-latest.osm.bz2

## Parse for settlements
parse: $(DATADIR)/planet-latest.osm.gz2
	python parser.py $(DATADIR)




# 
# Back to a clean slate
#
clean:
	rm -r $(DATADIR)
	rm -r extr 
