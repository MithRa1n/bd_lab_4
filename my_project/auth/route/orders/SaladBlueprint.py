from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import salad_controller
from my_project.auth.domain.orders.Salad import Salad

salad_bp = Blueprint('salad', __name__, url_prefix='/salad')

@salad_bp.get('')
def get_all_salads() -> Response:
    salads = salad_controller.find_all()
    salads_dto = [salad.put_into_dto() for salad in salads]
    return make_response(jsonify(salads_dto), HTTPStatus.OK)

@salad_bp.post('')
def create_salad() -> Response:
    content = request.get_json()
    salad = Salad.create_from_dto(content)
    salad_controller.create(salad)
    return make_response(jsonify(salad.put_into_dto()), HTTPStatus.CREATED)

@salad_bp.get('/<int:salad_id>')
def get_salad(salad_id: int) -> Response:
    salad = salad_controller.find_by_id(salad_id)
    if salad:
        return make_response(jsonify(salad.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Salad not found"}), HTTPStatus.NOT_FOUND)

@salad_bp.put('/<int:salad_id>')
def update_salad(salad_id: int) -> Response:
    content = request.get_json()
    salad = Salad.create_from_dto(content)
    salad_controller.update(salad_id, salad)
    return make_response("Salad updated", HTTPStatus.OK)

@salad_bp.delete('/<int:salad_id>')
def delete_salad(salad_id: int) -> Response:
    salad_controller.delete(salad_id)
    return make_response("Salad deleted", HTTPStatus.NO_CONTENT)
