import hashlib
import datetime

def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def format_date(date):
    return date.strftime("%Y-%m-%d %H:%M:%S")

def get_current_date():
    return datetime.datetime.now()

def calculate_bmi(weight, height):
    return weight / (height ** 2)
