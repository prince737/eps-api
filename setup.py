from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:rootuser@localhost:5432/eps'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['USER_IMAGE_FODLER'] = 'Users/profile_images'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

db.create_all