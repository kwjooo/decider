from flask import Blueprint
from flask_restful import Api, Resource, abort

user_bp = Blueprint('user', __name__)
api = Api(user_bp)

USERS = {
    'user1': {'task': 'build an API'},
    'user2': {'task': '?????'},
    'user3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in USERS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


class UserList(Resource):
    def get(self):
        return USERS


api.add_resource(UserList, '/users')
