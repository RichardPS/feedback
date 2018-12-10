# Feedback System

Feedback system for support and launch surveys

## Install system requirments

sudo apt-get install git

sudo apt-get install python3-pip

sudo apt-get install virtualenv

## Create virtual environment

virtualenv -p python3 dev

## Get repo and setup env

source dev/bin/activate

cd dev

git clone https://github.com/RichardPS/feedback.git

## Install env requirements

cd feedback

pip install -r requirements.txt

## Add DB config

feedback/cuckoo/cuckoo/site_config.py

## Requirments

Django==1.11.

flake8==3.5.0

psycopg2-binary==2.7.6.1

pytest==4.0.0

pytest-django==3.4.4
