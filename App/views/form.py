from flask import Blueprint, redirect, render_template, request, send_from_directory, url_for
from flask import flash
from App.forms import SignUp, LogIn
from App.models import User

from App.database import db
from App.controllers import create_user

form_views = Blueprint('form_views', __name__, template_folder='../templates')

@form_views.route('/signup', methods=['GET'])
def signup():
  form = SignUp() # create form object
  return render_template('signup.html', form=form) # pass form object to template

'''
How to signup with server side rendering
0. assume html form submission with POST method
1. create a post route
2. take data from form
3. check if form is valid
4. if form is invalid flash error message and redirect user
5. else get data from form
6. create model object from data
7. save object to db
8. flash success message
9. redirect user
'''
@form_views.route('/signup', methods=['POST'])
def signupAction():
  form = SignUp() # create form object
  if form.validate_on_submit():
    data = request.form # get data from form submission
    create_user = User(username=data['username'], password=data['password']) # create user object
    create_user.set_password(data['password']) # set password
    db.session.add(create_user) # save new user
    db.session.commit()
    flash('Account Created!')# send message
    return render_template('login.html', form=form)# redirect to login page
  flash('Error invalid input!')
  return render_template('signup.html', form=form)

@form_views.route('/signup/lol')
def lol():
    return 'lol'

