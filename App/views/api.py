from flask import Blueprint, redirect, render_template, request, send_from_directory, url_for
from flask_login import login_user, logout_user, login_required
from flask import flash
from App.forms import LogIn, HighScore
from App.models import User, Highscore


api_views = Blueprint('api_views', __name__, template_folder='../templates')

@api_views.route('/', methods=['GET'])
def get_api_docs():
    return render_template('index.html')

@api_views.route('/logout', methods=['GET'])
@login_required
def logout():
  logout_user()
  flash('Logged Out!')
  return render_template('index.html')

@api_views.route('/info', methods=['GET'])
def info():
  return render_template('info.html')

@api_views.route('/login', methods=['GET'])
def index():
  form = LogIn()
  return render_template('login.html', form=form) # pass form object to template

@api_views.route('/randomword', methods=['GET'])
def randomWord():
  return render_template('random.html') # pass form object to template

@api_views.route('/rapidword', methods=['GET'])
def rapidWord():
  form = HighScore()
  return render_template('rapid.html', form=form) # pass form object to template

@api_views.route('/highscore', methods=['GET'])
@login_required
def highScore():
  return render_template('highscore.html') # pass form object to template

#user submits the login form
@api_views.route('/login', methods=['POST'])
def loginAction():
  form = LogIn()
  if form.validate_on_submit(): # respond to form submission
      data = request.form
      user = User.query.filter_by(username = data['username']).first()
      if user and user.check_password(data['password']): # check credentials
        flash('Logged in successfully.') # send message to next page
        login_user(user) # login the user
        return render_template('index.html', form=form) # redirect to main page if login successful
  flash('Invalid credentials')
  return render_template('login.html', form=form)