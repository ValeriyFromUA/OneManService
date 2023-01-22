from sqlalchemy.orm import declarative_base

from db.db_engine import get_engine

Base = declarative_base()


def create_models():
    Base.metadata.create_all(get_engine())
