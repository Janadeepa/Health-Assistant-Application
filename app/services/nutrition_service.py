from app import db

class NutritionService:
    def get_nutrition_plan(self, user_id):
        nutrition_plan = NutritionPlan.query.filter_by(user_id=user_id).first()
        return nutrition_plan
