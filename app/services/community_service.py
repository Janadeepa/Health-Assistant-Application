from app import db

class CommunityService:
    def get_community_support(self, user_id):
        support = CommunitySupport.query.filter_by(user_id=user_id).all()
        return support
