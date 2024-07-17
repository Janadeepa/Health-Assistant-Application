from flask import Blueprint, request, jsonify
from app.services.health_service import get_health_data

health_blueprint = Blueprint('health', __name__)

@health_blueprint.route('/health_data', methods=['GET'])
def get_health_data_route():
    user_id = request.args.get('user_id')
    health_data = get_health_data(user_id)
    return jsonify(health_data)
