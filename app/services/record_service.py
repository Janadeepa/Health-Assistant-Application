from app import db

class RecordService:
    def get_medical_records(self, user_id):
        medical_records = MedicalRecord.query.filter_by(user_id=user_id).all()
        return medical_records
