from app import app
from flask import render_template

@app.route('/index')
@app.route('/')
def index():
  user = {'username': 'Guest'}
  return render_template('index.html', title='Home', user=user)