from App.models import User
from App.database import db


def get_all_users():
    return User.query.all()

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.toDict() for user in users]
    return users

def get_all_users():
    return User.query.all()

def is_active(self):
    """True, as all users are active."""
    return True

def get_id(self):
    """Return the email address to satisfy Flask-Login's requirements."""
    return self.username

def is_authenticated(self):
    """Return True if the user is authenticated."""
    return self.authenticated

def is_anonymous(self):
    """False, as anonymous users aren't supported."""
    return False