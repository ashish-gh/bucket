import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '1234')
    DEBUG = False


class LocalConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    local=LocalConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
