from app import db

class AlertService:
    def send_alert(self, user_id, alert_type):
        alert = Alert(user_id=user_id, alert_type=alert_type)
        db.session.add(alert)
        db.session.commit()
