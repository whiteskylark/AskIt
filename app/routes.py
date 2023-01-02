from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/index')
@app.route('/')
def index():
  user = {'username': 'Guest'}
  return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash(f'User {form.username.data} succesfully logged in!')
    return redirect(url_for('index'))
  return render_template('login.html', title='Login', form=form)