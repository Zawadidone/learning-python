# project/_config.py

import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = "flask"
CSRF_ENABLED = True
SECRET_KEY = "my_precious"

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = "mysql://root:asdf@localhost/flask"
SQLALCHEMY_TRACK_MODIFICATIONS = True
