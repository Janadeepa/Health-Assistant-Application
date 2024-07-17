from app import db

class MentalHealthService:
    def get_mental_health_resources(self, user_id):
        resources = MentalHealthResource.query.filter_by(user_id=user_id).all()
        return resources
