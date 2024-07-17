from app import db

class RecommendationService:
    def get_recommendations(self, user_id):
        recommendations = Recommendation.query.filter_by(user_id=user_id).all()
        return recommendations
