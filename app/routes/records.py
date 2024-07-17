from flask import Blueprint, request, jsonify
from app.services.record_service import get_medical_records

records_blueprint = Blueprint('records', __name__)

@records_blueprint.route('/medical_records', methods=['GET'])
def get_medical_records_route():
    user_id = request.args.get('user_id')
    medical_records = get_medical_records(user_id)
    return jsonify(medical_records)
