# Dev Tools

Dev tools for inital setup for testing purposes

## Inital Setup

Run the following command to setup a superuser and add mock data

```python devtools/run.py startup```

## Test URLS for mock data

### Launch Surveys

http://localhost:8000/survey/launch/290cf22a-3a97-4c4e-b5c3-eebc234821d3

http://localhost:8000/survey/support/e99e14d9-bd59-486f-970b-f092a07fd318

## Create Config Files

Within the following folder create two files

feedback/cuckoo/cuckoo

email_config.py

Within this file add:

MAIL_HOST = \<mail host\>

MAIL_PORT = \<mail port\>

MAIL_USER = \<mail user\>

MAIL_PASSWORD = \<mail password\>

MAIL_TLS = \<tls bool\>

site_config.py

Within this file add:

NAME = \<postgres database name\>

USER = \<postgress username\>

PASSWORD = \<postgres password\>
