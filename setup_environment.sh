#!/bin/bash
## Install python-virtualenv and other project dependencies
sudo apt-get install python-virtualenv python-pip libgeos-3.3.3    libgeos-c1

## Create a directory for virtual environments if does not exist
mkdir -p ~/venvs/

## Create a virtual environment for this project
virtualenv --no-site-packages ~/venvs/instruments

## Activate virtualenv just created
source ~/venvs/instruments/bin/activate

## Install dependencies for this project
pip install -r requirements.txt

## Install gis dependencies
sudo apt-get install gdal-bin
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable
sudo apt-get update
#sudo apt-get install spatialite-bin
#sudo apt-get install libsqlite3-dev
 
#spatialite instruments.db "SELECT InitSpatialMetaData();"
sudo apt-get install python-software-properties
sudo apt-add-repository ppa:sharpie/for-science
sudo apt-add-repository ppa:sharpie/postgis-stable
sudo apt-add-repository ppa:ubuntugis/ubuntugis-unstable
sudo apt-get update
sudo apt-get install libpq-dev python-dev
sudo apt-get install postgresql-9.1-postgis2 
pip install git+git://github.com/django/django.git
