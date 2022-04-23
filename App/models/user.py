from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    highscore = db.relationship('Highscore', backref='user', lazy=True) # sets up a relationship to todos which references Usedos = db.relationship('Todo', backref='user', lazy=True

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def toDict(self):
        return{
            'id': self.id,
            'username': self.username,
            "password": self.password
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def getNumHighScore(self):
      return len(self.todos)
      
    def getDoneHighScore(self):
        numDone = 0
        for todo in self.highscore:
          if highscore.done:
            numDone += 1
        return numDone 

    
class Highscore(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  highscore = db.Column(db.String(255), nullable=False)
  userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #set userid as a foreign key to user.id 

  def toDict(self):
   return {
     'id': self.id,
     'text': self.text,
     'userid': self.userid
   }

