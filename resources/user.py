from flask import Blueprint
from flask_restful import Api, Resource, abort

user_bp = Blueprint('user', __name__)
api = Api(user_bp)

USERS = {
    'user1': {'task': 'build an API'},
    'user2': {'task': '?????'},
    'user3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(user_id):
    if user_id not in USERS:
        abort(404, message="User {} doesn't exist".format(user_id))


class User(Resource):
    def get(self, user_id):
        abort_if_todo_doesnt_exist(user_id)
        return USERS[user_id]


class UserList(Resource):
    def get(self):
        return USERS


api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<user_id>')
