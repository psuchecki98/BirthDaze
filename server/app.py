from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
import os

from models import db, User, Birthday, Notification, Friend, Tag, BirthdayTag

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Birthdaze Database</h1>'

@app.route('/users', methods = ['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = User.query.all()

        if users:
            user_dict = [user.to_dict() for user in users]

            response = make_response(
                jsonify(user_dict),
                200
            )
            return response
        else:
            response = make_response(
                {
                    "error": "User not found."
                },
                404
            )
            return response
    elif request.method == 'POST':
        data = request.get_json()
        # try:
        new_user = User(
            username = data['username'],
            email = data['email'],
            password_hash = data['password_hash']
        )
        db.session.add(new_user)
        db.session.commit()
        response = make_response(
            jsonify(new_user.to_dict(rules = ())),
            201
        )
        return response
        
        # except ValueError:
        #     response = make_response(
        #         {
        #             "errors": "validiation errors"
        #         },
        #         400
        #     )
        #     return response
        
@app.route('/users/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def users_by_id(id):
    return ''

@app.route('/birthdays', methods = ['GET', 'POST'])
def birthdays():
    return ''

@app.route('/birthday/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def birthday_by_id(id):
    return ''

@app.route('/friends', methods = ['GET', 'POST'])
def friends():
    return ''

@app.route('/friends/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def friends_by_id(id):
    return ''



#Potential back routes for login and signup
# @app.route('/login')
# def login():
#     return ''

# @app.route('/signup')
# def signup():
#     return ''





if __name__ == '__main__':
    app.run(port=5555, debug=True)