from app import db

class FitnessService:
    def get_workout_plan(self, user_id):
        workout_plan = WorkoutPlan.query.filter_by(user_id=user_id).first()
        return workout_plan
