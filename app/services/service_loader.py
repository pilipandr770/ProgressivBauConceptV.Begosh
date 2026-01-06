import json
import os
from ..config import Config

def load_services(direction):
    file_path = os.path.join(Config.SERVICES_DIR, f'{direction}.json')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []