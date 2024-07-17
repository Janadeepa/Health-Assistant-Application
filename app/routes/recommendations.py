from flask import Blueprint, request, jsonify
from app.services.recommendation_service import get_recommendations

recommendations_blueprint = Blueprint('recommendations', __name__)

@recommendations_blueprint.route('/recommendations', methods=['GET'])
def get_recommendations_route():
    user_id = request.args.get('user_id')
    recommendations = get_recommendations(user_id)
    return jsonify(recommendations)
