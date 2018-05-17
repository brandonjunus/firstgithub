from kanyemadness import db
from sqlalchemy import desc
from flask_login import UserMixin


class Choices(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), unique = True)
    choice1 = db.Column(db.String(300))
    choice2 = db.Column(db.String(300))
    choice3 = db.Column(db.String(300))
    choice4 = db.Column(db.String(300))


    @staticmethod
    def newest():
        return Choices.query.order_by(desc(Choices.id)).limit(1)

    def __init__(self, username, choice1, choice2, choice3, choice4):
        self.username = username
        self.choice1 = choice1
        self.choice2 = choice2
        self.choice3 = choice3
        self.choice4 = choice4

from flask_login import LoginManager, UserMixin
from kanyemadness import login_manager
class User (UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), unique= True)
    email = db.Column(db.String(50), unique= True)
    password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    



