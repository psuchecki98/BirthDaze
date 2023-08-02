from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_only = ('id', 'username', 'email', 'password_hash')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @validates('username')
    def validate_username(self, key, username):
        if len(username) >= 3 and len(username) <= 16:
            return username
        else: 
            raise ValueError("Username must be between 3-16 characters.")
        
    @validates('email')
    def validate_email(self, key, email):
        if '@' in email:
            if email[-4:] in ['.com', '.org', '.net']:
                return email
            else:
                raise ValueError("Email must end in .com, .org, or .net")
        else:
            raise ValueError("Email must include @.")
        
    @validates('password_hash')
    def validate_password(self, key, password_hash):
        if len(password_hash) >= 5 and len(password_hash) <= 16:
            return password_hash
        else:
            raise ValueError("Password must be between 5-16 characters.")
        

class Birthday(db.Model, SerializerMixin):
    __tablename__ = 'birthdays'

    serialize_only = ('id', 'name', 'date', 'user_id', 'friend_id')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    friend_id = db.Column(db.Integer, db.ForeignKey('friends.id'))

    user = db.relationship('User', backref='birthdays')
    friend = db.relationship('Friend', backref='birthdays')


class Notification(db.Model, SerializerMixin):
    __tablename__ = 'notifications'

    serialize_only = ('id', 'message', 'timestamp', 'user_id')

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, default= datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref='notifications')


class Friend(db.Model, SerializerMixin):
    __tablename__ = 'friends'

    serialize_only = ('id', 'name', 'email', 'user_id')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref='friends')



class Tag(db.Model, SerializerMixin):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref='tags')

    #Many to Many relationship between tags and birthdays
    birthdays = db.relationship('Birthday', secondary= 'birthday_tags', backref='tags')


class BirthdayTag(db.Model, SerializerMixin):
    __tablename__ = 'birthday_tags'

    id = db.Column(db.Integer, primary_key=True)
    birthday_id = db.Column(db.Integer, db.ForeignKey('birthdays.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))



