from flask import Blueprint
from flask_restful import Api

from grocery_store.routes.users import Users


users = Blueprint("users", __name__)

api_users = Api(users)

api_users.add_resource(Users, "/users", "/users/<user_id>")
