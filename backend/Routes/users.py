from flask import Blueprint, request, jsonify
from Controllers.user_controller import get_users_controller, post_user_controller
from flask_cors import CORS, cross_origin

users = Blueprint('users', __name__)
path = '/users'


@users.route(f"{path}", methods=['GET'])
@cross_origin()
def get_users():
    return get_users_controller()


@users.route(f"{path}", methods=['POST'])
@cross_origin()
def post_user():
    return post_user_controller()
