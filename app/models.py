from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

class HealthData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('health_data', lazy=True))
    heart_rate = db.Column(db.Float)
    blood_pressure = db.Column(db.Float)
    sleep_quality = db.Column(db.Float)
    activity_level = db.Column(db.Float)

class MedicalRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('medical_records', lazy=True))
    diagnosis = db.Column(db.String(200))
    treatment = db.Column(db.String(200))
    medication = db.Column(db.String(200))
