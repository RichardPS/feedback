# Dev Tools

Dev tools for inital setup for testing purposes

## Inital Setup

Run the following command to setup a superuser and add mock data

```python devtools/run.py startup```

## Test URLS for mock data

### Launch Surveys

Create Launch Survey

http://localhost:8000/create/launch/

View Completed Launch Surveys (No secondary surveys)

http://localhost:8000/admin/launch/

View All Completed Launch Surveys

http://localhost:8000/admin/all-launch/

Link to launch Survey Questionnaire

http://localhost:8000/survey/launch/290cf22a-3a97-4c4e-b5c3-eebc234821d3

### Support Survey

Create Support Survey

http://localhost:8000/create/support/

View Completed Support Surveys (No secondary surveys)

http://localhost:8000/admin/support/

View All Completed Support Surveys

http://localhost:8000/admin/all-support/

Link to Support Survey Questionnaire

http://localhost:8000/survey/support/e99e14d9-bd59-486f-970b-f092a07fd318

## Create Config Files

Within the following folder create two files

feedback/cuckoo/cuckoo

```email_config.py```

Within this file add:

MAIL_HOST = _\<mail host\>_

MAIL_PORT = _\<mail port\>_

MAIL_USER = _\<mail user\>_

MAIL_PASSWORD = _\<mail password\>_

MAIL_TLS = _\<tls bool\>_

```site_config.py```

Within this file add:

NAME = _\<postgres database name\>_

USER = _\<postgress username\>_

PASSWORD = _\<postgres password\>_
