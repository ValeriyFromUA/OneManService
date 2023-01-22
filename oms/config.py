VER = 'v1'
ROUTE = f'//{VER}'
DATABASE_URI = 'sqlite:///D:\\Python\\OneManService\\db\\one_man_service.db'


class Config:
    HOST = 'localhost'
    PORT = 5000
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
