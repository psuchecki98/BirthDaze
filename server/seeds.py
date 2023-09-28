from faker import Faker
from models import db, UserLogin, UserInfo
from app import app

fake = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Wiping the database.")
        UserLogin.query.delete()
        UserInfo.query.delete()
        db.session.commit()

        print("Seeding the database.")
        
        for _ in range(20):
            userlogin = UserLogin(
                username=fake.user_name(),
                email=fake.email(),
                password_hash=fake.password()
            )
            db.session.add(userlogin)
            db.session.commit()
            db.session.refresh(userlogin)  # Refresh the object to get the id

            userInfo = UserInfo(
                user_login_id=userlogin.id,  # Now this should have a value
                name=fake.name(),
                birthdate=fake.date_of_birth(minimum_age=1, maximum_age=99)
            )
            db.session.add(userInfo)

        db.session.commit()
        print("Database seeded.")



#OLD SEED.PY in case the new one is broken

# if __name__ == '__main__':
#     with app.app_context():
#         print("Wiping the database.")
        # User.query.delete()
        # Birthday.query.delete()
        # Friend.query.delete()


#Seeding Users, Birthdays, Notifications, Friends, Tags, and more
#----------------------------------------------------------------
    # Creates empty lists for users, birthdays and friends
        # users = []
        # birthdays = []
        # friends = []

    # Creates Fake Users/Birthdays/Friends
        # for _ in range(20):
        #     user = User(
        #         username = fake.user_name(),
        #         email = fake.email(),
        #         password_hash = fake.password()
        #     )
        #     users.append(user)
        #     db.session.add(user)
        #     db.session.commit()

        #     birthday = Birthday(
        #         name = fake.name(), 
        #         date = fake.date_of_birth(minimum_age=1, maximum_age=99),
        #         user_id = user.id
        #     )
        #     birthdays.append(birthday)
        #     db.session.add(birthday)
 
        #     for _ in range(random.randint(5, 25)):
        #         friend = Friend(
        #             name = fake.name(),
        #             email = fake.email(),
        #             user_id = user.id
        #         )
        #         friends.append(friend)
        #         db.session.add(friend)
        #         db.session.commit()

        #         friend_birthday = Birthday(
        #             name = friend.name,
        #             date = fake.date_of_birth(minimum_age=1, maximum_age=99),
        #             friend_id = friend.id
        #         )
        #         birthdays.append(friend_birthday)
        #         db.session.add(friend_birthday)

        #     db.session.commit()

