from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, drop_database, database_exists

from config import Config
from populate_data import get_users, get_goods, get_stores


db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)


class Goods(db.Model):
    __tablename__ = "goods"

    good_id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer, nullable=False)  # db.String() if error


class Stores(db.Model):
    __tablename__ = "stores"

    store_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


with app.app_context():
    if database_exists(db.engine.url):
        db.create_all()
        print("Database is exists. ")

    # elif drop_database(db.engine.url):
    #     print("Database is droped. ")

    else:
        create_database(db.engine.url)
        print("Database is created. ")


with app.app_context():
    users = get_users()
    for user in users:
        db.session.add(Users(**user))
    db.session.commit()
    print("Data writen to database successfully. ")

with app.app_context():
    goods = get_goods()
    for good in goods:
        db.session.add(Goods(**good))
    db.session.commit()
    print("Data (good/goods) writen to database successfully. ")

with app.app_context():
    stores = get_stores()
    for store in stores:
        db.session.add(Stores(**store))
    db.session.commit()
    print("Data (store/stores) writen to database successfully. ")
