from flask import Blueprint

health_blueprint = Blueprint('health', __name__)
recommendations_blueprint = Blueprint('recommendations', __name__)
alerts_blueprint = Blueprint('alerts', __name__)
mental_health_blueprint = Blueprint('mental_health', __name__)
nutrition_blueprint = Blueprint('nutrition', __name__)
fitness_blueprint = Blueprint('fitness', __name__)
records_blueprint = Blueprint('records', __name__)
community_blueprint = Blueprint('community', __name__)

from app.routes import health, recommendations, alerts, mental_health, nutrition, fitness, records, community
