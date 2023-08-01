from faker import Faker
import random
from models import db, User, Birthday, Notification, Friend, Tag, BirthdayTag
from datetime import datetime, timedelta
from app import app

fake = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Wiping the database.")
        User.query.delete()
        Birthday.query.delete()
        Friend.query.delete()

#Seeding Users, Birthdays, Notifications, Friends, Tags, and more
#----------------------------------------------------------------
    # Creates fake users
        users = []
        for _ in range(50):
            user = User(
                username = fake.user_name(),
                email = fake.email(),
                password_hash = fake.password()
            )

            users.append(user)
            db.session.add(user)

        db.session.commit()
            
    #Creates Birthdays for Users
        birthdays = []
        for user in users:
            birthday = Birthday(
                name = fake.name(),
                date = fake.date_object(),
                user_id = user.id
            )
            birthdays.append(birthday)
            db.session.add(birthday)
        
        db.session.commit()




#Need to figure out the logic behind this a bit more before proceeding.
#Thoughts to remember:
#Friends are just other Users, generating random Friends does not make them Users
#in the sense of the database. The database only generates 50 Users and 50 correlating
#Birthdays, when you add the bode below we generate random integer of friends for a User
#between 1, 15 but technically none of these Friends have birthdays at the moment
#Try to think of a way to either make this work, or how to get friends to have arelationship with birthdays
#It's breaking my head

    #Creates Friends for Users
        # friends = []
        # rand_friend_amount = random.randint(1,15)
        # for user in users:
        #     for _ in range(rand_friend_amount):
        #         friend = Friend(
        #             name = fake.name(),
        #             email = fake.email(),
        #             user_id = user.id
        #         )
        #         friends.append(friend)
        #         db.session.add(friend)
            
        # db.session.commit()
