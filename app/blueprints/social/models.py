from datetime import datetime
import secrets 
import uuid
from werkzeug.security import check_password_hash, generate_password_hash

from app import db, login
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(100),index=True,unique=True)
    password_hash = db.Column(db.String(128))
    token = db.Column(db.String, unique= True)
    posts = db.relationship('Post', backref='author',lazy='dynamic')

    def __repr__(self):
        return f'User {self.username}'
    
    def set_token(self):
        setattr(self,'token',secrets.token_urlsafe(32))
        

    def set_id(self):
        return str(uuid.uuid4())
    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def commit(self):
        db.session.add(self)
        db.session.commit()
        
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f'Post by {self.author.username}: {self.body}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()