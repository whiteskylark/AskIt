import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
  SECRET_KEY = 'Basic g#fbxD2@&l3)sGN%87'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLLCHEMY_TRACK_MODIFICATIONS = False