from flask import Blueprint, request, jsonify
from app.services.fitness_service import get_workout_plan

fitness_blueprint = Blueprint('fitness', __name__)

@fitness_blueprint.route('/workout_plan', methods=['GET'])
def get_workout_plan_route():
    user_id = request.args.get('user_id')
    workout_plan = get_workout_plan(user_id)
    return jsonify(workout_plan)
