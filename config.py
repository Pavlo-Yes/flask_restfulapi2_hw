class Config:
    DEBUG = False


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/test_db5'
    SECRET_KEY = 'very secret key'
