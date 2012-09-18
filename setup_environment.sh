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
