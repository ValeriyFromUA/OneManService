from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy_utils import create_database, database_exists

from oms.config import DATABASE_URI


def get_engine(url: str = DATABASE_URI) -> Engine:
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url)
    return engine


def get_session() -> Session:
    session = sessionmaker(bind=get_engine())
    return session()
