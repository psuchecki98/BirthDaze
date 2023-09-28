from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS
import os

from models import db, UserLogin, UserInfo

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Birthdaze Database</h1>'


@app.route('/userlogin', methods = ['GET', 'POST'])
def usersLogin():
    if request.method == 'GET':
        usersLogin = UserLogin.query.all()

        if usersLogin:

            userLogin_dict = [userLogin.to_dict() for userLogin in usersLogin]

            response = make_response(
                jsonify(userLogin_dict),
                200
            )
            return response
        else:
            response = make_response(
                {
                    "error": "Users Login not found."
                },
                404
            )
            return response
        
    elif request.method == 'POST':
        data = request.get_json()

        new_user_login = UserLogin(
            username = data['username'],
            email = data['email'],
            password_hash = data['password_hash']
        )

        db.session.add(new_user_login)
        db.session.commit()

        response = make_response(
            jsonify(new_user_login.to_dict(rules = ())),
            201
        )
        return response
    
@app.route('/userlogin/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
def user_login_by_id(id):
    userlogin = UserLogin.query.filter(UserLogin.id == id).first()

    if userlogin:

        if request.method == 'GET':
            userlogin_dict = userlogin.to_dict()

            response = make_response(
                jsonify(userlogin_dict),
                200
            )
            return response
        
        elif request.method == 'PATCH':
            data = request.get_json()

            try:
                for key in data:
                    setattr(userlogin, key, data[key])
                
                db.session.commit()
                response = make_response(
                    jsonify(userlogin.to_dict(rules = ())),
                    202
                )
            except ValueError:

                response = make_response(
                    { "errors": ["validation errors"] },
                    400
                )

        elif request.method == 'DELETE':

            db.session.delete(userlogin)
            db.session.commit()

            response = make_response(
                jsonify({}),
                204
            )
            return response
    else:
        response = make_response(
            { "error": "User not found" },
            404
        )
    return response

@app.route('/userinfo', methods = ['GET', 'POST'])
def usersInfo():
    if request.method == 'GET':
        users_info = UserInfo.query.all()

        if users_info:

            user_info_dict = [user_info.to_dict() for user_info in users_info]

            response = make_response(
                jsonify(user_info_dict),
                200
            )
            return response
        else:
            response = make_response(
                {
                    "error": "Users Info not found."
                },
                404
            )
            return response

    elif request.method == 'POST':
        data = request.get_json()

        new_user_info = UserInfo(
            user_login_id = data['user_login.id'],
            name = data['name'],
            birthdate = data['birthdate']
        )

        db.session.add(new_user_info)
        db.session.commit()

        response = make_response(
            jsonify(new_user_info.to_dict(rules = ())),
            201
        )
        return response



    
# @app.route('/userinfo/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
# def user_info_by_id(id):
#     userInfo = UserInfo.query.filter(UserInfo.id == id).first()

#     if userInfo:

#         if request.method == 'GET':

#             user_info_dict = userInfo.to_dict()

#             response = make_response(
#                 jsonify(user_info_dict),
#                 200
#             )
#             return response
        
#         elif request.method == 'PATCH':
#             data = request.get_json()

#             try:

#                 for key in data:
#                     setattr(userInfo, key, data[key])

#                 db.session.commit()

#                 response = make_response(
#                     jsonify(user_info_dict.to_dict(rules = ())),
#                     202    
#                 )
#             except ValueError:

#                 response = make_response(
#                     { "errors": ["validation errors"] },
#                     400
#                 )
#         elif request.method == 'DELETE':

#             db.session.delete(userInfo)
#             db.session.commit()

#             response = make_response(
#                 jsonify({}),
#                 204
#             )
#             return response
#     else:

#         response = make_response(
#             { "error": "User info not found." },
#             404
#         )
#     return response


# @app.route('/users', methods = ['GET', 'POST'])
# def users():
#     if request.method == 'GET':
#         users = User.query.all()

#         if users:
#             user_dict = [user.to_dict() for user in users]

#             response = make_response(
#                 jsonify(user_dict),
#                 200
#             )
#             return response
#         else:
#             response = make_response(
#                 {
#                     "error": "User not found."
#                 },
#                 404
#             )
#             return response
#     elif request.method == 'POST':
#         data = request.get_json()
#         #How it should start if you add the ValueError down there -- then indent new_user in one
        # try:
        # new_user = User(
        #     username = data['username'],
        #     email = data['email'],
        #     password_hash = data['password_hash']
        # )
        # db.session.add(new_user)
        # db.session.commit()
        # response = make_response(
        #     jsonify(new_user.to_dict(rules = ())),
        #     201
        # )
        # return response

        #Adding this ValueError, gets rid of the validation handlers on the models.py page -- ask how to fix potentially
        # except ValueError:
        #     response = make_response(
        #         {
        #             "errors": "validiation errors"
        #         },
        #         400
        #     )
        #     return response


# @app.route('/users/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
# def users_by_id(id):

#     user = User.query.filter(User.id == id).first()

#     if user:

#         if request.method == 'GET':

#             user_dict = user.to_dict()

#             response = make_response(
#                 jsonify(user_dict),
#                 200
#             )
#             return response

#         elif request.method == 'PATCH':
#             data = request.get_json()

#             try:

#                 for key in data:
#                     setattr(user, key, data[key])

#                 db.session.commit()

#                 response = make_response(
#                     jsonify(user.to_dict(rules = ())),
#                     202
#                 )
#             except ValueError:

#                 response = make_response(
#                     { "errors": ["validation errors"] },
#                     400
#                 )

    #     elif request.method == 'DELETE':

    #         db.session.delete(user)
    #         db.session.commit()

    #         response = make_response(
    #             jsonify({}),
    #             204
    #         )
    #         return response

    # else:

    #     response = make_response(
    #         { "error": "User not found" },
    #         404
    #     )

    # return response



# @app.route('/birthdays', methods = ['GET', 'POST'])
# def birthdays():
#     if request.method == 'GET':
#         birthdays = Birthday.query.all()

#         if birthdays:
#             birthday_dict = [birthday.to_dict() for birthday in birthdays]

#             response = make_response(
#                 jsonify(birthday_dict),
#                 200
#             )
#             return response
#         else:
#             response = make_response(
#                 {
#                     "error": "User not found."
#                 },
#                 404
#             )
#             return response

    # elif request.method == 'POST':
    #     data = request.get_json()

    #     new_birthday = Birthday(
    #         name = data['name'],
    #         date = data['date'],
    #         user_id = data['user.id'],
    #         friend_id = data['friend.id']
    #     )
    #     db.session.add(new_birthday)
    #     db.session.commit()
    #     response = make_response(
    #         jsonify(new_birthday.to_dict(rules = ())),
    #         201
    #     )
    #     return response


# @app.route('/birthday/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
# def birthday_by_id(id):
#     birthday = Birthday.query.filter(Birthday.id == id).first()

#     if birthday:

#         if request.method == 'GET':

#             birthday_dict = birthday.to_dict()

#             response = make_response(
#                 jsonify(birthday_dict),
#                 200
#             )
#             return response

#         elif request.method == 'PATCH':
#             data = request.get_json()

#             try:

#                 for key in data:
#                     setattr(birthday, key, data[key])

#                 db.session.commit()

#                 response = make_response(
#                     jsonify(birthday.to_dict(rules = ())),
#                     202
#                 )
#             except ValueError:

#                 response = make_response(
#                     { "errors": ["validation errors"] },
#                     400
#                 )

#         elif request.method == 'DELETE':

#             db.session.delete(birthday)
#             db.session.commit()

#             response = make_response(
#                 jsonify({}),
#                 204
#             )
#             return response

#     else:

#         response = make_response(
#             { "error": "Birthday not found" },
#             404
#         )

#     return response

# @app.route('/friends', methods = ['GET', 'POST'])
# def friends():
#     if request.method == 'GET':
#         friends = Friend.query.filter(Friend.user_id == id)

#         if friends:
#             friend_dict = [friend.to_dict() for friend in friends]

#             response = make_response(
#                 jsonify(friend_dict),
#                 200
#             )
#             return response
#         else:
#             response = make_response(
#                 {
#                     "error": "User not found."
#                 },
#                 404
#             )
#             return response

#     elif request.method == 'POST':
#         data = request.get_json()

#         new_friend = Friend(
#             name = data['name'],
#             email = data['email'],
#             user_id = data['user.id'],
#         )
#         db.session.add(new_friend)
#         db.session.commit()
#         response = make_response(
#             jsonify(new_friend.to_dict(rules = ())),
#             201
#         )
#         return response

# @app.route('/friends/<int:id>', methods = ['GET', 'PATCH', 'DELETE'])
# def friends_by_id(id):
#     friend = Friend.query.filter(Friend.id == id).first()

#     if friend:

#         if request.method == 'GET':

#             friend_dict = friend.to_dict()

#             response = make_response(
#                 jsonify(friend_dict),
#                 200
#             )
#             return response

#         elif request.method == 'PATCH':
#             data = request.get_json()

#             try:

#                 for key in data:
#                     setattr(friend, key, data[key])

#                 db.session.commit()

#                 response = make_response(
#                     jsonify(friend.to_dict(rules = ())),
#                     202
#                 )
#             except ValueError:

#                 response = make_response(
#                     { "errors": ["validation errors"] },
#                     400
#                 )

#         elif request.method == 'DELETE':

#             db.session.delete(friend)
#             db.session.commit()

#             response = make_response(
#                 jsonify({}),
#                 204
#             )
#             return response

#     else:

#         response = make_response(
#             { "error": "Friend not found" },
#             404
#         )

#     return response



#Potential back routes for login and signup
# @app.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     email = data['email']
#     password = data['password']

#     user = User.query.filter_by(email=email).first()

#     if user and user.check_password(password):
#         return {"success": True, "message": "Logged in successfully."}
#     else:
#         return {"success": False, "message": "Invalid credentials."}, 401

# @app.route('/signup', methods=['POST'])
# def signup():
#     data = request.json

#     username = data['username']
#     email = data['email']
#     password = data['password']
#     existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
#     if existing_user:
#         return {"success": False, "message": "Username or email already in use."}, 400

#     new_user = User(username=username, email=email)
#     new_user.set_password(password)
#     db.session.add(new_user)
#     db.session.commit()

#     return {"success": True, "message": "Account created successfully."}





if __name__ == '__main__':
    app.run(port=5555, debug=True)
