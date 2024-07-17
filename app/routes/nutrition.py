from flask import Blueprint, request, jsonify
from app.services.nutrition_service import get_nutrition_plan

nutrition_blueprint = Blueprint('nutrition', __name__)

@nutrition_blueprint.route('/nutrition_plan', methods=['GET'])
def get_nutrition_plan_route():
    user_id = request.args.get('user_id')
    nutrition_plan = get_nutrition_plan(user_id)
    return jsonify(nutrition_plan)
