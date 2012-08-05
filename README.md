dgentledjango
=============

These are sample applications that walk through creating a fully featured
website. The modules start from straightforward template displays, and lead
you to a site the registers users and allow modifications.

Requirements
============
Django==1.4.1
MySQL-python==1.2.3
django-registration==0.8
django-registration-defaults==0.3
wsgiref==0.1.2

Installation
===========
Modify TEMPLATE_DIRS in dgentledjango/settings.py to point to the correct
templates path.

Create a database, and set the database access settings correctly in dgentledjango/settings.py

```python manage.py syncdb
python manage.py runserver
```

Modules
=======

* intro/
 * Simple template website

* classlist/
 * Show information from a database

* forminput/
 * Allow users to add information to the database through a webform.

* userreg/
 * Require user registration to view and modify the database
