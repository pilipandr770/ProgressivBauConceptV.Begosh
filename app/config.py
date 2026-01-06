import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'
    DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    SERVICES_DIR = os.path.join(DATA_DIR, 'services')
    BOOKINGS_FILE = os.path.join(DATA_DIR, 'bookings.json')
    CONTACTS_FILE = os.path.join(DATA_DIR, 'contacts.json')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

    # Future mail settings
    MAIL_SERVER = 'smtp.example.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = None
    MAIL_PASSWORD = None