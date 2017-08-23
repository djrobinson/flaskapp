import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktask.db'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'supersecret'

DATABASE_PATH = os.path.join(basedir, DATABASE)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH