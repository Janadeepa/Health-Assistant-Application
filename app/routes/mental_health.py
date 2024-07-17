from flask import Blueprint, request, jsonify
from app.services.mental_health_service import get_mental_health_resources

mental_health_blueprint = Blueprint('mental_health', __name__)

@mental_health_blueprint.route('/mental_health_resources', methods=['GET'])
def get_mental_health_resources_route():
    user_id = request.args.get('user_id')
    resources = get_mental_health_resources(user_id)
    return jsonify(resources)
