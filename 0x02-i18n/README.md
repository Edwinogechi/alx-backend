
0x02. i18n with Flask-Babel and pytz
This project aims to provide a comprehensive tutorial on internationalization (i18n) using Flask-Babel and pytz with Flask framework.

Introduction
Internationalization is the process of designing and developing a software application so that it can be adapted to various languages and regions without engineering changes. In the context of web development, Flask-Babel is a Flask extension that adds i18n and l10n support to Flask applications.

Features
Flask-Babel: Flask-Babel integrates the Babel library into Flask, providing support for message translation and locale-specific formatting.

pytz: pytz is a Python library that brings the Olson tz database into Python, allowing accurate and cross-platform timezone calculations.

Setup
Install Flask-Babel:

bash
Copy code
pip install Flask-Babel
Install pytz:

bash
Copy code
pip install pytz
Usage
Initializing Flask-Babel:

python
Copy code
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
Setting up translations:

Flask-Babel requires message catalogs to be set up for each language. You can use the babel.cfg file to specify the configurations.

Creating message catalogs:

Message catalogs are files that contain translations for different languages. These files are typically .po files that can be compiled into .mo files.

Using translations in templates:

You can mark translatable strings in your templates using the gettext() function:

jinja
Copy code
<h1>{{ _('Hello, World!') }}</h1>
Configuring timezones with pytz:

pytz allows you to work with timezones in your Flask application. You can set the timezone for your application using:

python
Copy code
import pytz

app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
Contribution
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on GitHub.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Flask-Babel: https://pythonhosted.org/Flask-Babel/
pytz: http://pytz.sourceforge.net


Tasks
0. Basic Flask app
mandatory
First you will setup a basic Flask app in 0-app.py. Create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title (<title>) and “Hello world” as header (<h1>).


1. Basic Babel setup
mandatory
Install the Babel Flask extension:

$ pip3 install flask_babel==2.0.0
Then instantiate the Babel object in your app. Store it in a module-level variable named babel.

In order to configure available languages in our app, you will create a Config class that has a LANGUAGES class attribute equal to ["en", "fr"].

Use Config to set Babel’s default locale ("en") and timezone ("UTC").

Use that class as config for your Flask app.


2. Get locale from request
mandatory
Create a get_locale function with the babel.localeselector decorator. Use request.accept_languages to determine the best match with our supported languages.


3. Parametrize templates
mandatory
Use the _ or gettext function to parametrize your templates. Use the message IDs home_title and home_header.

Create a babel.cfg file containing

[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
Then initialize your translations with

$ pybabel extract -F babel.cfg -o messages.pot .
and your two dictionaries with

$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
Then edit files translations/[en|fr]/LC_MESSAGES/messages.po to provide the correct value for each message ID for each language. Use the following translations:

msgid	English	French
home_title	"Welcome to Holberton"	"Bienvenue chez Holberton"
home_header	"Hello world!"	"Bonjour monde!"
Then compile your dictionaries with

$ pybabel compile -d translations
Reload the home page of your app and make sure that the correct messages show up.

Repo:

GitHub repository: alx-backend
Directory: 0x02-i18n
File: 3-app.py, babel.cfg, templates/3-index.html, translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po, translations/en/LC_MESSAGES/messages.mo, translations/fr/LC_MESSAGES/messages.mo
  
4. Force locale with URL parameter
mandatory
In this task, you will implement a way to force a particular locale by passing the locale=fr parameter to your app’s URLs.

In your get_locale function, detect if the incoming request contains locale argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting http://127.0.0.1:5000?locale=[fr|en].

Visiting http://127.0.0.1:5000/?locale=fr should display this level 1 heading: 

Repo:

GitHub repository: alx-backend
Directory: 0x02-i18n
File: 4-app.py, templates/4-index.html
 
5. Mock logging in
mandatory
Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in 5-app.py.

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
This will mock a database user table. Logging in will be mocked by passing login_as URL parameter containing the user ID to log in as.

Define a get_user function that returns a user dictionary or None if the ID cannot be found or if login_as was not passed.

Define a before_request function and use the app.before_request decorator to make it be executed before all other functions. before_request should use get_user to find a user if any, and set it as a global on flask.g.user.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

msgid	English	French
logged_in_as	"You are logged in as %(username)s."	"Vous êtes connecté en tant que %(username)s."
not_logged_in	"You are not logged in."	"Vous n'êtes pas connecté."
Visiting http://127.0.0.1:5000/ in your browser should display this:



Visiting http://127.0.0.1:5000/?login_as=2 in your browser should display this: 

Repo:

GitHub repository: alx-backend
Directory: 0x02-i18n
File: 5-app.py, templates/5-index.html
 
6. Use user locale
mandatory
Change your get_locale function to use a user’s preferred local if it is supported.

The order of priority should be

Locale from URL parameters
Locale from user settings
Locale from request header
Default locale
Test by logging in as different users



Repo:

GitHub repository: alx-backend
Directory: 0x02-i18n
File: 6-app.py, templates/6-index.html
 
7. Infer appropriate time zone
mandatory
Define a get_timezone function and use the babel.timezoneselector decorator.

The logic should be the same as get_locale:

Find timezone parameter in URL parameters
Find time zone from user settings
Default to UTC
Before returning a URL-provided or user time zone, you must validate that it is a valid time zone. To that, use pytz.timezone and catch the pytz.exceptions.UnknownTimeZoneError exception.

Repo:

GitHub repository: alx-backend
Directory: 0x02-i18n
File: 7-app.py, templates/7-index.html
Copyright © 2024 ALX, All rights reserved.

8. Display the current time
#advanced
Based on the inferred time zone, display the current time on the home page in the default format. For example:

Jan 21, 2020, 5:55:39 AM or 21 janv. 2020 à 05:56:28

Use the following translations

msgid	English	French
current_time_is	"The current time is %(current_time)s."	"Nous sommes le %(current_time)s."
Displaying the time in French looks like this:



Displaying the time in English looks like this:



