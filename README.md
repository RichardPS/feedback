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

### URLs (local env)

#### Create Support feedback

http://localhost:8000/create/support/

#### View First Support feedback

http://localhost:8000/admin/support/

#### View All Support feedback

http://localhost:8000/admin/all-support/

#### View JSON of Support data (start date / end date)

http://localhost:8000/json/support/YYYY-MM-DD/YYYY-MM-DD/

#### Create Launch feedback

http://localhost:8000/create/launch/

#### View First Launch feedback

http://localhost:8000/admin/launch/

#### View All Launch feedback

http://localhost:8000/admin/all-launch/

#### View JSON of Launch data (start date / end date)

http://localhost:8000/json/launch/YYYY-MM-DD/YYYY-MM-DD/


## Behaviour and Settings

* Creating a Support or Launch feedback will generate and display the URL for that feedback (This would be sent to the school)

* Completing a feedback with an 'Unsatifactory' will trigger an email to the relivant email (sored in config.py)
    * EMAIL_CONTACTS

* Wording for each question is set in config.py
    * SUPPORT_LABELS
    * LAUNCH_LABELS

* Intro text for feedback surveys is set in config.py
    * SUPPORT_INTRO_TEXT
    * LAUNCH_INTRO_TEXT

* Thankyou message once feedback has been submitted is set in config.py
    * FEEDBACK_THANKYOU_MESSAGE
