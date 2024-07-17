from flask import Blueprint, request, jsonify
from app.services.community_service import get_community_support

community_blueprint = Blueprint('community', __name__)

@community_blueprint.route('/community_support', methods=['GET'])
def get_community_support_route():
    user_id = request.args.get('user_id')
    support = get_community_support(user_id)
    return jsonify(support)
