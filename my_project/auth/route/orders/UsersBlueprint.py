from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import users_controller
from my_project.auth.domain.orders.Users import Users

users_bp = Blueprint('users', __name__, url_prefix='/users')

@users_bp.get('')
def get_all_users() -> Response:
    users = users_controller.find_all()
    users_dto = [user.put_into_dto() for user in users]
    return make_response(jsonify(users_dto), HTTPStatus.OK)

@users_bp.post('')
def create_user() -> Response:
    content = request.get_json()
    user = Users.create_from_dto(content)
    users_controller.create(user)
    return make_response(jsonify(user.put_into_dto()), HTTPStatus.CREATED)

@users_bp.get('/<int:user_id>')
def get_user(user_id: int) -> Response:
    user = users_controller.find_by_id(user_id)
    if user:
        return make_response(jsonify(user.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "User not found"}), HTTPStatus.NOT_FOUND)

@users_bp.put('/<int:user_id>')
def update_user(user_id: int) -> Response:
    content = request.get_json()
    user = Users.create_from_dto(content)
    users_controller.update(user_id, user)
    return make_response("User updated", HTTPStatus.OK)

@users_bp.delete('/<int:user_id>')
def delete_user(user_id: int) -> Response:
    users_controller.delete(user_id)
    return make_response("User deleted", HTTPStatus.NO_CONTENT)
