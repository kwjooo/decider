from application import db
from flask import Blueprint, jsonify
from flask_restful import reqparse, Api, Resource, abort
from models.group import Group
from models.user import User
from datetime import time
from constants import LUNCH_TIME, DINNER_TIME
import uuid

group_bp = Blueprint('group', __name__)
api = Api(group_bp)


class GroupList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str, location='json',
        required=True, help='The group\'s name'
    )
    parser.add_argument(
        'address',
        type=str, location='json',
        required=True, help='The group\'s address'
    )
    parser.add_argument(
        'users',
        type=list, location='json',
        required=True, help='The group\'s members'
    )
    parser.add_argument(
        'lunch_time',
        type=time, location='json',
        required=False, default=LUNCH_TIME,
        help='The group\'s lunch time'
    )
    parser.add_argument(
        'dinner_time',
        type=time, location='json',
        required=False, default=DINNER_TIME,
        help='The group\'s dinner time'
    )

    def post(self):
        args = self.parser.parse_args()

        group_id = str(uuid.uuid4())
        group = Group(id=group_id,
                      name=args['name'],
                      address=args['address'],
                      lunch_time=args['lunch_time'],
                      dinner_time=args['dinner_time']
                      )
        user_list = args['users']
        for user_id in user_list:
            user = User.query.get(user_id)
            user.groups.append(group)

        db.session.add(group)
        db.session.commit()

        response = {
            'result': 'ok',
            'group_id': group_id
        }

        return response, 201


class GroupUserList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'user_id',
        type=str, location='json',
        required=True, help='The user_id to invite'
    )

    def get(self, group_id):
        group = Group.query.get(group_id)
        if group is None:
            abort(404, message="Group {} doesn't exist".format(group_id))

        users = []

        for user in group.users:
            users.append({
                'user_id': user.id,
                'id': user.user_id,
                'nickname': user.nickname
            })

        response = {
            'group_id': group.id,
            'users': users
        }

        return response, 200

    def post(self, group_id):
        group = Group.query.get(group_id)
        if group is None:
            abort(404, message="Group {} doesn't exist".format(group_id))

        args = self.parser.parse_args()

        user = User.query.get(args['user_id'])
        if user is None:
            abort(404, message="User {} doesn't exist".format(args['user_id']))

        user.groups.append(group)
        db.session.add(user)
        db.session.commit()

        response = {
            'result': 'ok'
        }
        return response, 201


class GroupUser(Resource):
    def delete(self, group_id, user_id):
        user = User.query.get(user_id)
        if user is None:
            abort(404, message="User {} doesn't exist".format(user_id))

        group = Group.query.get(group_id)
        if group is None:
            abort(404, message="Group {} doesn't exist".format(group_id))

        user.groups.remove(group)
        db.session.commit()

        response = {
            'result': 'ok'
        }
        return response, 200


api.add_resource(GroupList, '/groups')
api.add_resource(GroupUserList, '/groups/<group_id>/users')
api.add_resource(GroupUser, '/groups/<group_id>/users/<user_id>')
