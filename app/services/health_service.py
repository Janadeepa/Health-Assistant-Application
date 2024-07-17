from app import db

class HealthService:
    def get_health_data(self, user_id):
        health_data = HealthData.query.filter_by(user_id=user_id).first()
        return health_data
