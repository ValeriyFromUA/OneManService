from db.db_manager import add_fake_data_to_db
from models.base import create_models

if __name__ == '__main__':
    create_models()
    add_fake_data_to_db()
