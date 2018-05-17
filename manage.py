from kanyemadness import app, db
from models import Choices
from flask_script import Manager, prompt_bool
from views import *


manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    db.session.commit()
    print ("Initialize the Database")

@manager.command
def dropdb():
    if prompt_bool(
        "Are you sure you want to lose all your data"):
        db.drop_all()
        print ("Dropped the database")

if __name__ == "__main__":
    manager.run()