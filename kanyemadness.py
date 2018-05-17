from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Lucky888@localhost/kanyemadness1'
db = SQLAlchemy(app)

#log in management init

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

