from flask import Blueprint, request, jsonify
from app.services.alert_service import send_alert

alerts_blueprint = Blueprint('alerts', __name__)

@alerts_blueprint.route('/alerts', methods=['POST'])
def send_alert_route():
    user_id = request.json.get('user_id')
    alert_type = request.json.get('alert_type')
    send_alert(user_id, alert_type)
    return jsonify({'message': 'Alert sent successfully'})
